%global source0_hash 6ecd15511a250df4c95626cdf713aed92eaa000872cc96b453e07538b109471a
%global realname grabserial
Name: python-grabserial
Version: 2.1.8
Release:        1%{?dist}
Summary:        Reads a serial port and writes data to standard output
License: GPL-2.0-only
URL: http://elinux.org/Grabserial
Source0:        https://github.com/tbird20d/grabserial/archive/v%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-grabserial
Summary: %summary
Requires: python3-pyserial
%{?python_provide:%python_provide python3-grabserial}
%description -n python3-grabserial

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{realname}-%{version}

%build

%{__python3} setup.py build
%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
%oreon_autofiles python3-grabserial usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-grabserial -f %{oreon_filedir}/python3-grabserial.list

%changelog

%autochangelog
