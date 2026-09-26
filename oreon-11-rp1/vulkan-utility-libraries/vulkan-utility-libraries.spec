%global source0_hash 972d7e5b2cc9b7b8f9b43fe637b4260a2035bef5bb59bbb7fbf02434610c2b3f

%global debug_package %{nil}

Name:           vulkan-utility-libraries
Version:        1.4.364
Release:        %autorelease
Summary:        Vulkan utility libraries

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Utility-Libraries
Source0:        https://github.com/KhronosGroup/Vulkan-Utility-Libraries/archive/v%{version}.tar.gz#/Vulkan-Utility-Libraries-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  vulkan-headers

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       vulkan-headers
Obsoletes:      vulkan-validation-layers-devel < 1.3.268.0-2
Provides:       vulkan-validation-layers-devel = %{version}-%{release}
Provides:       vulkan-validation-layers-devel%{?_isa} = %{version}-%{release}

%description    devel
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Vulkan-Utility-Libraries-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DBUILD_SHARED_LIBS:BOOL=OFF \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DBUILD_TESTS:BOOL=OFF \
       -DVUL_WERROR:BOOL=OFF \
       -DUPDATE_DEPS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/vulkan/
%{_libdir}/cmake/VulkanUtilityLibraries/*.cmake
%{_libdir}/libVulkanLayerSettings.a
%{_libdir}/libVulkanSafeStruct.a

%changelog
%autochangelog
