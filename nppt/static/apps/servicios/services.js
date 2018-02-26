new Vue({
  el: 'appServices',
  delimiters: ['{$', '$}'],

  //funcion de cilco de vida
  mounted() {
    var self = this;
    //cargamos lo tipode de cotizacion
    axios.get('/api/servicerecent/list/')
      .then(function (response) {
        self.servicios = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    enviar_armado: function() {
      console.log('--enviar datos para armado--');
    }
  },
  data: {
    servicios:[],
  },
})
