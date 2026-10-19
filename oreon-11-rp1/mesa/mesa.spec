%global source15_hash 357703d41365b4b27c590e3ed91eabb1b663f07c4c084095e60cbed4362dff0d
%global source14_hash 537dd038a89878be9b64dd4bd1b260315c1bb94f4d784956b81e27a088d9a09e
%global source13_hash 6e614ed320ac28113fa64972c4262d5dbc89deacdfd00c34a3e4cea073243c12
%global source12_hash 21b2ebcf727b7760c461f091f9f0f539b77b8e87f2fd88131e7f1b433b3cece4
%global source11_hash 8fd00f0bb2e90d81d1044c2b32617f68fcb9fa3bb7640c23e9c748e53fb30934
%global source10_hash 57c0d7b74b563b49d38dae00a0c37d4d6de9b432382b2892f0574ddcae73fd0a
%global source0_hash 1628058a8d2c0615975de5a15ab7bbb9638c50000b5bed9456ff423ea034a81f
%ifnarch s390x
%global with_hardware 1
%global with_kmsro 1
%global with_radeonsi 1
%global with_spirv_tools 1
%global with_vmware 1
%global with_vulkan_hw 1
%if 0%{?fedora} || 0%{?oreon} >= 11
%global with_r300 1
%global with_r600 1
%global with_opencl 1
%global with_va 1
%endif
%if 0%{?fedora} || 0%{?oreon} >= 11 || (0%{?rhel} > 0 && 0%{?rhel} >= 9)
%global with_nvk %{with_vulkan_hw}
%endif
%global base_vulkan %{?with_vulkan_hw:,amd}%{!?with_vulkan_hw:%{nil}}
%endif
%ifarch aarch64 x86_64
%if 0%{?fedora} || 0%{?oreon} >= 11
%global with_teflon 1
%endif
%endif
%ifarch %{ix86} x86_64
%global with_crocus 1
%global with_iris   1
%global intel_platform_vulkan %{?with_vulkan_hw:,intel,intel_hasvk}%{!?with_vulkan_hw:%{nil}}
%if 0%{?fedora} || 0%{?oreon} >= 11
%global with_i915   1
%endif
%endif
%ifarch x86_64
%if 0%{?with_vulkan_hw}
%global with_intel_vk_rt 1
%endif
%endif
%ifarch aarch64 x86_64 %{ix86}
%if 0%{?fedora} || 0%{?oreon} >= 11
%global with_asahi     1
%global with_d3d12     1
%global with_etnaviv   1
%global with_lima      1
%global with_tegra     1
%global with_vc4       1
%global with_v3d       1
%endif
%global with_freedreno 1
%global with_panfrost  1
%if 0%{?with_asahi}
%global asahi_platform_vulkan %{?with_vulkan_hw:,asahi}%{!?with_vulkan_hw:%{nil}}
%endif
%global extra_platform_vulkan %{?with_vulkan_hw:,broadcom,freedreno,panfrost,imagination}%{!?with_vulkan_hw:%{nil}}
%endif
%if 0%{?fedora} || 0%{?oreon} >= 11
%global with_libunwind 1
%global with_lmsensors 1
%global with_virtio    1
%endif
%ifarch %{valgrind_arches}
%bcond_without valgrind
%else
%bcond_with valgrind
%endif
%global vulkan_drivers swrast%{?base_vulkan}%{?intel_platform_vulkan}%{?asahi_platform_vulkan}%{?extra_platform_vulkan}%{?with_nvk:,nouveau}%{?with_virtio:,virtio}%{?with_d3d12:,microsoft-experimental}
%global _lto_cflags %nil
Name:           mesa
Summary:        Mesa graphics libraries
Version:        26.2.3
Release:        1%{?dist}
License:        MIT AND BSD-3-Clause AND SGI-B-2.0
URL:            https://mesa3d.org
%global ver %{gsub %version ~ -}
Source0:        https://archive.%{name}3d.org/%{name}-%{version}.tar.xz
Source1:        Mesa-MLAA-License-Clarification-Email.txt
%global rust_paste_ver 1.0.15
%global rust_proc_macro2_ver 1.0.106
%global rust_quote_ver 1.0.44
%global rust_syn_ver 2.0.115
%global rust_unicode_ident_ver 1.0.23
%global rustc_hash_ver 2.1.1
Source10:       https://crates.io/api/v1/crates/paste/%{rust_paste_ver}/download#/paste-%{rust_paste_ver}.tar.gz
Source11:       https://crates.io/api/v1/crates/proc-macro2/%{rust_proc_macro2_ver}/download#/proc-macro2-%{rust_proc_macro2_ver}.tar.gz
Source12:       https://crates.io/api/v1/crates/quote/%{rust_quote_ver}/download#/quote-%{rust_quote_ver}.tar.gz
Source13:       https://crates.io/api/v1/crates/syn/%{rust_syn_ver}/download#/syn-%{rust_syn_ver}.tar.gz
Source14:       https://crates.io/api/v1/crates/unicode-ident/%{rust_unicode_ident_ver}/download#/unicode-ident-%{rust_unicode_ident_ver}.tar.gz
Source15:       https://crates.io/api/v1/crates/rustc-hash/%{rustc_hash_ver}/download#/rustc-hash-%{rustc_hash_ver}.tar.gz
%if 0%{?with_hardware}
%endif
%if 0%{?with_libunwind}
%endif
%if 0%{?with_lmsensors}
%endif
%if 0%{?with_va}
%endif
%if 0%{?with_teflon}
%endif
%if 0%{?with_opencl} || 0%{?with_nvk} || 0%{?with_asahi} || 0%{?with_panfrost}
%endif
%if 0%{?with_opencl} || 0%{?with_nvk}
%endif
%if 0%{?with_nvk}
%endif
%if %{with valgrind}
%endif
%if 0%{?with_vulkan_hw}
%endif
%if 0%{?with_d3d12}
%endif
# oreon:deps
BuildRequires:  bindgen
BuildRequires:  bison
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  cbindgen
BuildRequires:  clang-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glslang
BuildRequires:  kernel-headers
BuildRequires:  libstdc++-static
BuildRequires:  llvm-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(LLVMSPIRVLib)
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(libclc)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-pycparser
BuildRequires:  python3-pyyaml
BuildRequires:  rustc
BuildRequires:  systemd-devel
BuildRequires:  vulkan-headers
# /oreon:deps
%description
%{summary}.

%package filesystem
Summary:        Mesa driver filesystem
Provides:       mesa-dri-filesystem = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-omx-drivers < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-libd3d < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-libd3d-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-vdpau-drivers < %{?epoch:%{epoch}:}%{version}-%{release}
%description filesystem
%{summary}.

%package libGL
Summary:        Mesa libGL runtime libraries
Requires:       libglvnd-glx%{?_isa} >= 1:1.3.2
Requires:       %{name}-dri-drivers%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-libOSMesa < 25.1.0~rc2-1
%description libGL
%{summary}.

%package libGL-devel
Summary:        Mesa libGL development package
Requires:       (%{name}-libGL%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release} if %{name}-libGL%{?_isa})
Requires:       libglvnd-devel%{?_isa} >= 1:1.3.2
Provides:       libGL-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       libGL-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     gl-manpages
Obsoletes:      %{name}-libOSMesa-devel < 25.1.0~rc2-1
%description libGL-devel
%{summary}.

%package libEGL
Summary:        Mesa libEGL runtime libraries
Requires:       libglvnd-egl%{?_isa} >= 1:1.3.2
Requires:       %{name}-libgbm%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-dri-drivers%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description libEGL
%{summary}.

%package libEGL-devel
Summary:        Mesa libEGL development package
Requires:       (%{name}-libEGL%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release} if %{name}-libEGL%{?_isa})
Requires:       libglvnd-devel%{?_isa} >= 1:1.3.2
Requires:       %{name}-khr-devel%{?_isa}
Provides:       libEGL-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       libEGL-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description libEGL-devel
%{summary}.

%package dri-drivers
Summary:        Mesa-based DRI drivers
Requires:       %{name}-filesystem%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-libgbm%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       (llvm-libs%{?_isa} or llvm22-libs%{?_isa})
Requires:       spirv-tools-libs%{?_isa}
Obsoletes:      %{name}-libglapi < 25.0.0~rc2-1
Provides:       %{name}-libglapi >= 25.0.0~rc2-1
Obsoletes:      %{name}-va-drivers < 26.0.0-5
Provides:       %{name}-va-drivers = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-va-drivers%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-vaapi-drivers < 22.2.0-5
%description dri-drivers
%{summary}.

%package libgbm
Summary:        Mesa gbm runtime library
Provides:       libgbm = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       libgbm%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     %{name}-dri-drivers%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       (%{name}-dri-drivers%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release} if %{name}-dri-drivers%{?_isa})
%description libgbm
%{summary}.

%package libgbm-devel
Summary:        Mesa libgbm development package
Requires:       %{name}-libgbm%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       libgbm-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       libgbm-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description libgbm-devel
%{summary}.

%if 0%{?with_opencl}
%package libOpenCL
Summary:        Mesa OpenCL runtime library
Requires:       (ocl-icd%{?_isa} or OpenCL-ICD-Loader%{?_isa})
Requires:       libclc%{?_isa}
Requires:       %{name}-libgbm%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       opencl-filesystem
%description libOpenCL
%{summary}.

%package libOpenCL-devel
Summary:        Mesa OpenCL development package
Requires:       %{name}-libOpenCL%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description libOpenCL-devel
%{summary}.
%endif

%if 0%{?with_teflon}
%package libTeflon
Summary:        Mesa TensorFlow Lite delegate
%description libTeflon
%{summary}.
%endif

%if 0%{?with_d3d12}
%package dxil-devel
Summary:        Mesa SPIR-V to DXIL binary
Requires:       %{name}-filesystem%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description dxil-devel
Development tools for translating SPIR-V shader code to DXIL for Direct3D 12
%endif

%package vulkan-drivers
Summary:        Mesa Vulkan drivers
Requires:       vulkan%{_isa}
Requires:       %{name}-filesystem%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-vulkan-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      VK_hdr_layer < 1
%description vulkan-drivers
The drivers with support for the Vulkan API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{ver} -p1
cp %{SOURCE1} docs/
%if 0%{?vendor_nvk_crates}
mkdir subprojects/packagecache/
tar -xvf %{SOURCE10} -C subprojects/packagecache/
tar -xvf %{SOURCE11} -C subprojects/packagecache/
tar -xvf %{SOURCE12} -C subprojects/packagecache/
tar -xvf %{SOURCE13} -C subprojects/packagecache/
tar -xvf %{SOURCE14} -C subprojects/packagecache/
tar -xvf %{SOURCE15} -C subprojects/packagecache/
for d in subprojects/packagecache/*-*; do
echo '{"files":{}}' > $d/.cargo-checksum.json
done
%endif
%if 0%{?with_nvk}
cat > Cargo.toml <<_EOF
[package]
name = "mesa"
version = "%{ver}"
edition = "2021"
[lib]
path = "src/nouveau/nil/lib.rs"
[dependencies]
paste = "$(grep ^directory subprojects/paste*.wrap | sed 's|.*-||')"
syn = { version = "$(grep ^directory subprojects/syn*.wrap | sed 's|.*-||')", features = ["clone-impls"] }
rustc-hash = "$(grep ^directory subprojects/rustc-hash*.wrap | sed 's|.*-||')"
_EOF
%if 0%{?vendor_nvk_crates}
%else
%oreon_vendor_cargo
%build

export RUSTFLAGS="%build_rustflags"
%if 0%{?with_nvk}
%if !0%{?vendor_nvk_crates}
export MESON_PACKAGE_CACHE_DIR="%{cargo_registry}/"
%endif
rewrite_wrap_file() {
  sed -e "/source.*/d" -e "s/^directory = ${1}-.*/directory = $(basename ${MESON_PACKAGE_CACHE_DIR:-subprojects/packagecache}/${1}-*)/" -i subprojects/${1}*.wrap
}
rewrite_wrap_file proc-macro2
rewrite_wrap_file quote
rewrite_wrap_file syn
rewrite_wrap_file unicode-ident
rewrite_wrap_file paste
rewrite_wrap_file rustc-hash
%endif
%meson \
  -Dplatforms=x11,wayland \
%if 0%{?with_hardware}
  -Dgallium-drivers=llvmpipe,virgl,nouveau%{?with_r300:,r300}%{?with_crocus:,crocus}%{?with_i915:,i915}%{?with_iris:,iris}%{?with_vmware:,svga}%{?with_radeonsi:,radeonsi}%{?with_r600:,r600}%{?with_asahi:,asahi}%{?with_freedreno:,freedreno}%{?with_etnaviv:,etnaviv}%{?with_tegra:,tegra}%{?with_vc4:,vc4}%{?with_v3d:,v3d}%{?with_lima:,lima}%{?with_panfrost:,panfrost}%{?with_vulkan_hw:,zink}%{?with_d3d12:,d3d12}%{?with_teflon:,ethosu,rocket} \
%else
  -Dgallium-drivers=llvmpipe,virgl \
%endif
  -Dgallium-va=%{?with_va:enabled}%{!?with_va:disabled} \
  -Dgallium-mediafoundation=disabled \
  -Dteflon=%{?with_teflon:true}%{!?with_teflon:false} \
%if 0%{?with_opencl}
  -Dgallium-rusticl=true \
%endif
  -Dvulkan-drivers=%{?vulkan_drivers} \
  -Dvulkan-layers=device-select,anti-lag \
  -Dgles1=enabled \
  -Dgles2=enabled \
  -Dopengl=true \
  -Dgbm=enabled \
  -Dglx=dri \
  -Degl=enabled \
  -Dglvnd=enabled \
  -Dintel-rt=%{?with_intel_vk_rt:enabled}%{!?with_intel_vk_rt:disabled} \
  -Dmicrosoft-clc=disabled \
  -Dllvm=enabled \
  -Dshared-llvm=enabled \
  -Dvalgrind=%{?with_valgrind:enabled}%{!?with_valgrind:disabled} \
  -Dbuild-tests=false \
%if !0%{?with_libunwind}
  -Dlibunwind=disabled \
%endif
%if !0%{?with_lmsensors}
  -Dlmsensors=disabled \
%endif
  -Dandroid-libbacktrace=disabled \
%ifarch %{ix86}
  -Dglx-read-only-text=true \
%endif
  -Dspirv-tools=%{?with_spirv_tools:enabled}%{!?with_spirv_tools:disabled} \
  %{nil}
%meson_build
%if 0%{?with_nvk}
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?vendor_nvk_crates}
%cargo_vendor_manifest
%endif
%endif
%install
%meson_install
rm -vf %{buildroot}%{_libdir}/libGLX_mesa.so
rm -vf %{buildroot}%{_libdir}/libEGL_mesa.so
rm -vf %{buildroot}%{_libdir}/libGLES*
%if ! 0%{?with_asahi}
rm -vf %{buildroot}%{_libdir}/dri/apple_dri.so
%endif
ln -s %{_libdir}/libGLX_mesa.so.0 %{buildroot}%{_libdir}/libGLX_system.so.0
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mesa-filesystem -f %{oreon_filedir}/mesa-filesystem.list
%files -n mesa-libGL -f %{oreon_filedir}/mesa-libGL.list
%files -n mesa-libGL-devel -f %{oreon_filedir}/mesa-libGL-devel.list
%files -n mesa-libEGL -f %{oreon_filedir}/mesa-libEGL.list
%files -n mesa-libEGL-devel -f %{oreon_filedir}/mesa-libEGL-devel.list
%files -n mesa-dri-drivers -f %{oreon_filedir}/mesa-dri-drivers.list
%files -n mesa-libgbm -f %{oreon_filedir}/mesa-libgbm.list
%files -n mesa-libgbm-devel -f %{oreon_filedir}/mesa-libgbm-devel.list
%files -n mesa-libOpenCL -f %{oreon_filedir}/mesa-libOpenCL.list
%files -n mesa-libOpenCL-devel -f %{oreon_filedir}/mesa-libOpenCL-devel.list
%files -n mesa-vulkan-drivers -f %{oreon_filedir}/mesa-vulkan-drivers.list

%changelog

%autochangelog
%endif
%endif
