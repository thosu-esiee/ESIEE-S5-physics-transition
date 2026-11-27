// Supplied application code: students do not modify this file.
const number = (v, digits = 2) => Number(v).toFixed(digits);
async function load() {
  const status = document.getElementById('status');
  try {
    const response = await fetch('/api/measurements');
    if (!response.ok) throw new Error(`API returned HTTP ${response.status}`);
    const data = await response.json();
    document.getElementById('total-kwh').textContent = `${number(data.total_kwh)} kWh`;
    document.getElementById('total-carbon').textContent = `${number(data.total_kg_co2e, 3)} kg CO₂e`;
    document.getElementById('rows').replaceChildren(...data.measurements.map(m => {
      const tr = document.createElement('tr');
      [m.measurement_date, m.building, number(m.energy_kwh),
       number(m.emission_factor, 3), number(m.kg_co2e, 3)].forEach(value => {
        const td = document.createElement('td'); td.textContent = value; tr.append(td);
      });
      return tr;
    }));
    status.textContent = `${data.measurements.length} measurements loaded`;
  } catch (e) { status.textContent = `Unable to load measurements: ${e.message}`; }
}
load();
