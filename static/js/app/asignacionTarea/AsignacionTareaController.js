scrumModule.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/VAsignacionTarea/:idTarea', {
                controller: 'VAsignacionTareaController',
                templateUrl: 'app/asignacionTarea/VAsignacionTarea.html'
            });
}]);

scrumModule.controller('VAsignacionTareaController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'asignacionTareaService', 'tareasService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, asignacionTareaService, tareasService) {
      $scope.msg = '';
      $scope.fAsignacionTarea = {};
      console.log($scope.idTarea);

      asignacionTareaService.VAsignacionTarea({"idTarea":$routeParams.idTarea}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }

        //  temporal rewriting of variable while harcoding on /pp/scrum/asignacionTarea.py is removed
        $scope.idTarea = $routeParams.idTarea;

        $scope.agrMiembro = function () {
          $scope.fAsignacionTarea.lista.push({miembro:null});
        };
        $scope.elimMiembro = function (index) {
          $scope.fAsignacionTarea.lista.splice(index, 1);
        };

      });

      $scope.VTarea1 = function(idTarea) {
        $location.path('/VTarea/'+idTarea);
      };

      $scope.fAsignacionTareaSubmitted = false;
      $scope.AActuralizarAsignacionTarea0 = function(isValid) {
        $scope.fAsignacionTareaSubmitted = true;
        if (isValid) {
          
          asignacionTareaService.AActuralizarAsignacionTarea($scope.fAsignacionTarea).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
