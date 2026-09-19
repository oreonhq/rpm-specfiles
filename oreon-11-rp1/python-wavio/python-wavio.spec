%global source0_hash 05dd659e2de71d0494588e7bc5fc23c53ffab63cd808e55ecd1e1c1de83e08f3

%global pypi_name wavio

%global pypi_description wavio is simple a Python module that allows to \
read and write WAV files as numpy arrays.

Name: python-%{pypi_name}
Summary: Read and write WAV files as numpy arrays
License: BSD-2-Clause

Version: 0.0.9
Release: 8%{?dist}

URL: https://github.com/WarrenWeckesser/wavio
Source0: %{URL}/archive/v%{version}/%{pypi_name}-v%{version}.tar.gz

# The library always returns data in little-endian format, but the test suite
# expects them in native endianness. This makes the test suite fail on
# big-endian architectures.
#
# Backported from upstream:
# https://github.com/WarrenWeckesser/wavio/commit/2ddae60ef9e83f004482d9ad6ee9ac7c87423ae6
Patch0: 0000-test-endianness.patch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

# For running the tests
BuildRequires: python3-numpy
BuildRequires: python3-pytest

BuildArch: noarch

%description
%{pypi_description}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildArch: noarch

%description -n python3-%{pypi_name}
%{pypi_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Extract license text from comment at top of source
awk 'BEGIN { start_print=0 }
/^-----$/ { start_print=1; next }
/^"""$/ { if ( start_print==1 ) exit }
/.*/ { if (start_print == 1) print $0 }' < wavio.py > LICENSE

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/__pycache__/%{pypi_name}.*

%changelog
%autochangelog
