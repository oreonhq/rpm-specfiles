%global source0_hash db4a3a853cfbb9e83b27f565b580f6fdc519475b162edc1a656043e1c126e993
%global debug_package %{nil}
Name:           libowfat
Version:        0.30
Release:        31%{?dist}
Summary:        Reimplementation of libdjb
License:        GPL-2.0-only
URL:            http://www.fefe.de/libowfat/
Source0:        http://www.fefe.de/%{name}/%{name}-%{version}.tar.xz
Patch0:         libowfat-0.30-fix-pure-attribute-usage.patch
Patch1:         libowfat-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This library is a reimplementation of libdjb, which means that it provides
Daniel Bernstein's interfaces (with some extensions).

It contains wrappers around memory allocation, buffered I/O, routines for
formatting and scanning, a full DNS resolver, several socket routines,
wrappers for socket functions, mkfifo, opendir, wait, and an abstraction
around errno. It also includes wrappers for Unix signal functions and a
layer of mmap and sendfile.

The library is available for use with the diet libc.

%package        devel
Summary:        Development files for %{name} (Static library only)
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .pure
%patch -P1 -p1
sed -i '/^CFLAGS/d;s/install -m/install -pm/g' GNUmakefile

%build

%make_build -f GNUmakefile CFLAGS="-std=gnu99 %{optflags} -I." 
%install
make -f GNUmakefile install \
        prefix="%{buildroot}%{_prefix}" \
        LIBDIR="%{buildroot}%{_libdir}" \
        INCLUDEDIR="%{buildroot}%{_includedir}/%{name}" \
        MAN3DIR="%{buildroot}%{_mandir}/man3"
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libowfat-devel -f %{oreon_filedir}/libowfat-devel.list

%changelog

%autochangelog
