%global source0_hash b9eb976a4a6d9ef47751d9d558b41f6dd717f97ee266db6fb17c8721ab6bb109

%global pypi_name pyspiflash

Name:           python-%{pypi_name}
Version:        0.6.5
Release:        5%{?dist}
Summary:        Python SPI data flash device drivers

License:        MIT
URL:            https://github.com/eblot/pyspiflash
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
SPI flash devices, also known as DataFlash are commonly found in embedded
products, to store firmware, microcode or configuration parameters.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
SPI flash devices, also known as DataFlash are commonly found in embedded
products, to store firmware, microcode or configuration parameters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l spiflash

# Not running tests as they try to create a device
#%check
#PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} i2cflash/tests/serialeeprom.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst spiflash/AUTHORS
%license LICENSE

%changelog
%autochangelog
