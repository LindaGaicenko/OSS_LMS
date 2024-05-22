// Styles
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";
import { md3 } from "vuetify/blueprints";
import { VDateInput } from "vuetify/labs/VDateInput";

// Composables
import { createVuetify } from "vuetify";

export default createVuetify({
  blueprint: md3,
  components: {
    VDateInput,
  },
});
