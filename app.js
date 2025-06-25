var app=angular.module("app1",["ngRoute"])
app.config(function($routeProvider)
{
	$routeProvider
	.when("/studenthome.html",
	{
		templateUrl:"studenthome.html",
		controller:"c1"
	})
	.when("/studentabout.html",
	{
		templateUrl:"studentabout.html",
		controller:"c2"
	})
	.when("/studentlist.html",
	{
		templateUrl:"studentlist.html",
		controller:"c3"
	})
	.otherwise(
	{
		redirectTo:"/studenthome.html"
	});
})
app.controller("c1",function($scope)
	{
		$scope.display="Welcome Shrimathi Devkunvar Nanalal Bhatt Vaishnav College for Women (Autonomous)"
	})
app.controller("c2",function($scope)
	{
		$scope.display="About us"
	})
app.controller("c3",function($scope)
	{
		$scope.display="Artificial intelligence students"
	})

		