Summary:        Libraries for the Matchbox Desktop
Name:           libmatchbox 
Version:        1.9
Release:        41%{?dist}
Url:            http://projects.o-hand.com/matchbox/
License:        LGPL-2.1-or-later
Source:         http://projects.o-hand.com/matchbox/sources/libmatchbox/%{version}/%{name}-%{version}.tar.bz2
Patch0:         libmatchbox-1.9-add-needed.patch
Patch1:         libmatchbox-1.9-libpng.patch
Patch2:         libmatchbox-c99.patch
Patch3:         libmatchbox-hash_empty.patch
BuildRequires:  pango-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  check-devel
BuildRequires:  autoconf automake libtool
BuildRequires:  make

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package devel
Summary:        Static libraries and header files from %{name}
Provides:       matchbox-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       libmb-devel = %{version}-%{release}
Requires:       libmatchbox = %{version}
Requires:       pkgconfig

%description devel
Static libraries and header files from %{name}

%prep
%autosetup -p 1

%build
autoreconf -v --install
%configure --enable-png --enable-jpeg --enable-pango
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'


%ldconfig_scriptlets

%files 
%_libdir/*.so.*

%files devel
%doc AUTHORS ChangeLog README COPYING
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%dir %{_includedir}/libmb
%{_includedir}/libmb/*.h

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9-41
- Import
