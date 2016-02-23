scrumModule.service('anexoService', ['$q', '$http', function($q, $http) {

    this.AAnexo = function(fAnexo) {
        return  $http({
          url: "anexo/AAnexo",
          data: fAnexo,
          method: 'POST',
          headers: { 'Content-Type': 'multipart/form-data' },
          transformRequest: function (data, headersGetter) {
                var formData = new FormData();
                angular.forEach(data, function (value, key) {
                    formData.append(key, value);
                });

                var headers = headersGetter();
                delete headers['Content-Type'];

                return formData;
          }    });
    //    var labels = ["/VAnexo", "/VAnexo", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AElimAnexo = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'anexo/AElimAnexo',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VAnexo", "/VAnexo", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VAnexo = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'anexo/VAnexo',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);