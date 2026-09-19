%global source0_hash none

%global release_date 2024Nov13

%global majornum 0

%ifarch %{java_arches}
%global JAVA 1
%else
%global JAVA 0
%endif

Name:           healpix
Version:        3.83
Release:        3%{?dist}
Summary:        Hierarchical Equal Area isoLatitude Pixelization of a sphere

License:        GPL-2.0-or-later
URL:            http://healpix.jpl.nasa.gov/
Source0:        http://downloads.sourceforge.net/project/healpix/Healpix_%{version}/Healpix_%{version}_%{release_date}.tar.gz
Source1:        Makefile_f

Patch0:         healpix-3.31-java-use-system-libraries.patch
Patch1:         healpix-3.82_javadoc.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cfitsio-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  zlib-devel

%if %{JAVA}
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  nom-tam-fits
%endif

%description
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains Fortran binaries and libraries.

NB. Due to some generic names, the binaries have been renamed to start with
hp_, e.g. anafast is now hp_anafast.

%package devel
Summary:        Healpix Fortran headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gcc-gfortran

%description devel
This package contains the Fortran module files needed to compile against
the HEALPix Fortran libraries.

%package c++
Summary:        Healpix C++ binaries and libraries
Provides:       bundled(libsharp)

%description c++
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains HEALPix binaries and libraries that are written in C++.

NB. Due to some generic names, the binaries have been renamed to start with
hp_, e.g. anafast is now hp_anafast.

%package c++-devel
Summary:        Healpix C++ headers
Requires:       %{name}-c++%{?_isa} = %{version}-%{release}

%description c++-devel
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains development headers for the C++ part of HEALPix.

%package -n c%{name}
Summary:        HEALPix C Bindings Library

%description -n c%{name}
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains the library for tools that use HEALPix C bindings.

%package -n c%{name}-devel
Summary:        HEALPix C Bindings Library development files
Requires:       c%{name}%{?_isa} = %{version}-%{release}

%description -n c%{name}-devel
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains the C include file for development with HEALPix.

%if %{JAVA}
%package java
Summary:        Java version of HEALPix
BuildArch:      noarch
Requires:       java
Requires:       jpackage-utils
Requires:       nom-tam-fits

%description java
HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
of a sphere. As suggested in the name, this pixelization produces a
subdivision of a spherical surface in which each pixel covers the same
surface area as every other pixel.

This package contains the Java version of HEALPix.

%package javadoc
Summary:        Javadocs for %{name}
BuildArch:      noarch
Requires:       jpackage-utils

%description javadoc
This package contains the Java API documentation for %{name}.
%endif

%prep
%setup -q -n Healpix_%{version}

%if %{JAVA}
%patch -P0 -p1
%patch -P1 -p1
%endif

cp %{SOURCE1} Makefile
mkdir binf libf includef
pushd libf
%__ln_s libhealpix.so.%{majornum} libhealpix.so
%__ln_s libhpxgif.so.%{majornum} libhpxgif.so
popd

%build
### libsharp
pushd src/common_libraries/libsharp
autoreconf -fi
%configure --enable-static=no
make
popd

### Fortran build
make F90_FFLAGS="%{optflags} -I$(pwd)/includef -fopenmp -fPIC " \
    SHLIB_SUFFIX=".so.%{majornum}" \
    F90_LIBSUFFIX=".so.%{majornum}" \
    F90_CFLAGS="%{optflags} -std=c99 -I$(pwd)/src/common_libraries/libsharp -fopenmp -fPIC" \
    FITSDIR=%{_libdir}

### C bindings
pushd src/C/autotools
autoreconf -fi
%configure --enable-static=no
make
popd

### C++ bindings
pushd src/cxx
export SHARP_LIBS="-L../common_libraries/libsharp/.libs/"
export SHARP_CFLAGS="-I../common_libraries/libsharp"
autoreconf -fi
%configure --enable-static=no
make LDFLAGS="%{build_ldflags} -L../common_libraries/libsharp/.libs/ -lsharp"
popd

%if %{JAVA}
### Java build
pushd src/java
# We don't want to have prebuilt bundled jars!
rm lib/*.jar
ant
popd
%endif

%install
pushd src/C/autotools
%make_install
popd

pushd src/cxx
%make_install
popd

# Rename binaries to have prefix hp_
pushd %{buildroot}%{_bindir}
for exec in *; do
        mv $exec hp_$exec
done
popd

#Fortran
pushd binf
install -d %{buildroot}%{_bindir}
install -D -m 755 alteralm %{buildroot}%{_bindir}/hp_alteralm
install -D -m 755 anafast %{buildroot}%{_bindir}/hp_anafast
install -D -m 755 hotspot %{buildroot}%{_bindir}/hp_hotspot
install -D -m 755 map2gif %{buildroot}%{_bindir}/hp_map2gif
install -D -m 755 median_filter %{buildroot}%{_bindir}/hp_median_filter
install -D -m 755 plmgen %{buildroot}%{_bindir}/hp_plmgen
install -D -m 755 process_mask %{buildroot}%{_bindir}/hp_process_mask
install -D -m 755 sky_ng_sim %{buildroot}%{_bindir}/hp_sky_ng_sim
install -D -m 755 sky_ng_sim_bin %{buildroot}%{_bindir}/hp_sky_ng_sim_bin
install -D -m 755 smoothing %{buildroot}%{_bindir}/hp_smoothing
install -D -m 755 synfast %{buildroot}%{_bindir}/hp_synfast
install -D -m 755 ud_grade %{buildroot}%{_bindir}/hp_ud_grade
popd

pushd libf
install -d %{buildroot}%{_libdir}
install -D -m 755 libhealpix.so.%{majornum} %{buildroot}%{_libdir}
install -D -m 755 libhpxgif.so.%{majornum} %{buildroot}%{_libdir}
popd
pushd %{buildroot}%{_libdir}
ln -s libhealpix.so.%{majornum} libhealpix.so
ln -s libhpxgif.so.%{majornum} libhpxgif.so
popd

pushd includef
install -d %{buildroot}/%{_fmoddir}/healpix
install -D -m 644 *.mod %{buildroot}/%{_fmoddir}/healpix
popd

# Install libsharp
pushd src/common_libraries/libsharp
install -D -m 755 .libs/libsharp.so.2.0.2 %{buildroot}%{_libdir}
install -D -m 644 libsharp.pc %{buildroot}/%{_libdir}/pkgconfig/
popd

pushd %{buildroot}%{_libdir}
ln -s libsharp.so.2.0.2 libsharp.so.2
ln -s libsharp.so.2.0.2 libsharp.so
popd

# remove unwanted files
rm -f %{buildroot}%{_libdir}/*.la

%if %{JAVA}
### Java install
pushd src/java
mkdir -p %{buildroot}%{_javadir}
install -m 644 dist/jhealpix.jar %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_javadocdir}
cp -rp doc %{buildroot}%{_javadocdir}/%{name}
popd
%endif

%files
%license COPYING READ_Copyrights_Licenses.txt
%{_bindir}/hp_alteralm
%{_bindir}/hp_anafast
%{_bindir}/hp_hotspot
%{_bindir}/hp_map2gif
%{_bindir}/hp_median_filter
%{_bindir}/hp_plmgen
%{_bindir}/hp_sky_ng_sim
%{_bindir}/hp_sky_ng_sim_bin
%{_bindir}/hp_smoothing
%{_bindir}/hp_synfast
%{_bindir}/hp_ud_grade
%{_bindir}/hp_compute_weights
%{_bindir}/hp_needlet_tool
%{_libdir}/libhealpix.so.*
%{_libdir}/libhpxgif.so.*

%files devel
%{_libdir}/libhealpix.so
%{_libdir}/libhpxgif.so
%{_fmoddir}/healpix/

%files c++
%license COPYING READ_Copyrights_Licenses.txt
%{_bindir}/hp_alice3
%{_bindir}/hp_alm2map_cxx
%{_bindir}/hp_anafast_cxx
%{_bindir}/hp_calc_powspec
%{_bindir}/hp_hotspots_cxx
%{_bindir}/hp_map2tga
%{_bindir}/hp_median_filter_cxx
%{_bindir}/hp_mult_alm
%{_bindir}/hp_process_mask
%{_bindir}/hp_rotalm_cxx
%{_bindir}/hp_smoothing_cxx
%{_bindir}/hp_syn_alm_cxx
%{_bindir}/hp_udgrade_cxx
%{_bindir}/hp_udgrade_harmonic_cxx
%{_libdir}/libhealpix_cxx.so.*
%{_libdir}/libsharp.so.2*

%files c++-devel
%{_libdir}/libhealpix_cxx.so
%{_libdir}/libsharp.so
%dir %{_includedir}/healpix_cxx
%{_includedir}/healpix_cxx/*.h
%{_libdir}/pkgconfig/healpix_cxx.pc
%{_libdir}/pkgconfig/libsharp.pc

%files -n chealpix
%license COPYING READ_Copyrights_Licenses.txt
%{_libdir}/libchealpix.so.*

%files -n chealpix-devel
%{_libdir}/libchealpix.so
%{_includedir}/chealpix.h
%{_libdir}/pkgconfig/chealpix.pc

%if %{JAVA}
%files java
%license COPYING READ_Copyrights_Licenses.txt
%{_javadir}/jhealpix.jar

%files javadoc
%license COPYING READ_Copyrights_Licenses.txt
%{_javadocdir}/%{name}
%endif

%changelog
%autochangelog
