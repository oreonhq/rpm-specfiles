%undefine __cmake_in_source_build

Name:           sdbus-cpp
Version:        2.2.1
Release:        1%{?dist}
Summary:        High-level C++ D-Bus library built on sd-bus

License:        LGPL-2.1-or-later
URL:            https://github.com/Kistler-Group/sdbus-cpp

Source0:        https://github.com/Kistler-Group/sdbus-cpp/archive/refs/tags/v%{version}.tar.gz#/sdbus-cpp-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 da69a0104beb6e51415a59f1571a47beb1eacc65cc6027b250eb1cf13ff4f802
%global source0_file v2.2.1.tar.gz
# oreon url source checksums end

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  systemd-devel

%description
sdbus-c++ is a C++ wrapper around sd-bus from libsystemd. Downstream
projects use it via pkg-config (sdbus-c++) or CMake (SDBusCpp::sdbus-c++).

%package devel
Summary:        Development files for sdbus-cpp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, CMake package config, and pkg-config file for building against
libsdbus-c++.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v2.2.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "da69a0104beb6e51415a59f1571a47beb1eacc65cc6027b250eb1cf13ff4f802" || { echo "oreon: Source0 SHA256 mismatch for v2.2.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n sdbus-cpp-%{version}

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DSDBUSCPP_BUILD_DOCS=OFF \
  -DSDBUSCPP_BUILD_TESTS=OFF \
  -DSDBUSCPP_BUILD_EXAMPLES=OFF \
  -DSDBUSCPP_BUILD_CODEGEN=OFF
%cmake_build

%install
%cmake_install

%files
%license COPYING COPYING-LGPL-Exception
%doc AUTHORS ChangeLog NEWS README README.md
%{_libdir}/libsdbus-c++.so.2*

%files devel
%{_libdir}/libsdbus-c++.so
%{_includedir}/sdbus-c++/
%{_libdir}/pkgconfig/sdbus-c++.pc
%{_libdir}/cmake/sdbus-c++/

%changelog
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.1-1
- Real package from upstream (replace noarch placeholder), v2.2.1

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-1
- Placeholder compatibility package (superseded)
