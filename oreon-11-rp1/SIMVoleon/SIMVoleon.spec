%global source0_hash ce1cfa0d1286c1eea8780b0f026aba75b280455b719c147f3e5f2c951ac8ebc3

#
# Copyright (c) 2004-2015 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Summary: Volume rendering library for Coin
Name: SIMVoleon
Version: 2.1.0
Release: 11%{?dist}

# Older releases had been licensed GPLv2
License: BSD-3-Clause
URL: http://www.coin3d.org

Source: https://github.com/coin3d/simvoleon/releases/download/simvoleon-%{version}/simvoleon-%{version}-src.tar.gz

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: /usr/bin/iconv
BuildRequires: Coin4-devel
BuildRequires: SoQt-devel
BuildRequires: doxygen

Provides: Coin4-SIMVoleon = %{version}-%{release}

%description
A volume rendering library for Coin.

%package devel
Summary: Development files for SIMVoleon
Requires: %{name} = %{version}-%{release}
Requires: Coin4-devel

Provides: Coin4-SIMVoleon-devel = %{version}-%{release}

%description devel
Development files for SIMVoleon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n simvoleon

# Some sources are ISO-8859-1 encoded
# We want doxygen to generate utf-8 encoded docs from them
for nonUTF8 in \
  lib/VolumeViz/readers/VRVolFileReader.cpp \
; do \
  %{_bindir}/iconv -f ISO-8859-1 -t utf-8 $nonUTF8 > $nonUTF8.conv
  mv -f $nonUTF8.conv $nonUTF8
done

# No timestamps in doxygen generated docs!
sed -i -e 's,HTML_TIMESTAMP.*= YES,HTML_TIMESTAMP = NO,' \
  docs/simvoleon.doxygen.cmake.in

%build
mkdir -p build-%{_build_arch}
pushd build-%{_build_arch}
%cmake -DSIMVOLEON_BUILD_DOCUMENTATION=TRUE \
       -DSIMVOLEON_BUILD_TESTS=FALSE \
       -DSIMVOLEON_BUILD_DOC_MAN=TRUE \
       -S .. -B .

%make_build
popd

%install
pushd build-%{_build_arch}
%make_install

# Remove stray files
rm -rf %{buildroot}/usr/share/info/SIMVoleon2/
popd

%files
%doc AUTHORS ChangeLog README NEWS
%license COPYING
%{_libdir}/libSIMVoleon*.so.*

%files devel
%{_docdir}/SIMVoleon/html/
%{_includedir}/VolumeViz/
%{_libdir}/libSIMVoleon.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}-%{version}/
%{_mandir}/man3/*.gz

%changelog
%autochangelog
