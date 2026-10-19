%global source0_hash cacecf0baa674d356641f1d406b8bff1d756d739c46b869a54de515d08e6fc9c
Name:           python-tempita
Version:        0.6.0
Release:        1%{?dist}
Summary:        A very small text templating language
License:        MIT
URL:            http://pythonpaste.org/tempita/
Source0:        https://pypi.python.org/packages/source/T/Tempita/Tempita-%{version}.tar.gz
Patch0001:      0001-Apply-fixes-required-for-Python-3.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-tempita
Summary:        A very small text templating language
%{?python_provide:%python_provide python3-tempita}
%description -n python3-tempita
Tempita is a small templating language for text substitution.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Tempita-%{version} -p1
# Since Setuptools 58+ upstream removed support for 2to3
sed -i '/use_2to3/d' setup.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-tempita usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-tempita -f %{oreon_filedir}/python3-tempita.list

%changelog

%autochangelog
