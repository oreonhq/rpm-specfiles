%global source0_hash abe134716f4c53fe60db2004b42adf6af60e64e45808135acfa4311454371ece
%bcond_with examples
%global forgeurl https://github.com/libuvc/libuvc
Name:           libuvc
Version:        0.0.8
Release:        1%{?dist}
Summary:        Cross-platform library for USB video devices
License:        BSD-3-Clause AND BSD-1-Clause
URL:            https://libuvc.github.io
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with examples}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libusb1-devel
# /oreon:deps
%description
libuvc is a cross-platform library for USB video devices, built atop libusb. It
enables fine-grained control over USB video devices exporting the standard USB
Video Class (UVC) interface, enabling developers to write drivers for
previously unsupported devices, or just access UVC devices in a generic
fashion.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       %{name}-doc = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch
%description    doc
This package contains developer documentation for %{name}.

%if %{with examples}
%package        examples
Summary:        Examples for %{name}
%description    examples
This package contains examples making use of %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DCMAKE_BUILD_TARGET=Shared \
%if %{with examples}
  -DBUILD_TEST=ON \
  -DBUILD_EXAMPLE=ON
%else
  -DBUILD_TEST=OFF \
  -DBUILD_EXAMPLE=OFF
%endif
%cmake_build
doxygen doxygen.conf
%install
%cmake_install
%if %{with examples}
install -Dpm0755 %{_vpath_builddir}/example %{buildroot}%{_bindir}/uvc_example
install -Dpm0755 -t %{buildroot}%{_bindir} %{_vpath_builddir}/uvc_test
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*
%endif
%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libuvc-devel -f %{oreon_filedir}/libuvc-devel.list
%files -n libuvc-doc -f %{oreon_filedir}/libuvc-doc.list

%changelog

%autochangelog
