// app.js

document.addEventListener('DOMContentLoaded', () => {
    loadInventory();

    // Function to fetch and display inventory
    function loadInventory() {
        fetch('/api/equipment')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.querySelector('#inventory-table tbody');
                tableBody.innerHTML = '';  // Clear existing rows

                data.forEach(item => {
                    const row = document.createElement('tr');

                    row.innerHTML = `
                        <td>${item.name}</td>
                        <td>${item.description || '-'}</td>
                        <td>${item.status}</td>
                        <td>
                            ${item.status === 'available' 
                                ? `<button class="btn btn-success btn-sm btn-borrow" onclick="borrowItem(${item.id})">Borrow</button>`
                                : `<button class="btn btn-secondary btn-sm btn-return" onclick="returnItem(${item.id})">Return</button>`
                            }
                        </td>
                    `;

                    tableBody.appendChild(row);
                });
            })
            .catch(error => console.error('Error loading inventory:', error));
    }

    // Function to borrow an item
    window.borrowItem = function(itemId) {
        const borrowerName = prompt("Please enter your name:");
        if (borrowerName) {
            fetch(`/api/equipment/${itemId}/borrow`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ borrower: borrowerName })
            })
            .then(response => {
                if (response.ok) {
                    loadInventory();  // Refresh the inventory table
                } else {
                    alert("Error: Could not borrow item.");
                }
            });
        }
    };

    // Function to return an item
    window.returnItem = function(itemId) {
        fetch(`/api/equipment/${itemId}/return`, { method: 'POST' })
            .then(response => {
                if (response.ok) {
                    loadInventory();  // Refresh the inventory table
                } else {
                    alert("Error: Could not return item.");
                }
            });
    };
});