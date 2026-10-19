%global source0_hash 42e5194ad06ab6ffb806c83eb99c03462b495d979cda782f3c72c08af833cd4e
Summary:        Garbage collector for C and C++
Name:    gc
Version: 8.2.12
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
URL:     https://www.hboehm.info/gc/
Source0:        https://github.com/ivmai/bdw%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Obsoletes: libgc < %{version}-%{release}
Provides:  libgc = %{version}-%{release}
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
The Boehm-Demers-Weiser conservative garbage collector can be
used as a garbage collecting replacement for C malloc or C++ new.

%package devel
Summary: Libraries and header files for %{name} development
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: libgc-devel < %{version}-%{release}
Provides:  libgc-devel = %{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n gc-%{version}%{?pre} -p1

%build

rm -f libtool libtool.m4
autoreconf -i -f
CPPFLAGS="-DUSE_GET_STACKBASE_FOR_MAIN $CPPFLAGS"
CPPFLAGS="-DDONT_UNDEF_EXCEPTIONS $CPPFLAGS"
export CPPFLAGS
%configure \
  --disable-docs \
  --enable-cplusplus \
  --enable-large-config \
  --enable-threads=posix
%make_build
%install
%make_install
install -p -D -m644 doc/gc.man  %{buildroot}%{_mandir}/man3/gc.3
rm -rfv %{buildroot}%{_datadir}/gc/
rm -fv  %{buildroot}%{_libdir}/lib*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch %{arm}
%global arch_ignore ||:
%endif
%ifnarch %{arm} aarch64 %{ix86} ppc64le
make check %{?arch_ignore}
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n gc-devel -f %{oreon_filedir}/gc-devel.list

%changelog

%autochangelog
