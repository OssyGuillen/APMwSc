scrumModule.service('equipoService', ['$q', '$http', function($q, $http) {

    this.AActualizarEquipo = function(fEquipo) {
        return  $http({
          url: "equipo/AActualizarEquipo",
          data: fEquipo,
          method: 'POST',
        });
    //    var labels = ["/VEquipo", "/VEquipo", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VEquipo = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'equipo/VEquipo',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);