from coche import Coche

cochecito = Coche("4629MVC",60,7.1,200)
#cochecito.arrancarMotor()

#cochecito.repostarCombustile(-9)
cochecito.repostarCombustile(15)
cochecito.arrancarMotor() 
cochecito.fijarVelocidad(80) 
cochecito.recorrerDistancia(100)
cochecito.fijarVelocidad(120) 
cochecito.recorrerDistancia(300)