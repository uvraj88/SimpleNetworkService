# SimpleNetworkService
Simple Network Service which resolves lat and long to a address.

# Start server
* Goto inside src folder and run __main__.py file
* Sample Eg: python __main__.py

# Run Tests
Goto inside tst folder and run 'pytest' command.

# Code structure

1. 'src' folder contains source files.
* Main and init files. Server is defined in main file.
* 'config.json' file which contains key for different service providers
* sns_api file which implements the main API and integrates multiple network
providers present in services folder. Retry logic is implemented
..* Retry logic:
  ..1. Try fetching resolved address using HERE API
  ..2. If failed (either network error or api error), try fetching using GOOGLE api.
  ..3. If failed, will return Failure.

* helper file which implements http url encoding and decoding.
* model file which implements the interface to get resolved address based on api used.
2. src/services folder
* bing_api file which implements the bing api provider specific implementation.
* google_api file which implements the google api provider specific implementation.
* here_api file which implements the here api provider specific implementation.
3. src/controllers folder
* ping_controller file which contains rest ping endpoint implementation.
* resolve_Controller file which contains rest endpoint for resolving lat and long.
This calls Sns_api file api method.
4. src/swagger folder
* swagger.yaml file which defines rest endpoint configuration.

5.'tst' folder contains test files.
* results folder in tst gives mock json object for google and here rest responses.
