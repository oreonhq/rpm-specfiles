%global source0_hash 443697a857c4efacbe08cdaf5182724fa9d9b9a79b8feff2a1601bde1df46b07

Name:           nativefiledialog-extended
Version:        1.2.1
Release:        4%{?dist}
Summary:        Native file dialog library with C and C++ bindings

License:        Zlib
URL:            https://github.com/btzy/nativefiledialog-extended
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel

%global _description %{expand:
A small C library with that portably invokes native file open, folder
select and file save dialogs. Write dialog code once and have it pop up
native dialogs on all supported platforms. Avoid linking large
dependencies like wxWidgets and Qt.

This library is based on Michael Labbe's Native File Dialog (
mlabbe/nativefiledialog).}

%description
%{_description}

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake \
  -D NFD_BUILD_TESTS=OFF \
  -D BUILD_SHARED_LIBRARY=ON
%cmake_build

%check
# all tests will fail because they require a display

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libnfd.so.*

%files devel
%license LICENSE
%{_includedir}/nfd.h*
%{_includedir}/nfd_glfw3.h
%{_includedir}/nfd_sdl2.h
%{_libdir}/libnfd.so
%{_exec_prefix}/lib/cmake/nfd/

%changelog
%autochangelog
