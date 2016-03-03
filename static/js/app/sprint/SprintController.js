scrumModule.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/VCrearReunionSprint/:idSprint', {
                controller: 'VCrearReunionSprintController',
                templateUrl: 'app/sprint/VCrearReunionSprint.html'
            }).when('/VCrearSprint/:idPila', {
                controller: 'VCrearSprintController',
                templateUrl: 'app/sprint/VCrearSprint.html'
            }).when('/VReunion/:idReunion', {
                controller: 'VReunionController',
                templateUrl: 'app/sprint/VReunion.html'
            }).when('/VSprint/:idPila', {
                controller: 'VSprintController',
                templateUrl: 'app/sprint/VSprint.html'
            }).when('/VSprints/:idPila', {
                controller: 'VSprintsController',
                templateUrl: 'app/sprint/VSprints.html'
            });
}]);

scrumModule.controller('VCrearReunionSprintController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'prodService', 'sprintService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, prodService, sprintService) {
      $scope.msg = '';
      $scope.fReunion = {};

      sprintService.VCrearReunionSprint({"idSprint":$routeParams.idSprint}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }

        if ($scope.fReunion.Fecha) {
          $scope.fReunion.Fecha=new Date($scope.fReunion.Fecha);
        }

      });
      $scope.VSprint0 = function(idPila) {
        $location.path('/VSprint/'+idPila);
      };

      $scope.fReunionSubmitted = false;
      $scope.ACrearReunionSprint1 = function(isValid) {
        $scope.fReunionSubmitted = true;
        if (isValid) {
          
          sprintService.ACrearReunionSprint($scope.fReunion).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);

scrumModule.controller('VCrearSprintController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'prodService', 'sprintService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, prodService, sprintService) {
      $scope.msg = '';
      $scope.fSprint = {};

      sprintService.VCrearSprint({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }


      });
      $scope.VSprints1 = function(idPila) {
        $location.path('/VSprints/'+idPila);
      };

      $scope.fSprintSubmitted = false;
      $scope.ACrearSprint0 = function(isValid) {
        $scope.fSprintSubmitted = true;
        if (isValid) {
          
          sprintService.ACrearSprint($scope.fSprint).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);

scrumModule.controller('VReunionController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'prodService', 'sprintService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, prodService, sprintService) {
      $scope.msg = '';
      $scope.fReunion = {};

      sprintService.VReunion({"idReunion":$routeParams.idReunion}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }

        if ($scope.fReunion.Fecha) {
          $scope.fReunion.Fecha=new Date($scope.fReunion.Fecha);
        }

      });
      $scope.VSprint0 = function(idPila) {
        $location.path('/VSprint/'+idPila);
      };

      $scope.fReunionSubmitted = false;
      $scope.AModifReunionSprint1 = function(isValid) {
        $scope.fReunionSubmitted = true;
        if (isValid) {
          
          sprintService.AModifReunionSprint($scope.fReunion).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);

scrumModule.controller('VSprintController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'prodService', 'sprintService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, prodService, sprintService) {
      $scope.msg = '';
      $scope.fSprint = {};

      sprintService.VSprint({"idSprint":$routeParams.idSprint}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }


              var VReunion4Data = $scope.res.data4;
              if(typeof VReunion4Data === 'undefined') VReunion4Data=[];
              $scope.tableParams4 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VReunion4Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VReunion4Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });


      });
      $scope.VCrearReunionSprint1 = function(idSprint) {
        $location.path('/VCrearReunionSprint/'+idSprint);
      };
      $scope.VSprints1 = function(idPila) {
        $location.path('/VSprints/'+idPila);
      };

      $scope.VSprints2 = function(idPila) {
        $location.path('/VSprints/'+idPila);
      };

      $scope.fSprintSubmitted = false;
      $scope.AModifSprint0 = function(isValid) {
        $scope.fSprintSubmitted = true;
        if (isValid) {
          
          sprintService.AModifSprint($scope.fSprint).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

      $scope.VReunion4 = function(idReunion) {
        $location.path('/VReunion/'+((typeof idReunion === 'object')?JSON.stringify(idReunion):idReunion));
      };

    }]);
scrumModule.controller('VSprintsController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'ngTableParams', 'prodService', 'sprintService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, ngTableParams, prodService, sprintService) {
      $scope.msg = '';
      sprintService.VSprints({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }


              var VSprint1Data = $scope.res.data1;
              if(typeof VSprint1Data === 'undefined') VSprint1Data=[];
              $scope.tableParams1 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VSprint1Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VSprint1Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });            


      });
      $scope.VProducto0 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };
      $scope.VCrearSprint2 = function(idPila) {
        $location.path('/VCrearSprint/'+idPila);
      };

      $scope.VSprint1 = function(idSprint) {
        $location.path('/VSprint/'+((typeof idSprint === 'object')?JSON.stringify(idSprint):idSprint));
      };

    }]);
