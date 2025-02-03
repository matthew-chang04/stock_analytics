document.addEventListener("DOMContentLoaded", function() {
    fetch("/stock_data/")
        .then(response => response.json())
        .then(data => {
            let tickers = data.map(d => d.ticker);
            let changes = data.map(d => d.change);

            let zValues = [];
            let xLabels = [];
            let yLabels = [];

            let gridSize = Math.ceil(Math.sqrt(tickers.length));
            for (let i = 0; i < gridSize; i++) {
                let row = [];
                for (let j = 0; j < gridSize; j++) {
                    let index = i * gridSize + j;
                    if (index < changes.length) {
                        row.push(changes[index]);
                        xLabels.push(tickers[index]);
                    } else {
                        row.push(null);
                    }
                }
                yLabels.push(i);
                zValues.push(row);
            }

            let trace = {
                z: zValues,
                x: xLabels,
                y: yLabels,
                type: 'heatmap',
                colorscale: 'RdYlGn',
                reversescale: true
            };

            let layout = { title: "S&P 500 Heatmap", xaxis: { title: "Ticker" }, yaxis: { title: "Grid Row" } };
            Plotly.newPlot("heatmap", [trace], layout);
        });
});