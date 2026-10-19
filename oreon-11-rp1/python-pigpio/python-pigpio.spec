%global source0_hash 91efa50e4990649da97408a384782d6ccf58342fc59cdfe21ed7a42911569975
Name:           python-pigpio
Version:        1.78
Release:        1%{?dist}
Summary:        Raspberry Pi GPIO module
License:        Unlicense
URL:            http://abyz.co.uk/rpi/pigpio/python.html
Source0:        https://files.pythonhosted.org/packages/source/p/pigpio/pigpio-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pigpio = %{version}-%{release}
# /oreon:deps
%description
Raspberry Pi Python module to access the pigpio daemon.

%package -n     python3-pigpio
Summary:        Raspberry Pi GPIO module
%description -n python3-pigpio
Raspberry Pi Python module to access the pigpio daemon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pigpio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pigpio usr/lib/python3*/site-packages/pigpio* usr/lib64/python3*/site-packages/pigpio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pigpio* usr/lib64/python3*/site-packages/pigpio* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-pigpio -f %{oreon_filedir}/python3-pigpio.list

%changelog

%autochangelog
