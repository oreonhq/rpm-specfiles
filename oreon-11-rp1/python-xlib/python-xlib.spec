%global source0_hash e10d1b49655800bffe0fbb5eb31eeef915a4421952ef006d468d53d34901f6f8
Name:           python-xlib
Version:        0.33
Release:        16%{?dist}
Summary:        X client library for Python
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/python-xlib/python-xlib
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        xorg.conf
Patch0:         python-xlib-mock.patch
Patch1:         python-xlib-tohex.patch
Patch2:         fix-ssh-tunnel-auth
Patch4:         python-xlib-test.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-six
BuildRequires:  python3-tkinter
BuildRequires:  tex(dvips)
BuildRequires:  texi2html
BuildRequires:  texinfo-tex
BuildRequires:  xorg-x11-drv-dummy
# /oreon:deps
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
%oreon_prep
%build

%py3_build
cd doc
make html ps
cd html
rm Makefile
%install
%py3_install
chmod a-x examples/*.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

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
%files -f %{oreon_filedir}/main.list
%files -n python3-xlib -f %{oreon_filedir}/python3-xlib.list
%files -n python-xlib-doc -f %{oreon_filedir}/python-xlib-doc.list

%changelog

%autochangelog
