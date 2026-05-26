Name:      libnumbertext
Version:   1.0.11
Release:   10%{?dist}
Summary:   Number to number name and money text conversion library

#The entire source code is dual license LGPLv3+ or BSD, except for
#the data files hr.sor, sr.sor and sh.sor which are dual license
#CC-BY-SA or LGPLv3+
License:   ( LGPL-3.0-or-later OR BSD-3-Clause ) AND ( LGPL-3.0-or-later OR CC-BY-SA-3.0 )
URL:       https://github.com/Numbertext/libnumbertext
Source:    https://github.com/Numbertext/libnumbertext/releases/download/%{version}/libnumbertext-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 5dcb4db3b2340f81f601ce86d8d76b69e34d70f84f804192c901e4b7f84d5fb0
%global source0_file libnumbertext-1.0.11.tar.xz
# oreon url source checksums end

BuildRequires: autoconf, automake, libtool, gcc-c++
BuildRequires: make

%description
Language-neutral NUMBERTEXT and MONEYTEXT functions for LibreOffice Calc

%package devel
Requires: libnumbertext = %{version}-%{release}
Summary: Files for developing with libnumbertext

%description devel
Includes and definitions for developing with libnumbertext

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libnumbertext-1.0.11.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5dcb4db3b2340f81f601ce86d8d76b69e34d70f84f804192c901e4b7f84d5fb0" || { echo "oreon: Source0 SHA256 mismatch for libnumbertext-1.0.11.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
autoreconf -v --install --force
%configure --disable-silent-rules --disable-static --disable-werror --with-pic
%make_build

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS THANKS
%license COPYING
%{_bindir}/spellout
%{_libdir}/*.so.*
%{_datadir}/libnumbertext

%files devel
%{_includedir}/libnumbertext
%{_libdir}/pkgconfig/libnumbertext.pc
%{_libdir}/*.so

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.11-10
- Import
