%global source0_hash a6639a556650e6ea8632a17b8188a69de844bdff54ce121a1fd5b92c8dd06cb1

# No more Java on i686
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

Name: hdf
Version: 4.3.0
Release: 5%{?dist}
Summary: A general purpose library and file format for storing scientific data
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://portal.hdfgroup.org/
Source0: https://github.com/HDFGroup/hdf4/archive/refs/tags/hdf%{version}.tar.gz
Source1: h4comp
# Fix java build
Patch1: hdf-build.patch

# For destdir/examplesdir patches
BuildRequires: automake, libtool, gcc, gcc-c++
BuildRequires: chrpath
BuildRequires: flex byacc libjpeg-devel zlib-devel %{!?el6:libaec-devel}
BuildRequires: libtirpc-devel
BuildRequires: gcc-gfortran, gcc
%if %{with java}
BuildRequires: java-devel
BuildRequires: javapackages-tools
BuildRequires: hamcrest
BuildRequires: junit
BuildRequires: slf4j
%else
Obsoletes:     java-hdf < %{version}-%{release}
%endif
BuildRequires: make
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
HDF4 is a general purpose library and file format for storing scientific data.
HDF4 can store two primary objects: datasets and groups. A dataset is
essentially a multidimensional array of data elements, and a group is a
structure for organizing objects in an HDF4 file. Using these two basic
objects, one can create and store almost any kind of scientific data
structure, such as images, arrays of vectors, and structured and unstructured
grids. You can also mix and match them in HDF4 files according to your needs.

%package devel
Summary: HDF4 development files
Provides: %{name}-static = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libjpeg-devel%{?_isa}
Requires: libtirpc-devel%{?_isa}
Requires: zlib-devel%{?_isa}

%description devel
HDF4 development headers and libraries.

%package examples
Summary: HDF4 example source files
BuildArch: noarch

%description examples
HDF4 example source files.

%package libs
Summary: HDF4 shared libraries

%description libs
HDF4 shared libraries.

%package static
Summary: HDF4 static libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
HDF4 static libraries.

%if %{with java}
%package -n java-hdf
Summary: HDF4 java library
Requires:  slf4j
Obsoletes: jhdf < 3.3.1-2

%description -n java-hdf
HDF4 java library
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n hdf4-hdf%{version}
%patch -P 1 -p1 -b .build

%if %{with java}
# Replace jars with system versions
# hamcrest-core is obsoleted in hamcrest-2.2
# Junit tests are failing with junit-4.13.1
%if 0%{?rhel} >= 9 || 0%{?fedora}
find . ! -name junit.jar -name "*.jar" -delete
ln -s $(build-classpath hamcrest) java/lib/hamcrest-core.jar
%else
find . -name "*.jar" -delete
ln -s $(build-classpath hamcrest/core) java/lib/hamcrest-core.jar
ln -s $(build-classpath junit) java/lib/junit.jar
# Fix test output
junit_ver=$(sed -n '/<version>/{s/^.*>\([0-9]\.[0-9.]*\)<.*/\1/;p;q}' /usr/share/maven-poms/junit.pom)
sed -i -e "s/JUnit version .*/JUnit version $junit_ver/" java/test/testfiles/JUnit-*.txt
%endif
ln -s $(build-classpath slf4j/api) java/lib/slf4j-api-1.7.33.jar
ln -s $(build-classpath slf4j/nop) java/lib/ext/slf4j-nop-1.7.33.jar
ln -s $(build-classpath slf4j/simple) java/lib/ext/slf4j-simple-1.7.33.jar
%endif

find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.c" -exec chmod 0644 '{}' \;

# restore include file timestamps modified by patching
#touch -c -r ./hdf/src/hdfi.h.ppc ./hdf/src/hdfi.h

%build
# This should be removed once rebased to an upstream version with
# C99 compatibility fixes (bug 2167466).
#global build_type_safety_c 0

# For destdir/examplesdir patches
autoreconf -vif

# avoid upstream compiler flags settings
rm config/*linux-gnu

# TODO: upstream fix
# libmfhdf.so is link to libdf.so
export CFLAGS="%{optflags} -std=gnu17 -I%{_usr}/include/tirpc"
export LIBS="-ltirpc"
%global _configure ../configure
# Java test needs this but doesn't create it
mkdir -p build-shared/java/lib
cd build-shared
# Java requires shared libraries, fortran requires static
%configure --disable-production %{?with_java:--enable-java} --disable-netcdf \
 --enable-shared=yes --enable-static=no --disable-fortran %{!?el6:--with-szlib} \
 --includedir=%{_includedir}/%{name}
%make_build
cd -
mkdir build-static
cd build-static
# Java requires shared libraries, fortran requires static

# Temporary workaround for compiling on GCC-10
%if 0%{?fedora} || 0%{?rhel} > 8 || 0%{?oreon}
export FCFLAGS="%{build_fflags} -fallow-argument-mismatch"
export FFLAGS="%{build_fflags} -fallow-argument-mismatch"
%endif
%configure --disable-production --disable-java --disable-netcdf \
 --enable-shared=no --enable-static=yes --enable-fortran %{!?el6:--with-szlib} \
 --includedir=%{_includedir}/%{name}
%make_build
cd -

# correct the timestamps based on files used to generate the header files
touch -c -r hdf/src/hdf.inc hdf/src/hdf.f90
touch -c -r hdf/src/dffunc.inc hdf/src/dffunc.f90
touch -c -r mfhdf/fortran/mffunc.inc mfhdf/fortran/mffunc.f90
# netcdf fortran include need same treatement, but they are not shipped

%install
%make_install -C build-static
%make_install -C build-shared
chrpath --delete --keepgoing %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/%{name}/*.so.* %{buildroot}%{_libdir}/*.so.* || :

#install -pm 644 README.txt release_notes/*.txt %{buildroot}%{_pkgdocdir}/

rm -f %{buildroot}%{_libdir}/%{name}/*.la
rm -f %{buildroot}%{_libdir}/*.la

#Don't conflict with netcdf
for file in ncdump ncgen; do
  mv %{buildroot}%{_bindir}/$file %{buildroot}%{_bindir}/h$file
  # man pages are the same than netcdf ones
  rm %{buildroot}%{_mandir}/man1/${file}.1
done

#Fixup headers and scripts for multiarch
%if "%{_lib}" == "lib64"
for x in h4cc h4fc
do
  mv %{buildroot}%{_bindir}/${x} \
     %{buildroot}%{_bindir}/${x}-64
  install -m 0755 %SOURCE1 %{buildroot}%{_bindir}/${x}
done
%else
for x in h4cc h4fc
do
  mv %{buildroot}%{_bindir}/${x} \
     %{buildroot}%{_bindir}/${x}-32
  install -m 0755 %SOURCE1 %{buildroot}%{_bindir}/${x}
done
%endif

%check
# https://github.com/HDFGroup/hdf4/issues/473
%ifarch ppc64le s390x
make -j1 -C build-shared check || :
make -j1 -C build-static check || :
%else
make -j1 -C build-shared check
make -j1 -C build-static check
%endif

%files
%license COPYING
%doc README.md release_notes/*.txt
%{_bindir}/*
%exclude %{_bindir}/h4?c*
%{_libdir}/*.so.0*

%files devel
%{_bindir}/h4?c*
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/*.settings

%files examples
%doc HDF4Examples

%files libs
%{_libdir}/*.so.0*

%files static
%{_libdir}/*.a

%if %{with java}
%files -n java-hdf
%{_jnidir}/hdf.jar
%{_libdir}/%{name}/libhdf_java.so
%endif

%changelog
%autochangelog
