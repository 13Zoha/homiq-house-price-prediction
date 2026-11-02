const form = document.getElementById("predict-form");
const button = document.getElementById("submit-btn");
const result = document.getElementById("result-content");
const status = document.querySelector(".result-status");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  button.disabled = true;
  button.innerHTML = 'Calculating estimate <span>…</span>';
  status.textContent = "CALCULATING";
  const data = Object.fromEntries(new FormData(form).entries());
  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    });
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.error || "Unable to calculate estimate.");
    result.innerHTML = `
      <div class="result-kicker">YOUR ESTIMATED PROPERTY VALUE</div>
      <div class="placeholder-value">${payload.formatted}</div>
      <p class="result-description">Approximately ₹${payload.price_crore.toFixed(2)} crore. This is an indicative output from the demonstration model.</p>
      <div class="result-divider"></div>
      <div class="result-foot"><span>Model output</span><strong>Random Forest ML</strong></div>`;
    status.textContent = "ESTIMATE GENERATED";
  } catch (error) {
    result.innerHTML = `<div class="result-kicker">PLEASE CHECK YOUR DETAILS</div><p class="result-description">${error.message}</p>`;
    status.textContent = "NEEDS ATTENTION";
  } finally {
    button.disabled = false;
    button.innerHTML = 'Calculate estimated price <span>↗</span>';
  }
});
