%global source0_hash 553f63d14234c79ce29a63c0594b81d78e716a8d7b28f5cd1f54668b4d54eefe
Name:           libuninameslist
Version:        20260918
Release:        1%{?dist}
Summary:        A library providing Unicode character names and annotations
License:        BSD-3-Clause
URL:            https://github.com/fontforge/libuninameslist
Source0:        https://github.com/fontforge/libuninameslist/archive/refs/tags/%{version}.tar.gz#/libuninameslist-20260918.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
libuninameslist provides applications with access to Unicode name and
annotation data from the official Unicode Character Database.

%package        devel
Summary:        Header files and static libraries for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
This package contains header files and static libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
automake --foreign -Wall
%configure --disable-static
make V=1 %{?_smp_mflags}
%install
%make_install incdir=$RPM_BUILD_ROOT%{_includedir}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libuninameslist-devel -f %{oreon_filedir}/libuninameslist-devel.list

%changelog

%autochangelog
