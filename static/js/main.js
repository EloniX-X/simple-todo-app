document.addEventListener("DOMContentLoaded", function() {
    let allcatsDropdown = document.querySelector("select[name='allcats']");
    let subcatsDropdown = document.querySelector("select[name='subcats']");

    function updateSubcats(selectedValue) {
        fetch("/get_subcats", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'selected_cat': selectedValue })
        })
        .then(response => response.json())
        .then(data => {
            subcatsDropdown.innerHTML = "";  // Clear previous options
            data.subcats.forEach(subcat => {
                let option = document.createElement("option");
                option.value = subcat;
                option.textContent = subcat;
                subcatsDropdown.appendChild(option);
            });
        });
    }

    allcatsDropdown.addEventListener("change", function() {
        updateSubcats(this.value);
    });

    // Initial population of subcats based on default allcats selection
    updateSubcats(allcatsDropdown.value);
});
