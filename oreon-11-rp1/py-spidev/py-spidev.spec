%global source0_hash 37a43be5fb5e9544bdacbe6ae30cffc754c6b3066c9bc0fa7d1c4b9b3b6f81cf
Name:           py-spidev
Version:        3.8
Release:        1%{?dist}
Summary:        A python library for manipulating SPI via spidev
License:        MIT
URL:            https://github.com/doceme/py-spidev/
Source0:        https://github.com/doceme/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-py-spidev = %{version}-%{release}
# /oreon:deps
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
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-spidev usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n python3-spidev -f %{oreon_filedir}/python3-spidev.list

%changelog

%autochangelog
