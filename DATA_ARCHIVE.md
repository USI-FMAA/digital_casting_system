# Data Archive

The sample data has been moved out of the main package to reduce package size from 95MB+ to ~65KB.

## Getting the Sample Data

The sample data is available as a separate archive that can be downloaded from the releases page.

### Manual Download

Download `dcs-sample-data-{version}.tar.gz` from the [releases page](https://github.com/USI-FMAA/digital_casting_system/releases) and extract it to your project directory:

```bash
tar -xzf dcs-sample-data-0.1.5.tar.gz
mv dcs-sample-data data
```

### Using Python

```python
import tarfile
import urllib.request

# Download and extract sample data
url = "https://github.com/USI-FMAA/digital_casting_system/releases/download/v0.1.5/dcs-sample-data-0.1.5.tar.gz"
urllib.request.urlretrieve(url, "dcs-sample-data.tar.gz")

with tarfile.open("dcs-sample-data.tar.gz", "r:gz") as tar:
    tar.extractall()
    
# Rename to expected directory name
import os
os.rename("dcs-sample-data", "data")
```

## What's in the Archive

The data archive contains:
- CSV files with experimental data (csv/)
- JSON configuration files (json/)
- Plot/visualization files (plot/)
- Documentation on file naming conventions

## Impact on Code

The data processing classes (`DataGathering` and `DataProcessing`) will automatically create the necessary directories when instantiated, so existing code will continue to work without modification.