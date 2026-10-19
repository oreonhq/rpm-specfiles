%global source0_hash 1c3593d2e6ce53bd84b27d6ac92df4a86d8923afd18b4f4f8e2c979f8a6277df
%global pypi_name gertty
Name:           python-gertty
Version:        1.6.0
Release:        1%{?dist}
Summary:        Gertty is a console-based interface to the Gerrit Code Review system
License:        Apache-2.0 
URL:            https://pypi.python.org/pypi/gertty
Source0:        https://pypi.python.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         fix_setup.cfg.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-gertty
Summary: %summary
Requires: python3-pbr
Requires: python3-urwid
Requires: python3-sqlalchemy
Requires: python3-GitPython
Requires: python3-dateutil
Requires: python3-requests
Requires: python3-alembic
Requires: python3-pyyaml
Requires: python3-voluptuous
Requires: python3-ply
Requires: python3-six
%{?python_provide:%python_provide python3-gertty}
%description -n python3-gertty

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
%patch -P0 -p1 -b .

# Remove egg-info
rm -rf gertty.egg-info

# We handle requirements ourselves, remove requirements.txt
rm -rf requirements.txt

# Fix the wrong-file-end-of-line-encoding warning from rpmlint
sed -i 's/\r$//' LICENSE

%build

%{__python3} setup.py build
%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
%oreon_autofiles python3-gertty usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-gertty -f %{oreon_filedir}/python3-gertty.list

%changelog

%autochangelog
