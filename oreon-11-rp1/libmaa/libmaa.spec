%global source0_hash 87860fe529cfe7c08f2b08caa5953e21039827b8e4837ac0f324e5f6c2223942

Name: libmaa
Version: 1.5.1
Release: 5%{?dist}
Summary: Library that implements some basic data structures and algorithms
URL: https://github.com/cheusov/libmaa
License: MIT

Source0: https://github.com/cheusov/libmaa/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: mk-configure
BuildRequires: gcc
BuildRequires: pkgconfig(zlib)

%description
This library implements some basic data structures and algorithms such
as command line arguments handling, base26 and base64 routines, bits
manipulation, debugging and error reporting routines, hash tables,
sets, lists, stacks, skip lists, string pool routines, memory
management routines, parsing routines, process management routines,
source code management routines and timer support.

%package devel
Summary: Development files for libmaa
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files (Headers, etc) for libmaa.

%global env \
        export MKSTATICLIB=no \
        export NOSUBDIR=doc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{env}
%mkcmake

%install
%{env}
%mkcmake install DESTDIR=%{buildroot}
chmod +x %{buildroot}/%{_libdir}/*.so.*

%check
%mkcmake test

%files
%license doc/LICENSE
%doc README doc/NEWS
%{_libdir}/libmaa.so.4{,.*}

%files devel
%{_includedir}/maa*
%{_libdir}/libmaa.so

%changelog
%autochangelog
