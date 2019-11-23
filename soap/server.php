<?php

$options = array(
    'uri' => 'http://localhost:8888/calc'
);
$server = new SoapServer(null, $options);

class Calculadora
{
    public function somar($valor1, $valor2)
    {
        return $valor1 + $valor2;
    }

    public function subtrair($valor1, $valor2)
    {
        return $valor1 - $valor2;
    }

    public function dividir($valor1, $valor2)
    {
        return $valor1 / $valor2;
    }

    public function multiplicar($valor1, $valor2)
    {
        return $valor1 * $valor2;
    }
}

$server->setObject(new Calculadora());

$server->handle();