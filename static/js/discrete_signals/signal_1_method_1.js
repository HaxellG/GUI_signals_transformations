document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('signal-form');
    const scaleFactorInput = document.getElementById('scale-factor');
    const timeShiftInput = document.getElementById('time-shift');
    const scaleFactorSelect = document.getElementById('scale-factor-select');
    const timeShiftSelect = document.getElementById('time-shift-select');

    function validateInput(input) {
        const value = input.value;
        if (value === '' || isNaN(value)) {
            input.setCustomValidity('Por favor, ingrese un número válido');
        } else {
            input.setCustomValidity('');
        }
    }

    scaleFactorInput.addEventListener('input', function() {
        validateInput(this);
        scaleFactorSelect.value = '';
    });

    timeShiftInput.addEventListener('input', function() {
        validateInput(this);
        timeShiftSelect.value = '';
    });

    scaleFactorSelect.addEventListener('change', function() {
        scaleFactorInput.value = this.value;
        validateInput(scaleFactorInput);
    });

    timeShiftSelect.addEventListener('change', function() {
        timeShiftInput.value = this.value;
        validateInput(timeShiftInput);
    });
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const scaleFactor = parseFloat(scaleFactorInput.value);
        const timeShift = parseFloat(timeShiftInput.value);
        
        if (isNaN(scaleFactor) || isNaN(timeShift)) {
            alert('Por favor, ingrese valores numéricos válidos');
            return;
        }
        
        let url = '/discrete-signals/first-signal/first-method';
        const params = new URLSearchParams();
        
        params.append('scale_factor', scaleFactor);
        params.append('time_shift', timeShift);
        
        url += '?' + params.toString();
        
        fetch(url, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            Plotly.newPlot('plotly-graph-1', data.data_1, data.layout_1);
            Plotly.newPlot('plotly-graph-2', data.data_2, data.layout_2);
            Plotly.newPlot('plotly-graph-3', data.data_3, data.layout_3);
            Plotly.newPlot('plotly-graph-4', data.data_4, data.layout_4);
            Plotly.newPlot('plotly-graph-5', data.data_5, data.layout_5);
            Plotly.newPlot('plotly-graph-6', data.data_6, data.layout_6);
            Plotly.newPlot('plotly-graph-7', data.data_7, data.layout_7);
            Plotly.newPlot('plotly-graph-8', data.data_8, data.layout_8);
            Plotly.newPlot('plotly-graph-9', data.data_9, data.layout_9);
        })
        .catch(error => console.error('Error:', error));
    });
});