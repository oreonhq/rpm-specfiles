%global debug_package %{nil}

Name:           vulkan-volk
Version:        1.4.341.0
Release:        %autorelease
Summary:        Meta loader for Vulkan API

License:        MIT
URL:            https://github.com/zeux/volk
Source0:        https://github.com/zeux/volk/archive/vulkan-sdk-1.4.341.0.tar.gz#/Vulkan-Volk-sdk-1.4.341.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 42df539c70ffdaea259e317aef73524512f4093f6f4dafb36fa6cf2680c823b9
%global source0_file vulkan-sdk-1.4.341.0.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/vulkan-sdk-1.4.341.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "42df539c70ffdaea259e317aef73524512f4093f6f4dafb36fa6cf2680c823b9" || { echo "oreon: Source0 SHA256 mismatch for vulkan-sdk-1.4.341.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
