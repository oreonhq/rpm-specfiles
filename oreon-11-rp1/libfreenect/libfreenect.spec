%global source0_hash 3c668053db726206a8c3a92e92e91ef7a64407968f422b9c4b828d0fd234c866
Name:           libfreenect
Version:        0.7.5
Release:        1%{?dist}
Summary:        Device driver for the Kinect
License:        Apache-2.0 AND (GPL-2.0-only OR Apache-2.0) AND MIT AND BSD-2-Clause
URL:            https://github.com/OpenKinect/
Source0:        https://github.com/OpenKinect/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.5.7-videogroup.patch
Patch1:         %{name}-openni2.patch
Patch3:         %{name}-0.4.2-libdir.patch
Patch4:         secarch.patch
Patch5:         %{name}-0.7.5-py3.patch
Patch6:         %{name}-0.7.5-notimestamp.patch
ExcludeArch:    %{ix86}
Requires:       udev
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libusb1-devel
BuildRequires:  opencv-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
# /oreon:deps
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
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_libdir}/openni2
install -p -m 0644 platform/linux/udev/51-kinect.rules %{buildroot}%{_udevrulesdir}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_datadir}/fwfetcher.py %{buildroot}%{_datadir}/%{name}
chmod +x %{buildroot}%{_datadir}/%{name}/fwfetcher.py
mv %{buildroot}%{_libdir}/OpenNI2-FreenectDriver %{buildroot}%{_libdir}/openni2/Drivers
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libfreenect-devel -f %{oreon_filedir}/libfreenect-devel.list
%files -n libfreenect-static -f %{oreon_filedir}/libfreenect-static.list
%files -n libfreenect-fakenect -f %{oreon_filedir}/libfreenect-fakenect.list
%files -n libfreenect-opencv -f %{oreon_filedir}/libfreenect-opencv.list
%files -n python3-libfreenect -f %{oreon_filedir}/python3-libfreenect.list
%files -n libfreenect-openni -f %{oreon_filedir}/libfreenect-openni.list

%changelog

%autochangelog
