%global source0_hash 37a43be5fb5e9544bdacbe6ae30cffc754c6b3066c9bc0fa7d1c4b9b3b6f81cf

Name:           py-spidev
Version:        3.8
Release:        %autorelease
Summary:        A python library for manipulating SPI via spidev
License:        MIT
URL:            https://github.com/doceme/py-spidev/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel

%description
A python module for interfacing with SPI devices from user 
space via the spidev linux kernel driver.

%package -n python3-spidev
Summary:  A python library for manipulating SPI
%{?python_provide:%python_provide python3-spidev}

%description -n python3-spidev
A python module for interfacing with SPI devices from user 
space via the spidev linux kernel driver.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spidev

%files -n python3-spidev -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
