%global source0_hash 0888a6caebd88f7ddbebc606e9a87b10077febf8e30d53e4628e6e325423173b
Summary:        The gerrit client tools
Name:          gerrymander
Version:       1.5
Release:        39%{?dist}
Source0:        https://pypi.python.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
URL:           https://pypi.python.org/pypi/gerrymander
License:       Apache-2.0
BuildArch:     noarch
Requires:      python3-gerrymander
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%package -n python3-gerrymander
Summary: The gerrit python3 client
License: GPL-2.0-or-later
%{?python_provide:%python_provide python3-gerrymander}
%description
The gerrymander package provides a set of command line tools
for interacting with Gerrit

%description -n python3-gerrymander
The python3-gerrymander package provides a set of python3
modules for interacting with Gerrit.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

# Remove any egg info (as of submitting this review, there's no bundled
# egg info)
rm -rf *.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-gerrymander usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-gerrymander -f %{oreon_filedir}/python3-gerrymander.list

%changelog

%autochangelog
