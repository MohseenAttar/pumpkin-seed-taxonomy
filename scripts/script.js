document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('pumpkin-form');
    const inputs = form.querySelectorAll('input[type="number"]');
    const formError = document.getElementById('form-error');
  
    const validateInput = (input) => {
      const value = input.value.trim();
      if (value === '' || isNaN(value) || Number(value) < 0) {
        input.classList.add('invalid');
        return false;
      } else {
        input.classList.remove('invalid');
        return true;
      }
    };
  
    const validateForm = () => {
      let isValid = true;
      inputs.forEach(input => {
        if (!validateInput(input)) {
          isValid = false;
        }
      });
      return isValid;
    };
  
    inputs.forEach(input => {
      input.addEventListener('blur', () => validateInput(input));
    });
  
    form.addEventListener('submit', (e) => {
      if (!validateForm()) {
        e.preventDefault();
        formError.textContent = 'Please fix the highlighted fields.';
      } else {
        formError.textContent = '';
      }
    });
  });
  