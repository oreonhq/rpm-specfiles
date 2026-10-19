%global source1_hash 1b9dfa04b6cb111b4cbd477155be5a675981ed545cc75cf1832961917a83a8d4
%global source0_hash e53b1ac288d017d66dde0471cd429a806168ecf07179d7f019572d7a7e05f0d6
%global talloc_version 2.5.0
Name:           libtevent
Version:        0.17.2
Release:        1%{?dist}
Summary:        The tevent library
License:        LGPL-3.0-or-later
URL:            http://tevent.samba.org/
Source0:        http://samba.org/ftp/tevent/tevent-%{version}.tar.gz
Source1:        http://samba.org/ftp/tevent/tevent-%{version}.tar.asc
Source2:        tevent.keyring
Provides: bundled(libreplace)
Obsoletes: python2-tevent < 0.10.0-1
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-talloc-devel
# /oreon:deps
%description
Tevent is an event system based on the talloc memory management library.
Tevent has support for many event types, including timers, signals, and
the classic file descriptor events.
Tevent also provide helpers to deal with asynchronous code providing the
tevent_req (Tevent Request) functions.

%package devel
Summary:        Developer tools for the Tevent library
Requires: libtevent%{?_isa} = %{version}-%{release}
Requires: libtalloc-devel%{?_isa} >= %{talloc_version}
%description devel
Header files needed to develop programs that link against the Tevent library.

%package -n python3-tevent
Summary:        Python 3 bindings for the Tevent library
Requires: libtevent%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-tevent}
%description -n python3-tevent
Python 3 bindings for libtevent

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
zcat %{SOURCE0} | gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} -
%autosetup -n tevent-%{version} -p1

%build

export PYTHONARCHDIR=%{python3_sitearch}
%configure --disable-rpath \
           --bundled-libraries=NONE \
           --builtin-libraries=replace
%make_build
doxygen doxy.config
%check

%make_build check
%install
%make_install
rm -f doc/man/man3/todo*
install -d -m0755 %{buildroot}%{_mandir}
cp -a doc/man/man3 %{buildroot}%{_mandir}
%oreon_autofiles python3-tevent usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libtevent-devel -f %{oreon_filedir}/libtevent-devel.list
%files -n python3-tevent -f %{oreon_filedir}/python3-tevent.list

%changelog

%autochangelog
