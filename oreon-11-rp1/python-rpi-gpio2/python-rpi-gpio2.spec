%global source0_hash fe2f7ff0ce98a814b885be973be7976fe84e27fe15f69e7ef799e9ac4d8a5b06

Summary: A libgpiod compatibility layer for the RPi.GPIO API
Name: python-rpi-gpio2
Version: 0.4.0
Release: 14%{?dist}

License: GPL-3.0-or-later
URL: https://github.com/underground-software/RPi.GPIO2
Source0: %{url}/archive/v%{version}/RPi.GPIO2-%{version}.tar.gz

BuildArch: noarch
%global _description %{expand:
This library implements a compatibility layer between RPi.GPIO syntax and
libgpiod semantics, allowing a fedora user on the Raspberry Pi platform to
use the popular RPi.GPIO API, the original implementation of which depends
on features provided by a non-mainline kernel.}

%description %_description

%package -n python3-rpi-gpio2
Summary: %{summary}

Obsoletes: python3-RPi.GPIO < 0.7.0-7
Provides: python3-RPi.GPIO = 1:%{version}-%{release}

BuildRequires: python3-devel
BuildRequires: python3-setuptools

# This explicit dependency on the libgpiod python bindings subpackage
# is neccessary because it is unsatisfiable via PyPi
Requires: python3-libgpiod >= 1.5

%description -n python3-rpi-gpio2  %_description

%package doc
Summary: Examples for python-rpi-gpio2

%description doc %{_description}
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

%check
%py3_check_import RPi

# The tests rely on the presence of the actual physical GPIO pins on the system for now and though we may develop emulation functionality to run the tests on any system in the future we think the software is ready to be packaged as-is and we will just update it when the better tests are done

%files -n python3-rpi-gpio2
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/RPi/
%{python3_sitelib}/RPi.GPIO2-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE.txt
%doc examples

%changelog
%autochangelog
