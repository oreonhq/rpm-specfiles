%global source6_hash 1c6b1462066a5452fa50c1da1dd47fed841f28232972c82d778f2962936568c7
%global source5_hash 961df327d8a756304d1b0a67316eebdb1111d13d559f0d3415114ec0eb30abd1
%global source4_hash 00e30d35117ae90a19b5b8878746fceaf31b41778b817ca9e6b3ae6063be8233
%global source3_hash a76ff77815012c76abc9811215c2167128a73a697bcc23948e858d1f7dd54a85
%global source2_hash 05881fd0bd36a5222124dcdd221c20e0e991fa9fb71f91ac0d7e808458b40030
%global source1_hash c5fbc5dcab1d46064001c3b84d7a88812985cde7e0e9ced03f5677bec1ba502a
%global source0_hash 00e30d35117ae90a19b5b8878746fceaf31b41778b817ca9e6b3ae6063be8233
%global appname MangoHud
%global forgeurl https://github.com/flightlessmango/MangoHud
%global imgui_ver 1.91.6
%global imgui_wrap_ver 2
%global vulkan_headers_ver 1.3.283
%global vulkan_headers_wrap_ver 2
%global implot_ver 0.16
%global implot_wrap_ver 2
%global tarball_version %%(echo %{version} | tr '~' '-')
%bcond_with tests
Name:           mangohud
Version:        0.8.4
%forgemeta
Release:        1%{?dist}
Summary:        Vulkan and OpenGL overlay for monitoring FPS, temperatures, CPU/GPU load
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/ocornut/imgui/archive/v%{imgui_ver}/imgui-%{imgui_ver}.tar.gz
Source2:        https://wrapdb.mesonbuild.com/v%{imgui_wrap_ver}/imgui_%{imgui_ver}-1/get_patch#/imgui-%{imgui_ver}-wrap.zip
Source3:        https://github.com/KhronosGroup/Vulkan-Headers/archive/v%{vulkan_headers_ver}/Vulkan-Headers-%{vulkan_headers_ver}.tar.gz
Source4:        https://wrapdb.mesonbuild.com/v%{vulkan_headers_wrap_ver}/vulkan-headers_%{vulkan_headers_ver}-1/get_patch#/vulkan-headers-%{vulkan_headers_ver}-wrap.zip
Source5:        https://github.com/epezent/implot/archive/v%{implot_ver}/implot-%{implot_ver}.tar.gz
Source6:        https://wrapdb.mesonbuild.com/v%{implot_wrap_ver}/implot_%{implot_ver}-1/get_patch#/implot-%{implot_ver}-wrap.zip
Source20:       README.Fedora.md
%if %{with tests}
%endif
Requires:       hicolor-icon-theme
Requires:       vulkan-loader%{?_isa}
Recommends:     (mangohud(x86-32) if glibc(x86-32))
Suggests:       %{name}-mangoplot
Suggests:       goverlay
Provides:       bundled(imgui) = %{imgui_ver}
Provides:       bundled(vulkan-headers) = %{vulkan_headers_ver}
# oreon:deps
BuildRequires:  appstream
BuildRequires:  dbus-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  libcmocka-devel
BuildRequires:  libstdc++-static
BuildRequires:  meson
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  python3-mako
BuildRequires:  vulkan-headers
# /oreon:deps
%description

%package        mangoplot
Summary:        Local visualization "mangoplot" for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       python3-matplotlib
Requires:       python3-numpy
%description    mangoplot
Local visualization "mangoplot" for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{appname}-%{tarball_version} -p1
%setup -qn %{appname}-%{tarball_version} -D -T -a1
%setup -qn %{appname}-%{tarball_version} -D -T -a2
%setup -qn %{appname}-%{tarball_version} -D -T -a3
%setup -qn %{appname}-%{tarball_version} -D -T -a4
%setup -qn %{appname}-%{tarball_version} -D -T -a5
%setup -qn %{appname}-%{tarball_version} -D -T -a6

# imgui
mv imgui-%{imgui_ver} subprojects/
# Vulkan-Headers
mv Vulkan-Headers-%{vulkan_headers_ver} subprojects/
# implot
mv implot-%{implot_ver} subprojects/

%if %{with tests}
# Use system cmocka instead of subproject
# https://gitlab.archlinux.org/archlinux/packaging/packages/mangohud/-/blob/0.6.9.1-10/PKGBUILD?ref_type=tags#L32
sed -i "s/  cmocka = subproject('cmocka')//g" meson.build
sed -i "s/cmocka_dep = cmocka.get_variable('cmocka_dep')/cmocka_dep = dependency('cmocka')/g" meson.build
%endif

%build

%meson \
    -Dmangoapp=true \
    -Dmangohudctl=true \
    -Dinclude_doc=true \
    -Duse_system_spdlog=enabled \
    -Dwith_wayland=enabled \
    -Dwith_xnvctrl=disabled \
    %if %{with tests}
    -Dtests=enabled \
    %else
    -Dtests=disabled \
    %endif
    %{nil}
%meson_build
%install
%meson_install
sed -i "s@#!/usr/bin/env python@#!/usr/bin/python3@" \
    %{buildroot}%{_bindir}/mangoplot
install -D -p -m 0644 %{SOURCE20} %{buildroot}%{_docdir}/%{name}/README.Fedora.md
rm %{buildroot}%{_libdir}/libimgui.a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%dnl appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%if %{with tests}
%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n mangohud-mangoplot -f %{oreon_filedir}/mangohud-mangoplot.list

%changelog

%autochangelog
