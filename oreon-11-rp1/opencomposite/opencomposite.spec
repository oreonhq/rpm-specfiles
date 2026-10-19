%global source0_hash 3b615f994adfa6184c6ff3b1b6af24965048ea1ddd3c3cf15c2b042282e74c05
%bcond_without bundled_openxr
%global _lto_cflags %nil
%global forgeurl0  https://gitlab.com/znixian/OpenOVR
%global oc_version 1.0.1521
%global tag0       %{oc_version}
%global forgeurl1  https://github.com/KhronosGroup/OpenXR-SDK
%global commit1    91a8a8d9d70f4b469bca0726122c3b5a6096010e
%forgemeta
Name:           opencomposite
Version:        %{oc_version}
Release:        1%{?dist}
Summary:        Reimplementation of OpenVR, translating calls to OpenXR
License:        GPL-3.0-or-later AND MIT AND BSD-3-Clause AND BSD-2-Clause AND Apache-2.0 AND CC-BY-4.0 AND BSL-1.0
URL:            %{forgeurl0}
Source0:        %{forgeurl0}/-/archive/%{version}/OpenOVR-%{version}.tar.bz2
Source1:        %{forgeurl1}/archive/%{commit1}/openxr-sdk-%{commit1}.tar.gz
%if %{without bundled_openxr}
%endif
%if %{with bundled_openxr}
Provides:       bundled(openxr) = 1.0.12
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(vulkan)
# /oreon:deps
%description
OpenComposite OpenXR is an implementation of SteamVR's API - OpenVR, 
forwarding calls directly to the OpenXR runtime.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%if %{with bundled_openxr}
mkdir -p libs/openxr-sdk
tar -xvf %{SOURCE1} --strip-components 1 -C libs/openxr-sdk
%endif

%build

%cmake -GNinja \
    -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=on \
%if %{with bundled_openxr}
    -DUSE_SYSTEM_OPENXR=off \
%else
    -DUSE_SYSTEM_OPENXR=on \
%endif
    -DUSE_SYSTEM_GLM=on \
    -DGLM_ENABLE_EXPERIMENTAL=on \
%cmake_build
%install
%ifarch %{ix86}
mkdir -p %{buildroot}%{_libdir}/%{name}/runtime/bin/
install -Dpm0755 -t %{buildroot}%{_libdir}/%{name}/runtime/bin/ redhat-linux-build/bin/vrclient.so
%else
mkdir -p %{buildroot}%{_libdir}/%{name}/runtime/bin/linux64
install -Dpm0755 -t %{buildroot}%{_libdir}/%{name}/runtime/bin/linux64 redhat-linux-build/bin/linux64/vrclient.so
%oreon_autofiles main
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
