%global source0_hash 8eb9e214b3a87b3ec7cce6a9401ea566277607d1f3102c884639387384fedaee

Name:           python-nitime
Version:        0.11
Release:        %autorelease
Summary:        Timeseries analysis for neuroscience data

%global forgeurl https://github.com/nipy/nitime
%global tag %{version}
%forgemeta

License:        BSD-3-Clause
URL:            http://nipy.org/nitime
Source:         %forgesource

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Nitime is library of tools and algorithms for the analysis of time-series data
from neuroscience experiments. It contains a implementation of numerical
algorithms for time-series analysis both in the time and spectral domains, a
set of container objects to represent time-series, and auxiliary objects that
expose a high level interface to the numerical machinery and make common
analysis tasks easy to express with compact and semantically clear code.

Current information can always be found at the nitime website. Questions and
comments can be directed to the mailing list:
http://mail.scipy.org/mailman/listinfo/nipy-devel.

Documentation is available at http://nipy.org/nitime/documentation.html
}

%description %_description

%package -n python3-nitime
Summary:        %{summary}

%description -n python3-nitime %_description

%pyproject_extras_subpkg -n python3-nitime full

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# Correct shebangs to python3
sed -i 's|^#!/usr/bin/env python|#!/usr/bin/python3|' setup.py

# This example doesn't seem to be correct, so we remove it for the time being and let upstream know.
rm -fv doc/examples/filtering_fmri.py

pushd tools
    for f in *; do
        sed -E -i 's|^#!/usr/bin/env python|#!/usr/bin/python3|' "$f"
    done
popd

# Remove duplicate license file from module
rm -v nitime/LICENSE

# Allow building with NumPy 1.x. F40 and F41 will stay on 1.x.
sed -r -i 's/numpy>=2.*,</numpy</' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x full

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l nitime

%check
%pytest -v --import-mode=importlib

%files -n python3-nitime -f %{pyproject_files}
%doc README.txt THANKS

%changelog
%autochangelog
