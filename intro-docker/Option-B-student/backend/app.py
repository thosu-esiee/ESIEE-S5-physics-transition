"""Supplied Flask API: students configure its environment, not its Python code."""
import os
from pathlib import Path
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)


def password():
    secret_file = os.environ.get("DB_PASSWORD_FILE")
    if not secret_file:
        raise RuntimeError("DB_PASSWORD_FILE must be configured")
    return Path(secret_file).read_text(encoding="utf-8").strip()


def db():
    return pymysql.connect(
        host=os.environ.get("DB_HOST", "mysql"),
        port=int(os.environ.get("DB_PORT", "3306")),
        user=os.environ.get("DB_USER", "energy_user"),
        password=password(),
        database=os.environ.get("DB_NAME", "energy_lab"),
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5,
    )


@app.get("/api/health")
def health():
    with db() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
    return jsonify(status="ok")


@app.get("/api/measurements")
def measurements():
    with db() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT CAST(measurement_date AS CHAR) AS measurement_date,
                       building,
                       energy_kwh,
                       emission_factor,
                       ROUND(energy_kwh * emission_factor, 3) AS kg_co2e
                FROM readings
                ORDER BY measurement_date DESC, building
            """)
            records = cursor.fetchall()
    for row in records:
        for key in ("energy_kwh", "emission_factor", "kg_co2e"):
            row[key] = float(row[key])
    return jsonify(
        measurements=records,
        total_kwh=round(sum(m["energy_kwh"] for m in records), 2),
        total_kg_co2e=round(sum(m["kg_co2e"] for m in records), 3),
        scope="Demonstration measurements with fictional emission factors",
    )
