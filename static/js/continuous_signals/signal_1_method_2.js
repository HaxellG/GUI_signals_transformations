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
        
        let url = '/continuous-signals/first-signal/second-method';
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
            })
            .catch(error => console.error('Error:', error));
    });
});