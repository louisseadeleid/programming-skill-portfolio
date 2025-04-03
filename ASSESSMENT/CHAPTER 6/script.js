function calculateTotal() {
    // Get input values
    let pricePerLiter = parseFloat(document.getElementById('pricePerLiter').value);
    let liters = parseFloat(document.getElementById('liters').value);
    
    // Calculate total cost
    let total = pricePerLiter * liters;
    
    // Display result in AED
    document.getElementById('totalCost').textContent = `Total Cost: AED ${total.toFixed(2)}`;
}
