Name:           libuninameslist
Version:        20260107
Release:        2%{?dist}

Summary:        A library providing Unicode character names and annotations

License:        BSD-3-Clause
URL:            https://github.com/fontforge/libuninameslist
Source0:        https://github.com/fontforge/libuninameslist/archive/%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 f4cb7ee4e19b6b558d829c44ffa18f3b3a4cda2f61150128b07bb9cbb262414a
%global source0_file 20260107.tar.gz
# oreon url source checksums end
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires: make

%description
libuninameslist provides applications with access to Unicode name and
annotation data from the official Unicode Character Database.

%package        devel
Summary:        Header files and static libraries for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains header files and static libraries for %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/20260107.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f4cb7ee4e19b6b558d829c44ffa18f3b3a4cda2f61150128b07bb9cbb262414a" || { echo "oreon: Source0 SHA256 mismatch for 20260107.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
autoreconf -i
automake --foreign -Wall
%configure --disable-static
make V=1 %{?_smp_mflags}


%install
%make_install incdir=$RPM_BUILD_ROOT%{_includedir}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%files
%license LICENSE
%doc ChangeLog README.md
%{_libdir}/*.so.*

%files devel
%{_mandir}/man3/libuninameslist.3.gz
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libuninameslist.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20260107-2
- Prepare for Oreon 11 (RP1)
