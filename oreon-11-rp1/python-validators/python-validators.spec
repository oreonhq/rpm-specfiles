%global source0_hash 992d6c48a4e77c81f1b4daba10d16c3a9bb0dbb79b3a19ea847ff0928e70497a

%global pypi_name validators

Name:           python-%{pypi_name}
Version:        0.35.0
Release:        5%{?dist}
Summary:        Data validation in Python for humans

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/kvesteri/validators
Source0:        %pypi_source
BuildArch:      noarch

%description
Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or
a schema.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or
a schema.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files validators

%check
pytest-%{python3_version} --ignore "tests/crypto_addresses/test_eth_address.py"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.md README.md
%license LICENSE.txt

%changelog
%autochangelog
