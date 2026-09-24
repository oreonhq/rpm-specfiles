%global source0_hash 5cdfb882137e40c0e20f676f9264d94dace952c8622e38cd31cca7d4add54b64

%global debug_package %{nil}

Name:           vulkan-volk
Version:        1.4.350
Release:        %autorelease
Summary:        Meta loader for Vulkan API

License:        MIT
URL:            https://github.com/zeux/volk
Source0:        https://github.com/zeux/volk/archive/vulkan-sdk-1.4.350.tar.gz#/Vulkan-Volk-sdk-1.4.350.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  vulkan-headers

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
Requires:       vulkan-headers
Conflicts:      volk-devel

%description    devel
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n volk-vulkan-sdk-%{version} -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DVOLK_INSTALL:BOOL=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.md
%doc README.md
%dir %{_libdir}/cmake/volk
%{_includedir}/volk.h
%{_includedir}/volk.c
%{_libdir}/cmake/volk/*.cmake
%{_libdir}/libvolk.a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.341.0-1
- Prepare for Oreon 11 (RP1)
