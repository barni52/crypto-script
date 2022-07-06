package main

import (
	"fmt"
	"net/http"
)

var BTCPrice, XMRPrice, ETHPrice float32

func main() {
	fmt.Println("hello World")
	getCryptoRates()
}

func getCryptoRates() {
	resp, err := http.Get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=1,328,1027")
	if err != nil {
		fmt.Println(resp)
	}
	fmt.Println(err)
}
