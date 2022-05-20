# azblob-regex-cli

## download
- run
    - `poetry run azblobregex --st_connect_str ${st_connect_str} --blob_container ${blob_container} --filter_pattern ".*" download`
- dry run
    - `poetry run azblobregex --dry --st_connect_str ${st_connect_str} --blob_container ${blob_container} --filter_pattern ".*" download`
    
## delete
- run
    - `poetry run azblobregex  --st_connect_str ${st_connect_str} --blob_container ${blob_container} --filter_pattern ".*" delete`
- dry run
    - `poetry run azblobregex --dry --st_connect_str ${st_connect_str} --blob_container ${blob_container} --filter_pattern ".*" delete`
