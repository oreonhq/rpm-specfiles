%global source0_hash 3d07cafd0fc5c1b1803e1f6418cf7375a387593e873d3897015b8ec94be20e74
%global abiver 2.58
Name:           librealsense
Version:        2.58.4
Release:        1%{?dist}
Summary:        Cross-platform camera capture for Intel RealSense
License:        Apache-2.0
URL:            https://github.com/IntelRealSense/librealsense
Source0:        https://github.com/IntelRealSense/librealsense/archive/v%{version}.tar.gz#/librealsense-%{version}.tar.gz
Patch0:         librealsense.remove-cflags.patch
Patch1:         librealsense.realsense-file-shared-library.patch
Patch2:         librealsense.use-system-pybind11.patch
Patch3:         librealsense.remove-invalid-unused-code.patch
Patch4:         librealsense.rsutils-shared-library.patch
Patch5:         librealsense.use-system-json.patch
Patch6:         librealsense.utf8-string-literals.patch
Patch7:         librealsense.system-yaml-cpp.patch
Provides:       librealsense2 = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(glfw3)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gdb-headless
BuildRequires:  git-core
BuildRequires:  glfw-devel
BuildRequires:  libGL-devel
BuildRequires:  libcurl-devel
BuildRequires:  libusb1-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  yaml-cpp-devel
# /oreon:deps
%description
The Intel RealSense SDK is a cross-platform library (Linux, OSX, Windows) for
capturing data from the Intel RealSense D400 and SR 300 depth cameras.

For older devices (F200, R200, LR200, ZR300), please use librealsense1.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       librealsense2-devel = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     python3-%{name}
Summary:        Python bindings for %{name}
%{?python_provide:%python_provide python3-%{name}}
Provides:       python3-librealsense2 = %{version}-%{release}
%description -n python3-%{name}
The python3-%{name} package contains python bindings for %{name}.

%package -n     python3-%{name}-devel
Summary:        Python development files for %{name}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
Provides:       python3-librealsense2-devel = %{version}-%{release}
%description -n python3-%{name}-devel
The python3-%{name}-devel package contains libraries and header files for
developing python applications that use %{name}.

%package        doc
BuildArch:      noarch
Summary:        Documentation for %{name}
Provides:       librealsense2-doc = %{version}-%{release}
%description    doc
The %{name}-doc package contains documentation for developing applications
with %{name}.

# enable PIE, we need -fPIC anyway
%global _hardened_build 1

%prep
%oreon_prep
%build

%cmake \
  -DBUILD_UNIT_TESTS=NO \
  -DCHECK_FOR_UPDATES=NO \
  -DCMAKE_INSTALL_BINDIR=%{_bindir} \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
  -DBUILD_PYTHON_BINDINGS:bool=true \
  -DBUILD_ROSBAG2=NO \
  -DPYTHON_EXECUTABLE=%{python3}
%cmake_build
sed -i "s:/usr/local/bin:%{_datadir}/realsense:" config/*
sed -i "s/plugdev/users/g" config/*rules
pushd doc/doxygen
sed -i \
  -e "s/GENERATE_HTMLHELP[[:space:]]*=[[:space:]]*YES/GENERATE_HTMLHELP = NO/" \
  doxyfile
doxygen
popd
%install
%cmake_install
mkdir -p %{buildroot}/%{_udevrulesdir}
install -p -m644 config/99-realsense-libusb.rules %{buildroot}/%{_udevrulesdir}
mkdir -p %{buildroot}/%{_datadir}/realsense
install -p -m755 config/usb-R200-in{,_udev} %{buildroot}/%{_datadir}/realsense
mv %{buildroot}/builddir/Documents/librealsense2/presets %{buildroot}/%{_datadir}/realsense
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n librealsense-devel -f %{oreon_filedir}/librealsense-devel.list
%files -n python3-librealsense -f %{oreon_filedir}/python3-librealsense.list
%files -n python3-librealsense-devel -f %{oreon_filedir}/python3-librealsense-devel.list
%files -n librealsense-doc -f %{oreon_filedir}/librealsense-doc.list

%changelog

%autochangelog
