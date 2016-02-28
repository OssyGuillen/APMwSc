scrumModule.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/VAnexo/:idPila', {
                controller: 'VAnexoController',
                templateUrl: 'app/anexo/VAnexo.html'
            });
}]);

scrumModule.controller('VAnexoController', 
   ['$window', '$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'ngTableParams', 'anexoService', 'prodService',
    function ($window, $scope, $location, $route, $timeout, flash, $routeParams, ngTableParams, anexoService, prodService) {
      $scope.msg = '';
      $scope.fAnexo = {};

      anexoService.VAnexo({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }


      var AElimAnexo1Data = $scope.res.data1;
      if(typeof AElimAnexo1Data === 'undefined') AElimAnexo1Data=[];
      $scope.tableParams1 = new ngTableParams({
          page: 1,            // show first page
          count: 10           // count per page
      }, {
          total: AElimAnexo1Data.length, // length of data
          getData: function($defer, params) {
              $defer.resolve(AElimAnexo1Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
          }
      });            


      });
      $scope.VProducto3 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };

      $scope.fAnexoSubmitted = false;
      $scope.AAnexo2 = function(isValid) {
        $scope.fAnexoSubmitted = true;
        if (isValid) {
          anexoService.AAnexo($scope.fAnexo, $scope.myFile, $routeParams.idPila).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();              
          });
        }
      };

      $scope.AElimAnexo1 = function(id, idBacklog) {
          var tableFields = [["idAnexo","id"], ['nombre','Nombre']];
          var arg = {};
          arg[tableFields[0][1]] = ((typeof id === 'object')?JSON.stringify(id):id);
          anexoService.AElimAnexo(arg).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label+'/'+idBacklog);
              $route.reload();
          });
      };

      $scope.downloadFile = function (url) {
        $window.location = '/anexo/ADescargar/' + url;
      };

    }]);
