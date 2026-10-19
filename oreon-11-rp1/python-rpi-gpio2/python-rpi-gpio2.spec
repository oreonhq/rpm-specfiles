%global source0_hash fe2f7ff0ce98a814b885be973be7976fe84e27fe15f69e7ef799e9ac4d8a5b06
Summary:        A libgpiod compatibility layer for the RPi.GPIO API
Name: python-rpi-gpio2
Version: 0.4.0
Release:        14%{?dist}
License: GPL-3.0-or-later
URL: https://github.com/underground-software/RPi.GPIO2
Source0:        https://github.com/underground-software/RPi.GPIO2/archive/v%{version}/RPi.GPIO2-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-rpi-gpio2
Summary:        A libgpiod compatibility layer for the RPi.GPIO API
Obsoletes: python3-RPi.GPIO < 0.7.0-7
Provides: python3-RPi.GPIO = 1:%{version}-%{release}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: python3-libgpiod >= 1.5
%description -n python3-rpi-gpio2

%package doc
Summary: Examples for python-rpi-gpio2
%description doc
A set of examples for python-rpi-gpio2

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n RPi.GPIO2-%{version}

# Make sure scripts in the examples directory aren't executable
chmod 0644 examples/*

%build

%py3_build
%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/tests
rm -rf %{buildroot}%{python3_sitelib}/examples
%oreon_autofiles python3-rpi-gpio2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%py3_check_import RPi
%files -f %{oreon_filedir}/main.list
%files -n python3-rpi-gpio2 -f %{oreon_filedir}/python3-rpi-gpio2.list
%files -n python-rpi-gpio2-doc -f %{oreon_filedir}/python-rpi-gpio2-doc.list

%changelog

%autochangelog
