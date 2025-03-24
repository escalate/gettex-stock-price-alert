[![Test](https://github.com/escalate/gettex-stock-price-alert/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/gettex-stock-price-alert/actions/workflows/test.yml)

# Gettex stock price alert

Price alerts for Gettex stock exchange

## Local usage

Usage is possible via an interactive Docker container in VSCode.

1. Build and launch the DevContainer in VSCode.

2. Initiate the Python Virtual Environment via `poetry env activate` in the terminal.

3. Run `./src/cli.py --help`

```
Usage: cli.py [OPTIONS]

  HTTP Call CLI

Options:
  --url TEXT  URL, e.g. https://example.com  [required]
  --help      Show this message and exit.
```

## License

MIT
