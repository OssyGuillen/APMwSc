scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VCrearPrueba/:idHistoria', {
                controller: 'VCrearPruebaController',
                templateUrl: 'app/pruebas/VCrearPrueba.html'
            }).when('/VPrueba/:idPrueba/:idHistoria', {
                controller: 'VPruebaController',
                templateUrl: 'app/pruebas/VPrueba.html'
            });
});

scrumModule.controller('VCrearPruebaController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'historiasService', 'identService', 'pruebasService',
    function ($scope, $location, $route, flash, $routeParams,  historiasService, identService, pruebasService) {
      $scope.msg = '';
      $scope.fPrueba = {};

      $scope.VHistoria1 = function(idHistoria) {
        $location.path('/VHistoria/'+idHistoria);
      };
      $scope.VLogin2 = function() {
        $location.path('/VLogin');
      };

      $scope.fPruebaSubmitted = false;
      $scope.ACrearPrueba0 = function(isValid) {
        $scope.fPruebaSubmitted = true;
        if (isValid) {          
          pruebasService.ACrearPrueba($scope.fPrueba, $scope.myFile).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

$scope.$watch('fPrueba.categoria', function(newV,oldV) {
  var tabla = $scope.fPrueba_opcionesCategoria;
  if (tabla) {
    for (var i=0; i<tabla.length;i++) {
      if(tabla[i].key==newV) {
        $scope.fPrueba.peso = tabla[i].peso;
        break;
      }
    }
  }
});
    }]);
scrumModule.controller('VPruebaController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'historiasService', 'identService', 'pruebasService', 'equipoService',
    function ($scope, $location, $route, flash, $routeParams, historiasService, identService, pruebasService, equipoService) {
      $scope.msg = '';
      $scope.fPrueba = {};
      $scope.idHistoria = $routeParams.idHistoria;

      pruebasService.VPrueba({"idPrueba":$routeParams.idPrueba, "idHistoria": 7}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        equipoService.VEquipo({"idPila":1}).then(function (object) {
            var miembros = object.data.fEquipo.lista;

            for (var i = 0; i < miembros.length; i++) {
                if (miembros[i].id == $scope.res.fPrueba.asignado){
                    $scope.miembroAsignado = miembros[i].miembro;
                }
            }
        });


        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VHistoria1 = function(idHistoria) {
        $location.path('/VHistoria/'+idHistoria);
      };
      $scope.AElimPrueba2 = function() {
          
        pruebasService.AElimPrueba().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.VLogin3 = function() {
        $location.path('/VLogin');
      };

      $scope.fPruebaSubmitted = false;
      $scope.AModifPrueba0 = function(isValid) {
        $scope.fPruebaSubmitted = true;
        if (isValid) {
          
          pruebasService.AModifPrueba($scope.fPrueba).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

$scope.$watch('fPrueba.categoria', function(newV,oldV) {
  var tabla = $scope.fPrueba_opcionesCategoria;
  if (tabla) {
    for (var i=0; i<tabla.length;i++) {
      if(tabla[i].key==newV) {
        $scope.fPrueba.peso = tabla[i].peso;
        break;
      }
    }
  }
});
    }]);