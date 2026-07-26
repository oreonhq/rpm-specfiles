%global source0_hash e10d1b49655800bffe0fbb5eb31eeef915a4421952ef006d468d53d34901f6f8

Name:           python-xlib
Version:        0.33
Release:        16%{?dist}
Summary:        X client library for Python

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/python-xlib/python-xlib
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        xorg.conf
# Use unittest.mock in py3.8+
Patch0:         python-xlib-mock.patch
# tests need to import tohex
# https://github.com/python-xlib/python-xlib/pull/75
Patch1:         python-xlib-tohex.patch
Patch2:         fix-ssh-tunnel-auth
# Remove failing test
# https://github.com/python-xlib/python-xlib/issues/1
Patch4:         python-xlib-test.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  texinfo-tex
BuildRequires:  tex(dvips)
# For tests
BuildRequires:  xorg-x11-drv-dummy

%description
The Python X Library is a complete X11R6 client-side implementation,
written in pure Python. It can be used to write low-levelish X Windows
client applications in Python.

%package -n python%{python3_pkgversion}-xlib
Summary:        X client library for Python 3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-six >= 1.10.0
BuildRequires:  python%{python3_pkgversion}-tkinter
BuildRequires:  python%{python3_pkgversion}-pytest
Requires:       python%{python3_pkgversion}-six >= 1.10.0
Suggests:       python%{python3_pkgversion}-tkinter
%{?python_provide:%python_provide python%{python3_pkgversion}-xlib}

%description -n python%{python3_pkgversion}-xlib
The Python X Library is a complete X11R6 client-side implementation,
written in pure Python. It can be used to write low-levelish X Windows
client applications in Python 3.

%package doc
Summary:        Documentation and examples for python-xlib
BuildRequires:  texi2html

%description doc
Install this package if you want the developers' documentation and examples
that tell you how to program with python-xlib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%py3_build
cd doc
make html ps
cd html
rm Makefile

%install
%py3_install
chmod a-x examples/*.py

%check
# Note - tests fail on big-endian, see https://github.com/python-xlib/python-xlib/issues/76
cp %SOURCE1 .
if [ -x /usr/libexec/Xorg ]; then
   Xorg=/usr/libexec/Xorg
elif [ -x /usr/libexec/Xorg.bin ]; then
   Xorg=/usr/libexec/Xorg.bin
else
   Xorg=/usr/bin/Xorg
fi
$Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./xorg.log -config ./xorg.conf -configdir . :99 &
export DISPLAY=:99
%pytest -v || (cat xorg.log && exit 1)
kill %1 || :
cat xorg.log

%files -n python%{python3_pkgversion}-xlib
%license LICENSE
%doc CHANGELOG.md README.rst TODO
%{python3_sitelib}/*

%files doc
%license LICENSE
%doc examples doc/html doc/ps/python-xlib.ps

%changelog
%autochangelog
