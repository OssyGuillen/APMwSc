scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VCrearTarea/:idHistoria', {
                controller: 'VCrearTareaController',
                templateUrl: 'app/tareas/VCrearTarea.html'
            }).when('/VTarea/:idTarea/:idHistoria', {
                controller: 'VTareaController',
                templateUrl: 'app/tareas/VTarea.html'
            });
});

scrumModule.controller('VCrearTareaController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'asignacionTareaService', 'historiasService', 'identService', 'tareasService',
    function ($scope, $location, $route, flash, $routeParams, asignacionTareaService, historiasService, identService, tareasService) {
      $scope.msg = '';
      $scope.fTarea = {};

      tareasService.VCrearTarea({"idHistoria":$routeParams.idHistoria}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VHistoria1 = function(idHistoria) {
        $location.path('/VHistoria/'+idHistoria);
      };
      $scope.VLogin2 = function() {
        $location.path('/VLogin');
      };

      $scope.fTareaSubmitted = false;
      $scope.ACrearTarea0 = function(isValid) {
        $scope.fTareaSubmitted = true;
        if (isValid) {
          
          tareasService.ACrearTarea($scope.fTarea).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

$scope.$watch('fTarea.categoria', function(newV,oldV) {
  var tabla = $scope.fTarea_opcionesCategoria;
  if (tabla) {
    for (var i=0; i<tabla.length;i++) {
      if(tabla[i].key==newV) {
        $scope.fTarea.peso = tabla[i].peso;
        break;
      }
    }
  }
});
    }]);
scrumModule.controller('VTareaController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'asignacionTareaService', 'historiasService', 'identService', 'tareasService', 'equipoService',
    function ($scope, $location, $route, flash, $routeParams, asignacionTareaService, historiasService, identService, tareasService, equipoService) {
      $scope.msg = '';
      $scope.fTarea = {};
      $scope.idHistoria = $routeParams.idHistoria;

      tareasService.VTarea({"idTarea":$routeParams.idTarea, "idHistoria": 7}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        equipoService.VEquipo({"idPila":1}).then(function (object) {
            var miembros = object.data.fEquipo.lista;

            for (var i = 0; i < miembros.length; i++) {
                if (miembros[i].id == $scope.res.fTarea.asignado){
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
      $scope.AElimTarea2 = function() {
          
        tareasService.AElimTarea().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.VLogin3 = function() {
        $location.path('/VLogin');
      };
      $scope.VAsignacionTarea4 = function(idTarea, idHistoria) {
        $location.path('/VAsignacionTarea/'+idTarea+'/'+idHistoria);
      };

      $scope.fTareaSubmitted = false;
      $scope.AModifTarea0 = function(isValid) {
        $scope.fTareaSubmitted = true;
        if (isValid) {
          
          tareasService.AModifTarea($scope.fTarea).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

$scope.$watch('fTarea.categoria', function(newV,oldV) {
  var tabla = $scope.fTarea_opcionesCategoria;
  if (tabla) {
    for (var i=0; i<tabla.length;i++) {
      if(tabla[i].key==newV) {
        $scope.fTarea.peso = tabla[i].peso;
        break;
      }
    }
  }
});
    }]);