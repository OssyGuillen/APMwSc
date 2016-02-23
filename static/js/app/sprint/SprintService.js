scrumModule.service('sprintService', ['$q', '$http', function($q, $http) {

    this.ACrearSprint = function(fSprint) {
        return  $http({
          url: "sprint/ACrearSprint",
          data: fSprint,
          method: 'POST',
        });
    //    var labels = ["/VSprints", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AElimSprint = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/AElimSprint',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VSprints", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AModifSprint = function(fSprint) {
        return  $http({
          url: "sprint/AModifSprint",
          data: fSprint,
          method: 'POST',
        });
    //    var labels = ["/VSprints", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearSprint = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/VCrearSprint',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VSprint = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/VSprint',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VSprints = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/VSprints',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);