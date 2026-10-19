%global source0_hash fcfbd1199a9a29209231a3002d2ebdf8d22fd990eb1ea14810d6e884c72ef7fe
%if %{undefined package_revision}
%global package_revision 1
%endif
%if %{undefined make_build}
%global make_build %{__make} %{?_smp_mflags}
%endif
%if %{undefined autosetup}
%global autosetup %setup -q
%endif
%global release_version 1.0.68
%global gittag v%{release_version}
%if %{undefined make_check}
%global make_check 1
%endif
Summary:        Fast User Level LOCK (FULLOCK) library for C/C++
Name: libfullock
Version: %{release_version}
Release:        1%{?dist}
License: MIT
URL: https://github.com/yahoojapan/fullock
Source0:        https://github.com/yahoojapan/fullock/archive/%{gittag}/fullock-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
fullock is an open-source software for user level lock library sup-
ported by Yahoo! JAPAN. It runs on user level and provides two types
lock. One is a shared reader/writer lock which has the same function-
ality with pthread_rwlock. Another is a shared mutex lock which also
has the same functionality with pthread_mutex.

Here is primary fullock features:

1. fullock is a thread safety library which can be used for multi-
processing as well as for multi-threading.

2. fullock releases a mutex lock safely even if a lock owner
process exit with 0 in which case OS doesn't release the lock.

3. fullock provides a shared reader/writer lock. A lock owner
thread can get another lock again without deadlock.

Please visit our website and get more details at:

https://github.com/yahoojapan/fullock

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir fullock-%{version}
%oreon_prep
%build

./autogen.sh
%configure --disable-static 
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{__make} check
%if %{defined ldconfig_scriptlets}
%ldconfig_scriptlets
%else
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%endif
%package devel
Summary: Fast User Level LOCK (FULLOCK) library for C/C++ (development)
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development package for building with libfullock shared library.
This package has header files and symbols for it.

%files -f %{oreon_filedir}/main.list
%files -n libfullock-devel -f %{oreon_filedir}/libfullock-devel.list

%changelog

%autochangelog
