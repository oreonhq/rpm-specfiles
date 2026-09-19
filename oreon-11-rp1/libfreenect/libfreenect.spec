%global source0_hash 3c668053db726206a8c3a92e92e91ef7a64407968f422b9c4b828d0fd234c866

Name:           libfreenect
Version:        0.7.5
Release:        6%{?dist}
Summary:        Device driver for the Kinect
# Core libfreenect is available as Apache-2.0 OR GPL-2.0-only
# OpenNI driver is available as Apache-2.0
# fakenect/parson.{c,h} is MIT
# fwfetcher.py is BSD-2-Clause
License:        Apache-2.0 AND (GPL-2.0-only OR Apache-2.0) AND MIT AND BSD-2-Clause
URL:            https://github.com/OpenKinect/

Source0:        https://github.com/OpenKinect/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Edit udev rule to only allow access to the device from the video group
Patch0:         %{name}-0.5.7-videogroup.patch
# Freenect openni driver is a plugin lib, and doesn't need soversion symlinks
Patch1:         %{name}-openni2.patch
# Allow for proper libdir
Patch3:         %{name}-0.4.2-libdir.patch
# BZ: https://bugzilla.redhat.com/show_bug.cgi?id=1143912
Patch4:         secarch.patch
# Fix the installation path for python libs
Patch5:         %{name}-0.7.5-py3.patch
# Avoid timestamps in generated docs
Patch6:         %{name}-0.7.5-notimestamp.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  libusb1-devel
BuildRequires:  libGL-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  opencv-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-numpy

Requires:       udev

%description
libfreenect is a free and open source library that provides access to the
Kinect device.  Currently, the library supports the RGB webcam, the depth
image, the LED, and the tilt motor.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Development files for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains static libraries for
developing applications that use %{name}.

%package        fakenect
Summary:        Library to play back recorded data for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# upstream commit f1bb6e7fbe347754fbfc4613bf43000ef0b0c2b2
Provides:       bundled(parson)

%description    fakenect
Fakenect consists of a "record" program to save dumps from the kinect sensor 
and a library that can be linked to, providing an interface compatible with 
freenect.  This allows you to save data and repeat for experiments, debug 
problems, share datasets, and experiment with the kinect without having one.

%package        opencv
Summary:        OpenCV bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    opencv
The %{name}-opencv package contains the libfreenect binding
library for OpenCV development.

%package -n     python3-%{name}
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-numpy

%description -n  python3-%{name}
The %{name}-python package contains python 3 bindings for %{name}

%package        openni
Summary:        OpenNI2 driver for the Kinect

%description    openni
The OpenNI2-FreenectDriver is a bridge to libfreenect implemented as an 
OpenNI2 driver. It allows OpenNI2 to use Kinect hardware on Linux and OSX. 
It was originally a separate project but is now distributed with libfreenect.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
rm -rv platform/windows

%patch -P 0 -p0 -b .videogroup
%patch -P 1 -p1 -b .openni2
%patch -P 3 -p0 -b .libdir
%patch -P 4 -p1 -b .secarch
%patch -P 5 -p1 -b .py3
%patch -P 6 -p1 -b .tstamp

%build
%cmake \
  -DBUILD_AUDIO=ON \
  -DBUILD_C_SYNC=ON \
  -DBUILD_CV=ON \
  -DBUILD_REDIST_PACKAGE=ON \
  -DBUILD_EXAMPLES=ON \
  -DBUILD_FAKENECT=ON \
  -DBUILD_PYTHON=OFF  \
  -DBUILD_PYTHON2=OFF \
  -DBUILD_PYTHON3=ON \
  -DBUILD_OPENNI2_DRIVER=ON

%cmake_build

pushd doc
doxygen Doxyfile
popd

%install
%cmake_install

# Install the kinect udev rule
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_libdir}/openni2
install -p -m 0644 platform/linux/udev/51-kinect.rules %{buildroot}%{_udevrulesdir}

# Delete libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Move the fwfetcher script to the correct datadir
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_datadir}/fwfetcher.py %{buildroot}%{_datadir}/%{name}
chmod +x %{buildroot}%{_datadir}/%{name}/fwfetcher.py

# Move openni plugin: rhbz#1094787
mv %{buildroot}%{_libdir}/OpenNI2-FreenectDriver %{buildroot}%{_libdir}/openni2/Drivers

%files
%license APACHE20 GPL2
%doc README.md CONTRIB
%{_udevrulesdir}/51-kinect.rules
%{_libdir}/libfreenect.so.0{,.*}
%{_libdir}/libfreenect_sync.so.0{,.*}
%{_bindir}/freenect-camtest
%{_bindir}/freenect-chunkview
%{_bindir}/freenect-cpp_pcview
%{_bindir}/freenect-cppview
%{_bindir}/freenect-glpclview
%{_bindir}/freenect-glview
%{_bindir}/freenect-hiview
%{_bindir}/freenect-micview
%{_bindir}/freenect-regtest
%{_bindir}/freenect-regview
%{_bindir}/freenect-tiltdemo
%{_bindir}/freenect-wavrecord
%{_datadir}/%{name}

%files opencv
%{_bindir}/freenect-cvdemo
%{_libdir}/libfreenect_cv.so.0{,.*}

%files devel
%doc doc/html
%doc examples/*.c wrappers/cpp/cppview.cpp
%{_includedir}/libfreenect
%{_libdir}/libfreenect.so
%{_libdir}/libfreenect_cv.so
%{_libdir}/libfreenect_sync.so
%{_libdir}/pkgconfig/libfreenect.pc
%{_libdir}/fakenect/libfakenect.so

%files static
%{_libdir}/libfreenect.a
%{_libdir}/libfreenect_sync.a

%files -n python3-%{name}
%{python3_sitearch}/freenect.so

%files fakenect
%dir %{_libdir}/fakenect
%{_bindir}/fakenect-record
%{_libdir}/fakenect/libfakenect.so.0{,.*}
%{_bindir}/fakenect
%{_mandir}/man1/fakenect-record.1.*
%{_mandir}/man1/fakenect.1.*

%files openni
%license APACHE20 GPL2
%{_libdir}/openni2

%changelog
%autochangelog
