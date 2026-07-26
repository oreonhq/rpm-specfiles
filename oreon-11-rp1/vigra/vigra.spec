%global source0_hash none

Summary:        Generic Programming for Computer Vision
Name:           vigra
Version:        1.12.1
Release:        7%{?dist}
License:        MIT
# The "Lenna" files are non-free, we need to remove them from the source tarball.
# wget https://github.com/ukoethe/vigra/archive/refs/tags/Version-1-12-1.tar.gz
# tar -zxvf Version-1-12-1.tar.gz
# mv vigra-Version-1-12-1 vigra-1.12.1
# find vigra-1.12.1/ -name "lenna*" -delete
# tar zcf vigra-1.12.1-src-clean.tar.gz vigra-1.12.1/
Source0:        %{name}-%{version}-src-clean.tar.gz
Source1:        vigra-config.sh
# Avoid attempt to install non-free 'lenna' files
Patch1:         vigra-1.10.0-no-lenna.patch
Patch2:         vigra-1.11.1.docdir.patch
URL:            http://ukoethe.github.io/vigra/
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  fftw-devel >= 3
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  doxygen
%if ! 0%{?rhel}
Requires: python3
BuildRequires:  hdf5-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(Imath)
BuildRequires:  python3-numpy-f2py
BuildRequires:  python3-pytest
BuildRequires:  boost-python3
BuildRequires:  boost-python3-devel
%else
Requires: python
%endif

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel computer vision
library that puts its main emphasis on customizable algorithms and data
structures. By using template techniques similar to those in the C++ Standard
Template Library, you can easily adapt any VIGRA component to the needs of your
application without thereby giving up execution speed.

%package devel
Summary: Development tools for programs which will use the vigra library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libjpeg-devel libtiff-devel libpng-devel zlib-devel fftw-devel >= 3
Requires: boost-devel
%if ! 0%{?rhel}
Requires: hdf5-devel
Requires: OpenEXR-devel
Requires: python3-numpy-f2py boost-python3 boost-python3-devel
%endif

%description devel
The vigra-devel package includes the header files necessary for developing
programs that use the vigra library.

%if ! 0%{?rhel}
%package -n python3-vigra
%{?python_provide:%python_provide python3-vigra}
Summary: Python 3 interface for the vigra computer vision library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-numpy python3-numpy-f2py

%description -n python3-vigra
The python3-vigra package provides python 3 bindings for vigra
%endif

%prep
%autosetup -p1

%build
# Will need to set LEMON_DIR to /usr/share/coin-or-lemon/cmake to compile WITH_LEMON
# once the coin-or-lemon package's installed cmake is fixed for x86_64 arch.
%if ! 0%{?rhel}
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' \
       config/vigra-config.in
sed -i 's=SET(BOOST_PYTHON_NAMES=& boost_python%{python3_version_nodots}=' \
      config/FindVIGRANUMPY_DEPENDENCIES.cmake

export CXXFLAGS="%{optflags} -DH5_USE_110_API"
%cmake -DWITH_OPENEXR=1 -DWITH_HDF5=1 -DWITH_VALGRIND=0 -DWITH_LEMON=0 \
          -DPYTHON_NUMPY_INCLUDE_DIR=%{_includedir}/numpy \
          -DWITH_VIGRANUMPY=1 -DVIGRANUMPY_INSTALL_DIR=%{python3_sitearch} \
          -DPYTHON_VERSION=%{python3_version} \
          -DCMAKE_CXX_FLAGS="-Wno-template-body %{build_cxxflags}"
%cmake_build
%else
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python}=' \
      config/vigra-config.in

%cmake . -DWITH_OPENEXR=0 -DWITH_HDF5=0 -DWITH_VIGRANUMPY=0 -DWITH_VALGRIND=0 -DWITH_LEMON=0
make VERBOSE=1 %{?_smp_mflags}
%endif

# cleanup
rm -f doc/vigranumpy/.buildinfo
rm -f doc/vigra/lenna*
rm -f doc/vigranumpy/vigra/lenna*
find ./doc/ -type f | xargs chmod -x

%install
rm -rf %{buildroot}

%if ! 0%{?rhel}
%cmake_install
mv %{buildroot}/%{_libdir}/vigranumpy/VigranumpyConfig.cmake \
   %{buildroot}/%{_libdir}/vigranumpy/Vigranumpy3Config.cmake

%else
make install DESTDIR=%{buildroot}
%endif

rm -rf %{buildroot}%{_prefix}/doc
(
 cd %{buildroot}%{_bindir}
 mv vigra-config vigra-config-%{__isa_bits}
)
install -p -m755 -D %{SOURCE1} %{buildroot}%{_bindir}/vigra-config

%ldconfig_scriptlets

%files
%doc LICENSE.txt
%{_libdir}/libvigraimpex.so.*

%files devel
%{_includedir}/vigra
%{_bindir}/vigra-config*
%{_libdir}/libvigraimpex.so
%{_libdir}/vigra
%doc doc/vigra

%if ! 0%{?rhel}
%files -n python3-vigra
%{python3_sitearch}/vigra
%{_libdir}/vigranumpy
%endif

%changelog
%autochangelog
