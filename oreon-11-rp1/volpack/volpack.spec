%global source0_hash b82b143df479add2b3e18499537a79b1b0fa7e1cc88dff2e7481b4ee075719d2

# This code is old and ugly.
%global optflags %{optflags} -std=gnu17

Name:          volpack
Version:       1.0c7
Release:       36%{?dist}
Summary:       Portable library for fast volume rendering
License:       BSD-3-Clause
URL:           http://amide.sourceforge.net
Source0:       http://downloads.sourceforge.net/amide/%{name}/%{name}-%{version}.tgz
Patch0:        volpack-aarch64.patch
Patch1:        volpack-c99.patch
Patch2:        volpack-1.0c7-fix-casts.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: m4

%description 
VolPack is a portable library of fast volume rendering algorithms that
produce high-quality images.

%package       devel
Summary:       Shared libraries and header files for development using volpack
Requires:      volpack = %{version}-%{release}

%description   devel
The volpack-devel package contains the header files and shared libraries
necessary for developing programs using the volpack volume rendering 
library.

%package       doc
Summary:       Documentation and examples for help using volpack
Requires:      volpack = %{version}-%{release}

%description   doc
The volpack-doc package contains docs and examples helpful for developing
programs using the volpack volume rendering library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .aarch64
%patch -P1 -p1 -b .c99
%patch -P2 -p1 -b .fix-casts

%build
%configure --disable-dependency-tracking --disable-static
# no %{?_smp_mflags} because parallel builds will fail very often
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# remove doc and example files we don't want to package
rm -f doc/vp_userguide..pdf doc/Makefile*
pushd examples
make clean
rm -f Makefile.*
chmod 644 test.csh
popd

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING ChangeLog README
%{_mandir}/man3/*.3*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc doc/ examples/

%changelog
%autochangelog
