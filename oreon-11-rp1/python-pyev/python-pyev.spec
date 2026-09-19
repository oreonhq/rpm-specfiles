%global source0_hash 1711fd92bb21fc1868f0bb5e1b2692b9047c4752515c50b7496a1964e4b4f47d

Name:           python-pyev
Version:        0.9.0
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Summary:        Python binding for the libev library
URL:            https://github.com/gabrielfalcao/pyev
#               https://code.google.com/archive/p/pyev/

%global         gituser         gabrielfalcao
%global         gitname         pyev
%global         gitdate         20130610
%global         commit          e31d13720916439038290d57d00ee3604298705f
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} >= 7 )
%global with_python3 1
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2:        %global __python2 /usr/bin/python2}
%endif

%if 0%{?fedora} <= 21
 %{!?py3_build:         %global py3_build       %{__python3} setup.py build --executable="%{__python3} -s"}
 %{!?py3_install:       %global py3_install     %{__python3} setup.py install -O1 --skip-build --root %{buildroot}}
%endif

# Build source is github release=1 or git commit=0
%global         build_release    0

%if 0%{?build_release}  > 0
Release:        29%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Release:        0.30.%{gitdate}git%{shortcommit}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
%endif #build_release

# https://bugzilla.redhat.com/show_bug.cgi?id=1817984
Patch1:         python3.9.patch

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libev-devel

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif # if with_python3

# html doc generation

%description
Python binding for the libev library.
The libev is an event loop: you register interest in certain events (such
as a file descriptor being readable or a timeout occurring), and it will 
manage these event sources and provide your program with events.

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{gitname}
Summary:        Python3 binding for the libev library
%{?python_provide:%python_provide python%{python3_pkgversion}-%{gitname}}

%description -n python%{python3_pkgversion}-%{gitname}
The libev for Python3 wrapper - This is a Python extension that gives access
to libev library to be called from Python scripts.
%endif # with_python3

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?build_release} > 0
# Build from git release version
%autosetup -p1 -n %{gitname}-%{version}

%else
# Build from git commit
%autosetup -p1 -n %{gitname}-%{commit}
%endif

%build

%if 0%{?with_python3}
%py3_build
%endif # with_python3

%install

%if 0%{?with_python3}
%py3_install
%endif # with_python3

#check

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{gitname}
#license LICENSE
%doc README.md
%{python3_sitearch}/%{gitname}*
%endif # with_python3

%changelog
%autochangelog
