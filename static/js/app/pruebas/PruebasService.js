scrumModule.service('pruebasService', ['$q', '$http', function($q, $http) {

    this.ACrearPrueba = function(fPrueba, myFile) {
        return  $http({
          url: "pruebaAceptacion/ACrearPruebaAceptacion",
          data: fPrueba,
          method: 'POST',
          headers: { 'Content-Type': 'multipart/form-data' },
          transformRequest: function (data, headersGetter) {
                var formData = new FormData();
                formData.append('contenido',myFile);
                angular.forEach(data, function (value, key) {
                    formData.append(key, value);
                });

                var headers = headersGetter();
                delete headers['Content-Type'];

                return formData;
          }          
        });
    //    var labels = ["/VHistoria", "/VCrearPrueba", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearPrueba = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'pruebaAceptacion/VCrearPruebaAceptacion',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AElimPrueba = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'pruebaAceptacion/AElimPruebaAceptacion',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VHistoria", "/VPrueba", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
}]);