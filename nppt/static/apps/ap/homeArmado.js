new Vue({
  el: 'appHomeArmado',
  delimiters: ['{$', '$}'],

  //funcion de cilco de vida
  mounted() {
    var self = this;
    //cargamos la lista de destinos
    axios.get('/api/servicio/destino/list/')
      .then(function (response) {
        self.destinos = response.data;
      })
      .catch(function (error) {
        console.log(error);
      }
    );
    //cargamos paices del mundo
    axios.get('https://restcountries.eu/rest/v2/all')
      .then(function (response) {
        self.paises = response.data;
      })
      .catch(function (error) {
        console.log(error);
      }
    );
  },
  methods: {
    add_destinos_seleccionados: function(d) {
      var self = this;
      console.log('--destinos seleccionados--');
      self.destinos_seleccionados.push(d);
      self.destinos_seleccionados.unique()
    }
  },
  data: {
    destinos: [],
    destinos_seleccionados: [],
    apDestinos: null,
    paises: null,
    apPais: [],
  },
})
