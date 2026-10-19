%global source0_hash 9c8485c8900af294b7287fd5fb061c0cc34827ef13e26d5728ae6a24afe56d4b
Name:           python-mpd2
Version:        3.1.1
Release:        1%{?dist}
Summary:        Python library providing a client interface for MPD
License:        LGPL-3.0-or-later
URL:            https://github.com/Mic92/python-mpd2
Source0:        https://github.com/Mic92/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mpd2 = %{version}-%{release}
# /oreon:deps
%description
Python library providing a client interface for MPD.

%package -n python3-mpd2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Summary:        Python 3 mpd2 module
%description -n python3-mpd2
Python3 library providing a client interface for MPD.

%package doc
Summary:    Examples for %{name}
%description doc
This package contains examples for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
echo "whitelist_externals = coverage" >> tox.ini

# Remove unecessary shebang
sed -i '/^#!\/usr\/bin\/env.*python$/ d' mpd/tests.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mpd2 usr/lib/python3*/site-packages/mpd2* usr/lib64/python3*/site-packages/mpd2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mpd2* usr/lib64/python3*/site-packages/mpd2* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{tox}
%files
%files -n python3-mpd2 -f %{oreon_filedir}/python3-mpd2.list
%files -n python-mpd2-doc -f %{oreon_filedir}/python-mpd2-doc.list

%changelog

%autochangelog
