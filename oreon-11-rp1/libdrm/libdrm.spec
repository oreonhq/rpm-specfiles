# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ac5e74d157830eb8bee44c6a6bf3ad49774ef0dd2a72bdad74a8f20308b52a95

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define bcond_meson() %{lua: do
  local option = rpm.expand("%{1}")
  local with = rpm.expand("%{?with_" .. option .. "}")
  local value = (with ~= '') and "enabled" or "disabled"
  option = option:gsub('_', '-')
  print(string.format("-D%s=%s", option, value))
end}
%define bcond_meson_tf() %{lua: do
  local option = rpm.expand("%{1}")
  local with = rpm.expand("%{?with_" .. option .. "}")
  local value = (with ~= '') and "true" or "false"
  option = option:gsub('_', '-')
  print(string.format("-D%s=%s", option, value))
end}

%bcond_without intel
%bcond_without radeon
%bcond_without amdgpu
%bcond_without nouveau
%bcond_without vmwgfx
%bcond_with    omap
%bcond_with    exynos
%ifarch aarch64
%bcond_without freedreno
%bcond_without freedreno_kgsl
%bcond_without tegra
%bcond_without vc4
%bcond_without etnaviv
%else
%bcond_with    freedreno
%bcond_with    freedreno_kgsl
%bcond_with    tegra
%bcond_with    vc4
%bcond_with    etnaviv
%endif
%bcond_with    cairo_tests
%bcond_without man_pages
%ifarch %{valgrind_arches}
%bcond_without valgrind
%else
%bcond_with    valgrind
%endif
%bcond_without install_test_programs
%bcond_without udev

Name:           libdrm
Summary:        Direct Rendering Manager runtime library
Version:        2.4.134
Release:        1%{?dist}
License:        MIT

%global lib_version %(echo %{version} | sed "s/.*\\.//")

URL:            https://dri.freedesktop.org
Source0:        %{url}/libdrm/%{name}-%{version}.tar.xz
Source1:        README.rst
Source2:        91-drm-modeset.rules
Source3:        %{name}-%{version}.tar.xz.sig
# Simon Ser, 34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48
Source4:        gpgkey-34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48.gpg

Patch1001:      libdrm-make-dri-perms-okay.patch
Patch1002:      libdrm-2.4.0-no-bc.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.43
BuildRequires:  gcc
BuildRequires:  kernel-headers
%if %{with intel}
BuildRequires:  pkgconfig(pciaccess) >= 0.10
%endif
%if %{with cairo_tests}
BuildRequires:  pkgconfig(cairo)
%endif
%if %{with man_pages}
BuildRequires:  python3-docutils
%endif
%if %{with valgrind}
BuildRequires:  valgrind-devel
%endif
%if %{with udev}
BuildRequires:  pkgconfig(udev)
BuildRequires:  systemd-rpm-macros
%endif
BuildRequires:  chrpath

%description
Direct Rendering Manager runtime library

%package devel
Summary:        Direct Rendering Manager development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kernel-headers

%description devel
Direct Rendering Manager development package.

%if %{with install_test_programs}
%package -n drm-utils
Summary:        Direct Rendering Manager utilities
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n drm-utils
Utility programs for the kernel DRM interface.  Will void your warranty.
%endif

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE4} --sig %{SOURCE3} --data %{SOURCE0}
%autosetup -p1

%build
%meson \
  %{bcond_meson intel}                 \
  %{bcond_meson radeon}                \
  %{bcond_meson amdgpu}                \
  %{bcond_meson nouveau}               \
  %{bcond_meson vmwgfx}                \
  %{bcond_meson omap}                  \
  %{bcond_meson exynos}                \
  %{bcond_meson freedreno}             \
  %{bcond_meson tegra}                 \
  %{bcond_meson vc4}                   \
  %{bcond_meson etnaviv}               \
  %{bcond_meson cairo_tests}           \
  %{bcond_meson man_pages}             \
  %{bcond_meson valgrind}              \
  %{bcond_meson_tf freedreno_kgsl}        \
  %{bcond_meson_tf install_test_programs} \
  %{bcond_meson_tf udev}                  \
  %{nil}
%meson_build

%install
%meson_install
%if %{with install_test_programs}
chrpath -d %{_vpath_builddir}/tests/drmdevice
install -Dpm0755 -t %{buildroot}%{_bindir} %{_vpath_builddir}/tests/drmdevice
%endif
%if %{with udev}
install -Dpm0644 -t %{buildroot}%{_udevrulesdir} %{S:2}
%endif
mkdir -p %{buildroot}%{_docdir}/libdrm
cp %{SOURCE1} %{buildroot}%{_docdir}/libdrm

%check
%meson_test

%ldconfig_scriptlets

%files
%doc README.rst
%{_libdir}/libdrm.so.2
%{_libdir}/libdrm.so.2.%{lib_version}.0
%dir %{_datadir}/libdrm
%if %{with intel}
%{_libdir}/libdrm_intel.so.1
%{_libdir}/libdrm_intel.so.1.%{lib_version}.0
%endif
%if %{with radeon}
%{_libdir}/libdrm_radeon.so.1
%{_libdir}/libdrm_radeon.so.1.%{lib_version}.0
%endif
%if %{with amdgpu}
%{_libdir}/libdrm_amdgpu.so.1
%{_libdir}/libdrm_amdgpu.so.1.%{lib_version}.0
%{_datadir}/libdrm/amdgpu.ids
%endif
%if %{with nouveau}
%{_libdir}/libdrm_nouveau.so.2
%{_libdir}/libdrm_nouveau.so.2.%{lib_version}.0
%endif
%if %{with omap}
%{_libdir}/libdrm_omap.so.1
%{_libdir}/libdrm_omap.so.1.0.0
%endif
%if %{with exynos}
%{_libdir}/libdrm_exynos.so.1
%{_libdir}/libdrm_exynos.so.1.0.0
%endif
%if %{with freedreno}
%{_libdir}/libdrm_freedreno.so.1
%{_libdir}/libdrm_freedreno.so.1.%{lib_version}.0
%endif
%if %{with tegra}
%{_libdir}/libdrm_tegra.so.0
%{_libdir}/libdrm_tegra.so.0.%{lib_version}.0
%endif
%if %{with etnaviv}
%{_libdir}/libdrm_etnaviv.so.1
%{_libdir}/libdrm_etnaviv.so.1.%{lib_version}.0
%endif
%if %{with udev}
%{_udevrulesdir}/91-drm-modeset.rules
%endif

%files devel
%dir %{_includedir}/libdrm
%{_includedir}/libdrm/drm.h
%{_includedir}/libdrm/drm_fourcc.h
%{_includedir}/libdrm/drm_mode.h
%{_includedir}/libdrm/drm_sarea.h
%{_includedir}/libdrm/*_drm.h
%{_libdir}/libdrm.so
%{_libdir}/pkgconfig/libdrm.pc
%if %{with intel}
%{_includedir}/libdrm/intel_*.h
%{_libdir}/libdrm_intel.so
%{_libdir}/pkgconfig/libdrm_intel.pc
%endif
%if %{with radeon}
%{_includedir}/libdrm/radeon_{bo,cs,surface}*.h
%{_includedir}/libdrm/r600_pci_ids.h
%{_libdir}/libdrm_radeon.so
%{_libdir}/pkgconfig/libdrm_radeon.pc
%endif
%if %{with amdgpu}
%{_includedir}/libdrm/amdgpu.h
%{_libdir}/libdrm_amdgpu.so
%{_libdir}/pkgconfig/libdrm_amdgpu.pc
%endif
%if %{with nouveau}
%{_includedir}/libdrm/nouveau/
%{_libdir}/libdrm_nouveau.so
%{_libdir}/pkgconfig/libdrm_nouveau.pc
%endif
%if %{with omap}
%{_includedir}/libdrm/omap_*.h
%{_includedir}/omap/
%{_libdir}/libdrm_omap.so
%{_libdir}/pkgconfig/libdrm_omap.pc
%endif
%if %{with exynos}
%{_includedir}/libdrm/exynos_*.h
%{_includedir}/exynos/
%{_libdir}/libdrm_exynos.so
%{_libdir}/pkgconfig/libdrm_exynos.pc
%endif
%if %{with freedreno}
%{_includedir}/freedreno/
%{_libdir}/libdrm_freedreno.so
%{_libdir}/pkgconfig/libdrm_freedreno.pc
%endif
%if %{with tegra}
%{_includedir}/libdrm/tegra.h
%{_libdir}/libdrm_tegra.so
%{_libdir}/pkgconfig/libdrm_tegra.pc
%endif
%if %{with vc4}
%{_includedir}/libdrm/vc4_*.h
%{_libdir}/pkgconfig/libdrm_vc4.pc
%endif
%if %{with etnaviv}
%{_includedir}/libdrm/etnaviv_*.h
%{_libdir}/libdrm_etnaviv.so
%{_libdir}/pkgconfig/libdrm_etnaviv.pc
%endif
%{_includedir}/libsync.h
%{_includedir}/xf86drm.h
%{_includedir}/xf86drmMode.h
%if %{with man_pages}
%{_mandir}/man3/drm*.3*
%{_mandir}/man7/drm*.7*
%endif

%if %{with install_test_programs}
%files -n drm-utils
%if %{with amdgpu}
%{_bindir}/amdgpu_stress
%endif
%{_bindir}/drmdevice
%if %{with etnaviv}
%exclude %{_bindir}/etnaviv_*
%endif
%if %{with exynos}
%exclude %{_bindir}/exynos_*
%endif
%if %{with tegra}
%exclude %{_bindir}/tegra-*
%endif
%{_bindir}/modeprint
%{_bindir}/modetest
%{_bindir}/proptest
%{_bindir}/vbltest
%endif

%changelog
%autochangelog
