%global source22_hash bb73693c5d000dcf610912cde4e4a0b3a09677d82d3fef46d75b9e25a7770177
%global source15_hash 6636f56dc9460ad9d2db355ab6f2126a52ea4740670ade4d93770ecf19c06b8c
%global source14_hash 15dacc4a625c90f790c199ebb06e3327baee2f4a2163e1ee13643b0d8c29ac37
%global source0_hash 15dacc4a625c90f790c199ebb06e3327baee2f4a2163e1ee13643b0d8c29ac37
%define _lto_cflags %{nil}
%global _default_patch_fuzz 2
%global system_build_flags 0
%global numjobs %{_smp_build_ncpus}
%global official_build 1
%global use_custom_libcxx 0
%global bootstrap 0
%global build_target() \
	export NINJA_STATUS="[%2:%f/%t] " ; \
	ninja -j %{numjobs} -C '%1' '%2'
%global build_chromedriver 1
%if 0%{?flatpak}
%global build_chromedriver 0
%endif
%global build_headless 1
%if 0%{?flatpak}
%global build_headless 0
%endif
%global nodejs_version v22.22.0
%global system_nodejs 1
%global gtk_version 4
%global chromium_pybin %{__python3}
%global use_vaapi 1
%global use_v4l2_codec 0
%ifarch aarch64
%endif
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global noopenh264 1
%endif
%global disable_bti 0
%ifarch aarch64
%endif
%ifarch aarch64
%global chromium_arch arm64
%endif
%ifarch ppc64le
%global chromium_arch ppc64
%endif
%ifarch x86_64
%global chromium_arch x64
%endif
%global chromebuilddir out/Release_GN_%{chromium_arch}
%global enable_debug 1
%if ! %{enable_debug}
%global debug_package %{nil}
%global debug_level 0
%else
%global debug_level 1
%undefine _debugsource_packages
%endif
%global chromium_path %{_libdir}/cef
%global cef_wrapper_src_path %{_usrsrc}/%{name}-%{cef_version}
%global __provides_exclude_from ^(%{chromium_path}/.*\\.so|%{chromium_path}/.*\\.so.*)$
%global __requires_exclude ^(%{chromium_path}/.*\\.so|%{chromium_path}/.*\\.so.*)$
%global cfi 0
%ifarch x86_64 aarch64
%global cfi 1
%endif
%global use_qt6 0
%global use_qt5 0
%global bundlere2 1
%global bundlejsoncpp 1
%global bundlewoff2 1
%global bundlelibaom 1
%global bundlelibavif 1
%global bundlesnappy 1
%global bundlezstd 1
%global bundleicu 1
%global bundledav1d 1
%global bundlebrotli 1
%global bundlelibwebp 1
%global bundlecrc32c 1
%global bundleharfbuzz 1
%global bundlelibpng 1
%global bundlelibjpeg 1
%global bundlefreetype 1
%global bundlelibdrm 1
%global bundlefontconfig 1
%global bundleffmpegfree 1
%global bundlehighway 1
%global bundlelibopenjpeg2 1
%global bundlelibtiff 1
%global bundlelibxml 1
%global bundlepylibs 0
%global bundlelibxslt 0
%global bundleflac 0
%global bundledoubleconversion 0
%global bundlelibXNVCtrl 0
%global bundlelibusbx 0
%global bundlelibsecret 0
%global bundleopus 0
%global bundlelcms2 0
%global bundlesimdutf 1
%global bundleminizip 1
%global chromium_major 145
%global chromium_branch 7632
%global chromium_minor 159
%global chromium_version %{chromium_major}.0.%{chromium_branch}.%{chromium_minor}
%global cef_commit 51162e83c6f21779c0a3bc110589aff9ead2af33
%global cef_branch %{chromium_branch}
%global cef_minor 0
%global cef_patch 28
%global cef_version %{chromium_major}.%{cef_minor}.%{cef_patch}
%global shortcommit %(c=%{cef_commit}; echo ${c:0:7})
Name:	cef
Version: %{cef_version}^chromium%{chromium_version}
Release:        1%{?dist}
Summary:        Chromium Embedded Framework
Url: https://bitbucket.org/chromiumembedded/cef
License: BSD-3-Clause AND LGPL-2.1-or-later AND Apache-2.0 AND IJG AND MIT AND GPL-2.0-or-later AND ISC AND OpenSSL AND (MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-only)
Provides: cef(abi) = %{cef_version}
Patch1: chromium-115-initial_prefs-etc-path.patch
Patch8: chromium-117-widevine-other-locations.patch
Patch20: chromium-disable-font-tests.patch
Patch21: chromium-123-screen-ai-service.patch
Patch22: chromium-131-fix-qt-ui.pach
Patch23: chromium-143-revert-libpng_for_testonly.patch
Patch30: chromium-143-autodarkmode-workaround.patch
Patch31: chromium-145-disable-enterprise_companion_integration_tests.patch
Patch82: chromium-98.0.4758.102-remoting-no-tests.patch
Patch89: chromium-142-system-brotli.patch
Patch90: chromium-121-system-libxml.patch
Patch91: chromium-108-system-opus.patch
Patch92: chromium-138-checkversion-nodejs.patch
Patch93: chromium-141-csss_style_sheet.patch
Patch96: chromium-142-crabbyavif-ftbfs-old-rust.patch
Patch97: chromium-141-glibc-2.42-SYS_SECCOMP.patch
Patch128: chromium-138-el9-ffmpeg-deprecated-apis.patch
Patch129: chromium-el9-ffmpeg-AV_CODEC_FLAG_COPY_OPAQUE.patch
Patch130: chromium-142-el9-ffmpeg-5.x-duration.patch
Patch131: chromium-107-proprietary-codecs.patch
Patch132: chromium-118-sigtrap_system_ffmpeg.patch
Patch133: chromium-142-el9-ffmpeg-5.1.x.patch
Patch135: chromium-133-disable-H.264-video-parser-during-demuxing.patch
Patch136: chromium-133-workaround-system-ffmpeg-whitelist.patch
Patch141: chromium-118-dma_buf_export_sync_file-conflict.patch
Patch142: chromium-143-python-3.9-ftbfs.patch
Patch143: chromium-145-rust-1.88-enable-unstable_features.patch
Patch144: chromium-145-rust-1.88-undefined-symbol.patch
Patch150: chromium-124-qt6.patch
Patch300: chromium-145-swiftshader-missing-include.patch
Patch301: chromium-145-rustc-enable-nightly.patch
Patch302: chromium-145-static_assert.patch
Patch305: chromium-124-el8-arm64-memory_tagging.patch
Patch306: chromium-127-el8-ifunc-header.patch
Patch307: chromium-134-el8-atk-compiler-error.patch
Patch308: chromium-136-unsupport-clang-flags.patch
Patch309: chromium-132-el8-unsupport-rustc-flags.patch
Patch310: chromium-139-rust-FTBFS-suppress-warnings.patch
Patch311: chromium-123-fstack-protector-strong.patch
Patch312: chromium-143-el9-rust-no-alloc-shim-is-unstable.patch
Patch313: chromium-143-el9-rust_alloc_error_handler_should_panic.patch
Patch314: chromium-136-rust-skrifa-build-error.patch
Patch315: chromium-145-rustc-ftbfs.patch
Patch316: chromium-122-clang-build-flags.patch
Patch317: chromium-142-clang++-unknown-argument.patch
Patch318: memory-allocator-dcheck-assert-fix.patch
Patch319: chromium-143-swiftshader-llvm-16.0.patch
Patch352: chromium-117-workaround_for_crash_on_BTI_capable_system.patch
Patch353: chromium-127-aarch64-duplicate-case-value.patch
Patch354: chromium-142-split-threshold-for-reg-with-hint.patch
Patch355: chromium-130-hardware_destructive_interference_size.patch
Patch356: chromium-141-use_libcxx_modules.patch
Patch357: chromium-134-type-mismatch-error.patch
Patch358: chromium-144-rust-clanglib.patch
Patch359: add-ppc64-architecture-string.patch
Patch361: 0001-sandbox-Enable-seccomp_bpf-for-ppc64.patch
Patch376: 0001-third_party-angle-Include-missing-header-cstddef-in-.patch
Patch377: 0001-Add-PPC64-support-for-boringssl.patch
Patch378: 0001-third_party-libvpx-Properly-generate-gni-on-ppc64.patch
Patch380: 0001-third_party-pffft-Include-altivec.h-on-ppc64-with-SI.patch
Patch381: 0002-Add-PPC64-generated-files-for-boringssl.patch
Patch382: 0002-third_party-lss-kernel-structs.patch
Patch383: 0001-swiftshader-fix-build.patch
Patch384: Rtc_base-system-arch.h-PPC.patch
Patch386: 0004-third_party-crashpad-port-curl-transport-ppc64.patch
Patch387: HACK-third_party-libvpx-use-generic-gnu.patch
Patch389: HACK-debian-clang-disable-base-musttail.patch
Patch390: HACK-debian-clang-disable-pa-musttail.patch
Patch391: 0001-Add-ppc64-target-to-libaom.patch
Patch392: 0001-Add-pregenerated-config-for-libaom-on-ppc64.patch
Patch393: 0002-third_party-libvpx-Remove-bad-ppc64-config.patch
Patch394: 0003-third_party-libvpx-Add-ppc64-generated-config.patch
Patch395: 0004-third_party-libvpx-work-around-ambiguous-vsx.patch
Patch396: skia-vsx-instructions.patch
Patch397: 0001-Implement-support-for-ppc64-on-Linux.patch
Patch398: 0001-Implement-support-for-PPC64-on-Linux.patch
Patch399: 0001-Force-baseline-POWER8-AltiVec-VSX-CPU-features-when-.patch
Patch401: fix-rustc.patch
Patch402: fix-rust-linking.patch
Patch403: fix-breakpad-compile.patch
Patch404: fix-partition-alloc-compile.patch
Patch405: fix-study-crash.patch
Patch407: fix-different-data-layouts.patch
Patch408: 0002-Add-ppc64-trap-instructions.patch
Patch409: fix-page-allocator-overflow.patch
Patch410: 0001-Enable-ppc64-pointer-compression.patch
Patch411: dawn-fix-ppc64le-detection.patch
Patch412: add-ppc64-architecture-to-extensions.diff
Patch413: fix-unknown-warning-option-messages.diff
Patch415: add-ppc64-pthread-stack-size.patch
Patch417: 0001-add-xnn-ppc64el-support.patch
Patch418: 0002-regenerate-xnn-buildgn.patch
Patch419: 0009-sandbox-ignore-byte-span-error.patch
Patch500: flatpak-Add-initial-sandbox-support.patch
Patch501: flatpak-Adjust-paths-for-the-sandbox.patch
Patch502: flatpak-Expose-Widevine-into-the-sandbox.patch
%if ! %{system_nodejs}
Patch510: 0001-Remove-unused-OpenSSL-config.patch
Patch511: 0001-fips-disable-options.patch
%endif
Patch900: cef-no-sysroot.patch
Patch901: cef-no-libxml-visibility-patch.patch
Source0:        chromium-%{chromium_version}-clean.tar.xz
Source1: README.fedora
Source5: clean_ffmpeg.sh
Source6: chromium-latest.py
Source7: get_free_ffmpeg_source_files.py
%if ! %{system_nodejs}
Source12: node-%{nodejs_version}-stripped.tar.gz
Source13: nodejs-sources.sh
%endif
Source14: https://npm.skia.org/chrome-devtools/@rollup%2frollup-linux-arm64-gnu/-/rollup-linux-arm64-gnu-4.22.4.tgz
Source15: https://npm.skia.org/chrome-devtools/@rollup%2frollup-linux-powerpc64le-gnu/-/rollup-linux-powerpc64le-gnu-4.22.4.tgz
Source22: https://github.com/chromiumembedded/cef/archive/%{cef_commit}.tar.gz
Source23: mkspec.sh
Source24: FindCEF.cmake
%if ! %{use_custom_libcxx}
%endif
%if ! %{bundlezstd}
%endif
%if ! %{bundleffmpegfree}
%endif
%if 0%{?noopenh264}
%endif
%if ! %{bundlelibaom}
%endif
%if ! %{bundleharfbuzz}
%endif
%if ! %{bundlelibdrm}
%endif
%if 0%{?fedora} >= 37 || 0%{?rhel} > 9 || 0%{?oreon} >= 11
%else
%endif
%if ! %{bundleminizip}
%endif
%if ! %{bootstrap}
%endif
%if ! %{bundleflac}
%endif
%if ! %{bundlefreetype}
%endif
%if ! %{bundlecrc32c}
%endif
%if ! %{bundlewoff2}
%endif
%if ! %{bundledav1d}
%endif
%if ! %{bundlehighway}
%endif
%if ! %{bundlelibavif}
%endif
%if ! %{bundlejsoncpp}
%endif
%if ! %{bundlelibsecret}
%endif
%if ! %{bundledoubleconversion}
%endif
%if ! %{bundlesnappy}
%endif
%if ! %{bundlelibXNVCtrl}
%endif
%if ! %{bundleicu}
%endif
%if ! %{bundlelibjpeg}
%endif
%if ! %{bundlelibpng}
%endif
%if ! %{bundlelibopenjpeg2}
%endif
%if ! %{bundlelcms2}
%endif
%if ! %{bundlelibtiff}
%endif
%if ! %{bundlelibusbx}
Requires: libusbx >= 1.0.21-0.1.git448584a
%endif
%if ! %{bundlelibwebp}
%endif
%if ! %{bundlelibxslt}
%endif
%if ! %{bundleopus}
%endif
%if %{gtk_version} == 4
%endif
%if ! %{bundlepylibs}
%endif
%if ! %{bundlere2}
Requires: re2 >= 20160401
%endif
%if ! %{bundlebrotli}
%endif
%if ! %{bundlesimdutf}
%endif
Requires: nss%{_isa} >= 3.26
Requires: nss-mdns%{_isa}
ExclusiveArch: x86_64 aarch64
Provides: bundled(bintrees) = 1.0.1
Provides: bundled(boringssl)
Provides: bundled(simdutf) = 7.0.0
Provides: bundled(bspatch) = 465265d0d473d107b76e74d969199eaf2cdc8750
Provides: bundled(colorama) = 0.4.6
Provides: bundled(crashpad) = 8f131016b21d986c38ca4a0f091403dbb822d636
Provides: bundled(expat) = 2.7.1
Provides: bundled(fdmlibm) = c512d6173f33c6b8301d3fba9384edc9fc1f9e45
Provides: bundled(libaom) = 3.12.1
Provides: bundled(hunspell) = 6d7d19f
Provides: bundled(icu) = 74-2
Provides: bundled(leveldb) = 1.23
Provides: bundled(libaddressinput) = 2610f7b104
Provides: bundled(libjingle) = 5493b8a59deb16cf0481e24707a0ed72d19047dc
Provides: bundled(libphonenumber) = 140dfeb81b753388e8a672900fb7a971e9a0d362
Provides: bundled(libsrtp) = fd08747fa6800b321d53e15feb34da12dc697dee
Provides: bundled(libvpx) = 1.6.0
Provides: bundled(libxml) = 2.14.2
Provides: bundled(libyuv) = 1909
Provides: bundled(lzma) = 24.09
Provides: bundled(ots) = 8d70cffebbfa58f67a5c3ed0e9bc84dccdbc5bc0
Provides: bundled(protobuf) = 3.0.0.beta.3
Provides: bundled(qcms) = 4
Provides: bundled(re2)
Provides: bundled(sfntly) = 04740d2600193b14aa3ef24cd9fbb3d5996b9f77
Provides: bundled(skia)
Provides: bundled(SMHasher) = 0
Provides: bundled(snappy) = 1.1.4-head
Provides: bundled(speech-dispatcher) = 0.7.1
Provides: bundled(sqlite) = 3.17patched
Provides: bundled(superfasthash) = 0
Provides: bundled(talloc) = 2.0.1
Provides: bundled(usrsctp) = 0
Provides: bundled(v8) = 5.9.211.31
Provides: bundled(webrtc) = 90usrsctp
Provides: bundled(woff2) = 445f541996fe8376f3976d35692fd2b9a6eedf2d
Provides: bundled(xdg-mime)
Provides: bundled(xdg-user-dirs)
%if %{undefined flatpak}
Requires(post): /usr/sbin/semanage
Requires(post): /usr/sbin/restorecon
%endif
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  /usr/bin/python3
BuildRequires:  alsa-lib-devel
BuildRequires:  atk-devel
BuildRequires:  bindgen-cli
BuildRequires:  bison
BuildRequires:  brotli-devel
BuildRequires:  bzip2-devel
BuildRequires:  clang
BuildRequires:  clang-tools-extra
BuildRequires:  compiler-rt
BuildRequires:  cups-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  double-conversion-devel
BuildRequires:  elfutils
BuildRequires:  elfutils-libelf-devel
BuildRequires:  expat-devel
BuildRequires:  flac-devel
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel
BuildRequires:  gn
BuildRequires:  golang-github-evanw-esbuild
BuildRequires:  google-crc32c-devel
BuildRequires:  gperf
BuildRequires:  harfbuzz-devel
BuildRequires:  hwdata
BuildRequires:  java-openjdk-headless
BuildRequires:  jq
BuildRequires:  kernel-headers
BuildRequires:  lcms2-devel
BuildRequires:  libXNVCtrl-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXtst-devel
BuildRequires:  libappstream-glib
BuildRequires:  libatomic
BuildRequires:  libcap-devel
BuildRequires:  libcurl-devel
BuildRequires:  libcxx-devel
BuildRequires:  libdav1d-devel
BuildRequires:  libdrm-devel
BuildRequires:  libevdev-devel
BuildRequires:  libffi-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libsecret-devel
BuildRequires:  libtiff-devel
BuildRequires:  libudev-devel
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  libusbx-devel
BuildRequires:  libutempter-devel
BuildRequires:  libuuid-devel
BuildRequires:  libva-devel
BuildRequires:  libwebp-devel
BuildRequires:  libxshmfence-devel
BuildRequires:  libxslt-devel
BuildRequires:  libzstd-devel
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  ninja-build
BuildRequires:  nodejs
BuildRequires:  nss-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  opus-devel
BuildRequires:  pam-devel
BuildRequires:  pciutils-devel
BuildRequires:  pipewire-devel
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-jinja2
BuildRequires:  rustc
BuildRequires:  rustfmt
BuildRequires:  speech-dispatcher-devel
BuildRequires:  systemd
BuildRequires:  wayland-devel
BuildRequires:  xcb-proto
BuildRequires:  zlib-devel
# /oreon:deps
%description
CEF is an embeddable build of Chromium, powered by WebKit (Blink).

%package devel
Summary: Header files for the Chromium Embedded Framework
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files for the Chromium Embedded Framework.
## END CEF

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

## CEF: Unpack and move CEF/chromium sources into the expected layout
%setup -q -T -n cef-%{cef_commit} -b 22
%setup -q -n chromium-%{chromium_version}
mv %{_builddir}/cef-%{cef_commit} ./cef
## END CEF

### Chromium Fedora Patches ###
%patch -P1 -p1 -b .etc
%patch -P8 -p1 -b .widevine-other-locations

%patch -P20 -p1 -b .disable-font-test
%patch -P21 -p1 -b .screen-ai-service
%if ! %{use_custom_libcxx}
%patch -P22 -p1 -b .fix-qt-ui
%endif

%patch -P23 -p1 -R -b .revert-libpng_for_testonly
%patch -P30 -p1 -b .autodarkmode-workaround
%patch -P31 -p1 -b .disable-enterprise_companion_integration_tests
%patch -P82 -p1 -b .remoting-no-tests

%if ! %{bundlebrotli}
%patch -P89 -p1 -b .system-brotli
%endif

%if ! %{bundlelibxml}
%endif

%if ! %{bundleopus}
%patch -P91 -p1 -b .system-opus
%endif

%patch -P92 -p1 -b .nodejs-checkversion
%patch -P93 -p1 -b .ftbfs-csss_style_sheet
%patch -P96 -p1 -b .crabbyavif-ftbfs-old-rust

%if ! %{bundleffmpegfree}
%patch -P131 -p1 -b .prop-codecs
%patch -P132 -p1 -b .sigtrap_system_ffmpeg
%patch -P135 -p1 -b .disable-H.264-video-parser-during-demuxing
%patch -P136 -p1 -b .workaround-system-ffmpeg-whitelist
%endif

%patch -P150 -p1 -b .qt6

%patch -P300 -p1 -b .swiftshader-missing-include
%patch -P301 -p1 -b .rustc-enable-nightly

# llvm version < 21 on f42/el9/epel10.1

%patch -P307 -p1 -b .el8-atk-compiler-error
%patch -P308 -p1 -b .unsupport-clang-flags
%patch -P309 -p1 -b .el8-unsupport-rustc-flags
%patch -P314 -p1 -b .rust-skrifa-build-error
%patch -P315 -p1 -b .rustc-ftbfs
%patch -P310 -p1 -b .rust-FTBFS-suppress-warnings
%patch -P311 -p1 -b .fstack-protector-strong

%patch -P316 -p1 -b .clang-build-flags

%patch -P318 -p1 -b .memory-allocator-dcheck-assert-fix
%patch -P319 -p1 -b .swiftshader-llvm-16.0

%patch -P352 -p1 -b .workaround_for_crash_on_BTI_capable_system

%ifarch aarch64 && 0%{?fedora} > 40
%patch -P353 -p1 -b .duplicate-case-value
%endif

%patch -P355 -p1 -b .hardware_destructive_interference_size

%patch -P356 -p1 -b .disable_use_libcxx_modules

%patch -P357 -p1 -b .type-mismatch-error

%patch -P358 -p1 -b .rust-clang_lib

%ifarch ppc64le
%patch -P359 -p1 -b .add-ppc64-architecture-string
%patch -P361 -p1 -b .0001-sandbox-Enable-seccomp_bpf-for-ppc64
%patch -P376 -p1 -b .0001-third_party-angle-Include-missing-header-cstddef-in-
%patch -P377 -p1 -b .0001-Add-PPC64-support-for-boringssl
%patch -P378 -p1 -b .0001-third_party-libvpx-Properly-generate-gni-on-ppc64
%patch -P380 -p1 -b .0001-third_party-pffft-Include-altivec.h-on-ppc64-with-SI
%patch -P381 -p1 -b .0002-Add-PPC64-generated-files-for-boringssl
%patch -P382 -p1 -b .0002-third_party-lss-kernel-structs
%patch -P383 -p1 -b .0001-swiftshader-fix-build
%patch -P384 -p1 -b .Rtc_base-system-arch.h-PPC
%patch -P386 -p1 -b .0004-third_party-crashpad-port-curl-transport-ppc64
%patch -P387 -p1 -b .HACK-third_party-libvpx-use-generic-gnu
%patch -P389 -p1 -b .HACK-debian-clang-disable-base-musttail
%patch -P390 -p1 -b .HACK-debian-clang-disable-pa-musttail
%patch -P391 -p1 -b .0001-Add-ppc64-target-to-libaom
%patch -P392 -p1 -b .0001-Add-pregenerated-config-for-libaom-on-ppc64
%patch -P393 -p1 -b .0002-third_party-libvpx-Remove-bad-ppc64-config
%patch -P394 -p1 -b .0003-third_party-libvpx-Add-ppc64-generated-config
%patch -P395 -p1 -b .0004-third_party-libvpx-work-around-ambiguous-vsx
%patch -P396 -p1 -b .skia-vsx-instructions
%patch -P397 -p1 -b .0001-Implement-support-for-ppc64-on-Linux
%patch -P398 -p1 -b .0001-Implement-support-for-PPC64-on-Linux
%patch -P399 -p1 -b .0001-Force-baseline-POWER8-AltiVec-VSX-CPU-features-when-
%patch -P401 -p1 -b .fix-rustc
%patch -P402 -p1 -b .fix-rust-linking
%patch -P403 -p1 -b .fix-breakpad-compile
%patch -P404 -p1 -b .fix-partition-alloc-compile
%patch -P405 -p1 -b .fix-study-crash
%patch -P407 -p1 -b .fix-different-data-layouts
%patch -P408 -p1 -b .0002-Add-ppc64-trap-instructions
%patch -P409 -p1 -b .fix-page-allocator-overflow
%patch -P410 -p1 -b .0001-Enable-ppc64-pointer-compression
%patch -P411 -p1 -b .dawn-fix-ppc64le-detection
%patch -P412 -p1 -b .add-ppc64-architecture-to-extensions
%patch -P413 -p1 -b .fix-unknown-warning-option-messages
%patch -P415 -p1 -b .add-ppc64-pthread-stack-size
%patch -P417 -p1 -b .0001-add-xnn-ppc64el-support
%patch -P418 -p1 -b .0002-regenerate-xnn-buildgn
%patch -P419 -p1 -b .0009-sandbox-ignore-byte-span-error
%endif

%if 0%{?flatpak}
%patch -P500 -p1 -b .flatpak-initial-sandbox
%patch -P501 -p1 -b .flatpak-sandbox-paths
%patch -P502 -p1 -b .flatpak-widevine
%endif

# Upstream patches

## CEF: CEF-specific fix patches & other fixup
%patch -P900 -p1 -b .cef-no-sysroot
%if ! %{bundlelibxml}
%patch -P901 -p1 -b .cef-no-libxml-visibility-patch
%endif

# Redirect the git version stuff to use the version file contents instead
cat >>cef/VERSION.in <<EOF
HASH=%{cef_commit}
MINOR=%{cef_minor}
PATCH=%{cef_patch}
EOF
cat > cef/.git-version <<EOF
COMMIT_HASH=%{cef_commit}
URL=https://bitbucket.org/chromiumembedded/cef
EOF
cat > .git-version <<EOF
COMMIT_HASH=refs/tags/%{chromium_version}
URL=https://chromium.googlesource.com/chromium/src.git
EOF
sed -i -e 's/\.get_cef_commit_components/.get_cef_version_components/g' \
  -e 's/\.get_cef_branch_version_components/.get_cef_version_components/g' \
  -e 's/if not on_release_branch/if False/g' \
  -e 's/%d/%s/g' \
  cef/tools/cef_version.py

# Use system clang
echo 'clang_exe = "clang"' >> cef/tools/clang_util.py

# Mock the git functions
cat <<EOF >>cef/tools/git_util.py
import subprocess

def git_apply_patch_file(patch_path, patch_dir):
    try:
        subprocess.run(["patch", "-p0", "--ignore-whitespace",
                        "-N", "-i", patch_path], cwd=patch_dir, check=True)
    except subprocess.CalledProcessError:
        return "fail"
    return "apply"

def ver_info(path):
    info = {}
    for line in open(os.path.join(path, '.git-version')):
        key, val = line.strip().split("=")
        info[key] = val
    return info

def is_checkout(path):
    return os.path.exists(os.path.join(path, '.git-version'))

def get_hash(path='.', branch='HEAD'):
    return ver_info(path)["COMMIT_HASH"]

def get_url(path):
    return ver_info(path)["URL"]

def get_commit_number(path='.', branch='HEAD'):
    return 0
EOF
## END CEF

# Change shebang in all relevant files in this directory and all subdirectories
# See `man find` for how the `-exec command {} +` syntax works
find -type f \( -iname "*.py" \) -exec sed -i '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{chromium_pybin}=' {} +

# unpack rollup binary for aarch64
%ifarch aarch64
tar xf %{SOURCE14} && mv package third_party/devtools-frontend/src/node_modules/@rollup/rollup-linux-arm64-gnu
%endif

#unpack rollup binary for ppc64le
%ifarch ppc64le
tar xf %{SOURCE15} && mv package third_party/devtools-frontend/src/node_modules/@rollup/rollup-linux-powerpc64le-gnu
%endif 

# Add correct path for nodejs binary
mkdir -p third_party/node/linux/node-linux-x64/bin
%if ! %{system_nodejs}
  ln -s ../../../../../node-%{nodejs_version}/node third_party/node/linux/node-linux-x64/bin/node
%else
  ln -s $(which node) third_party/node/linux/node-linux-x64/bin/node
%endif

# Add correct path for esbuild binary
mkdir -p third_party/devtools-frontend/src/third_party/esbuild
ln -s $(which esbuild) third_party/devtools-frontend/src/third_party/esbuild/esbuild

# Remove bundle gn and replace it with a system gn or bootstrap gn as it is x86_64 and causes
# FTBFS on other arch like aarch64/ppc64le
ln -sf ../../%{chromebuilddir}/gn buildtools/linux64/gn

# hackity hack hack
rm -rf third_party/libusb/src/libusb/libusb.h
# we _shouldn't need to do this, but it looks like we do.
cp -a $(pkg-config --variable=includedir libusb-1.0)/libusb-1.0/libusb.h third_party/libusb/src/libusb/libusb.h

# Hard code extra version
sed -i 's/getenv("CHROME_VERSION_EXTRA")/"Fedora Project"/' chrome/common/channel_info_posix.cc

# Fix hardcoded path in remoting code
sed -i 's|/opt/google/chrome-remote-desktop|%{crd_path}|g' remoting/host/setup/daemon_controller_delegate_linux.cc

# bz#2265957, add correct platform
sed -i "s/Linux x86_64/Linux %{_arch}/" components/embedder_support/user_agent_utils.cc

%if ! %{bundlesimdutf}
ln -sf %{_includedir}/simdutf.h third_party/simdutf/simdutf.h
%endif

%build

%if ! %{system_nodejs}
export CXX=c++
tar xf %{SOURCE12}
pushd node-%{nodejs_version}
patch -p1 < %{_sourcedir}/0001-Remove-unused-OpenSSL-config.patch
patch -p1 < %{_sourcedir}/0001-fips-disable-options.patch
./configure --ninja --shared-openssl --openssl-is-fips --openssl-conf-name=openssl_conf --enable-static --prefix=node-%{nodejs_version}-linux-x64
ninja -j %{numjobs} -C %{chromebuilddir}
make install
popd
%endif
FLAGS=' -Wno-deprecated-declarations -Wno-unknown-warning-option -Wno-unused-command-line-argument'
FLAGS+=' -Wno-unused-but-set-variable -Wno-unused-result -Wno-unused-function -Wno-unused-variable'
FLAGS+=' -Wno-unused-const-variable -Wno-unneeded-internal-declaration -Wno-unknown-attributes -Wno-unknown-pragmas'
CFLAGS="$FLAGS"
CXXFLAGS="$FLAGS"
%ifarch ppc64le
CXXFLAGS+=' -faltivec-src-compat=mixed -Wno-deprecated-altivec-src-compat'
%endif
%if ! %{use_custom_libcxx}
LDFLAGS="${LDFLAGS} -stdlib=libc++"
CXXFLAGS="${CXXFLAGS} -stdlib=libc++"
%endif
export CC=clang
export CXX=clang++
export AR=llvm-ar
export NM=llvm-nm
export READELF=llvm-readelf
export CFLAGS
export CXXFLAGS
export LDFLAGS
export RUSTC_BOOTSTRAP=1
rustc_version="$(rustc --version)"
rust_bindgen_root="$(which bindgen | sed 's#/s\?bin/.*##')"
rust_sysroot_absolute="$(rustc --print sysroot)"
clang_version="$(clang --version | sed -n 's/clang version //p' | cut -d. -f1)"
clang_base_path="$(clang --version | grep InstalledDir | cut -d' ' -f2 | sed 's#/bin##')"
CHROMIUM_CORE_GN_DEFINES=""
CHROMIUM_CORE_GN_DEFINES+=' custom_toolchain="//build/toolchain/linux/unbundle:default"'
CHROMIUM_CORE_GN_DEFINES+=' host_toolchain="//build/toolchain/linux/unbundle:default"'
%if ! %{use_custom_libcxx}
CHROMIUM_BROWSER_GN_DEFINES+=' use_custom_libcxx=false'
%endif
CHROMIUM_CORE_GN_DEFINES+=' is_debug=false dcheck_always_on=false dcheck_is_configurable=false'
CHROMIUM_CORE_GN_DEFINES+=' enable_enterprise_companion=false'
CHROMIUM_CORE_GN_DEFINES+=' system_libdir="%{_lib}"'
CHROMIUM_CORE_GN_DEFINES+=' is_official_build=true'
sed -i 's|OFFICIAL_BUILD|GOOGLE_CHROME_BUILD|g' tools/generate_shim_headers/generate_shim_headers.py
CHROMIUM_CORE_GN_DEFINES+=' chrome_pgo_phase=0'
%if ! %{cfi}
CHROMIUM_CORE_GN_DEFINES+=' is_cfi=false use_thin_lto=false'
%endif
CHROMIUM_CORE_GN_DEFINES+=' is_clang=true'
CHROMIUM_CORE_GN_DEFINES+=" clang_base_path=\"$clang_base_path\""
CHROMIUM_CORE_GN_DEFINES+=" clang_version=$clang_version"
CHROMIUM_CORE_GN_DEFINES+=' clang_use_chrome_plugins=false'
CHROMIUM_CORE_GN_DEFINES+=' use_lld=true'
CHROMIUM_CORE_GN_DEFINES+=" rust_sysroot_absolute=\"$rust_sysroot_absolute\""
CHROMIUM_CORE_GN_DEFINES+=" rust_bindgen_root=\"$rust_bindgen_root\""
CHROMIUM_CORE_GN_DEFINES+=" rustc_version=\"$rustc_version\""
CHROMIUM_CORE_GN_DEFINES+=' use_sysroot=false'
%ifarch aarch64
CHROMIUM_CORE_GN_DEFINES+=' target_cpu="arm64"'
%endif
%ifarch ppc64le
CHROMIUM_CORE_GN_DEFINES+=' target_cpu="ppc64"'
%endif
CHROMIUM_CORE_GN_DEFINES+=' icu_use_data_file=true'
CHROMIUM_CORE_GN_DEFINES+=' target_os="linux"'
CHROMIUM_CORE_GN_DEFINES+=' current_os="linux"'
CHROMIUM_CORE_GN_DEFINES+=' treat_warnings_as_errors=false'
CHROMIUM_CORE_GN_DEFINES+=' enable_iterator_debugging=false'
CHROMIUM_CORE_GN_DEFINES+=' enable_vr=false'
CHROMIUM_CORE_GN_DEFINES+=' build_dawn_tests=false enable_perfetto_unittests=false'
CHROMIUM_CORE_GN_DEFINES+=' disable_fieldtrial_testing_config=true'
CHROMIUM_CORE_GN_DEFINES+=' symbol_level=0 blink_symbol_level=0'
CHROMIUM_CORE_GN_DEFINES+=' angle_has_histograms=false'
CHROMIUM_CORE_GN_DEFINES+=' safe_browsing_use_unrar=false'
CHROMIUM_CORE_GN_DEFINES+=' v8_enable_backtrace=true'
CHROMIUM_CORE_GN_DEFINES+=' devtools_bundle=false'
export CHROMIUM_CORE_GN_DEFINES
CHROMIUM_BROWSER_GN_DEFINES=""
%if ! %{bundleffmpegfree}
CHROMIUM_BROWSER_GN_DEFINES+=' ffmpeg_branding="Chrome" proprietary_codecs=true is_component_ffmpeg=true enable_ffmpeg_video_decoders=true media_use_ffmpeg=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' ffmpeg_branding="Chromium" proprietary_codecs=false is_component_ffmpeg=false enable_ffmpeg_video_decoders=false media_use_ffmpeg=true'
%endif
%if 0%{?noopenh264}
CHROMIUM_BROWSER_GN_DEFINES+=' media_use_openh264=true'
CHROMIUM_BROWSER_GN_DEFINES+=' rtc_use_h264=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' media_use_openh264=false'
CHROMIUM_BROWSER_GN_DEFINES+=' rtc_use_h264=false'
%endif
CHROMIUM_BROWSER_GN_DEFINES+=' use_kerberos=true'
CHROMIUM_BROWSER_GN_DEFINES+=' rtc_video_psnr=false'
CHROMIUM_BROWSER_GN_DEFINES+=' use_qt5=false'
CHROMIUM_BROWSER_GN_DEFINES+=' use_qt6=false'
CHROMIUM_BROWSER_GN_DEFINES+=' use_gtk=true gtk_version=%{gtk_version}'
CHROMIUM_BROWSER_GN_DEFINES+=' use_gio=true use_pulseaudio=true'
CHROMIUM_BROWSER_GN_DEFINES+=' enable_hangout_services_extension=true'
CHROMIUM_BROWSER_GN_DEFINES+=' enable_widevine=true'
CHROMIUM_BROWSER_GN_DEFINES+=' use_vaapi=false'
CHROMIUM_BROWSER_GN_DEFINES+=' use_v4l2_codec=true'
CHROMIUM_BROWSER_GN_DEFINES+=' rtc_use_pipewire=false rtc_link_pipewire=false'
%if ! %{bundlelibjpeg}
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_libjpeg=true'
%endif
%if ! %{bundlelibpng}
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_libpng=true'
%endif
%if ! %{bundlelibopenjpeg2}
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_libopenjpeg2=true'
%endif
%if ! %{bundlelcms2}
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_lcms2=true'
%endif
%if ! %{bundlelibtiff}
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_libtiff=true'
%endif
CHROMIUM_BROWSER_GN_DEFINES+=' use_system_libffi=true'
export CHROMIUM_BROWSER_GN_DEFINES
CHROMIUM_HEADLESS_GN_DEFINES=""
CHROMIUM_HEADLESS_GN_DEFINES+=' use_ozone=true ozone_auto_platforms=false ozone_platform="headless" ozone_platform_headless=true'
CHROMIUM_HEADLESS_GN_DEFINES+=' angle_enable_vulkan=true angle_enable_swiftshader=true headless_use_embedded_resources=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' headless_use_prefs=false headless_use_policy=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' v8_use_external_startup_data=false enable_print_preview=false enable_remoting=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_alsa=false use_bluez=false use_cups=false use_dbus=false use_gio=false use_kerberos=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_libpci=false use_pulseaudio=false use_udev=false rtc_use_pipewire=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' v8_enable_lazy_source_positions=false use_glib=false use_gtk=false use_pangocairo=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_qt5=false use_qt6=false is_component_build=false enable_ffmpeg_video_decoders=false media_use_ffmpeg=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' media_use_libvpx=false proprietary_codecs=false'
export CHROMIUM_HEADLESS_GN_DEFINES
system_libs=()
%if ! %{bundlelibaom}
	system_libs+=(libaom)
%endif
%if ! %{bundlelibavif}
	system_libs+=(libavif)
%endif
%if ! %{bundlebrotli}
	system_libs+=(brotli)
%endif
%if ! %{bundlecrc32c}
	system_libs+=(crc32c)
%endif
%if ! %{bundledav1d}
	system_libs+=(dav1d)
%endif
%if ! %{bundlehighway}
	system_libs+=(highway)
%endif
%if ! %{bundlefontconfig}
	system_libs+=(fontconfig)
%endif
%if ! %{bundleffmpegfree}
	system_libs+=(ffmpeg)
%endif
%if ! %{bundlefreetype}
	system_libs+=(freetype)
%endif
%if ! %{bundleharfbuzz}
	system_libs+=(harfbuzz-ng)
%endif
%if ! %{bundleicu}
	system_libs+=(icu)
%endif
%if ! %{bundlelibdrm}
	system_libs+=(libdrm)
%endif
%if ! %{bundlelibjpeg}
	system_libs+=(libjpeg)
%endif
%if ! %{bundlelibpng}
	system_libs+=(libpng)
%endif
%if ! %{bundlelibusbx}
	system_libs+=(libusb)
%endif
%if ! %{bundlelibwebp}
	system_libs+=(libwebp)
%endif
%if ! %{bundlelibxml}
	system_libs+=(libxml)
%endif
%if ! %{bundlelibxslt}
	system_libs+=(libxslt)
%endif
%if ! %{bundleopus}
	system_libs+=(opus)
%endif
%if ! %{bundlere2}
	system_libs+=(re2)
%endif
%if ! %{bundlewoff2}
	system_libs+=(woff2)
%endif
%if ! %{bundleminizip}
	system_libs+=(zlib)
%endif
%if ! %{bundlejsoncpp}
	system_libs+=(jsoncpp)
%endif
%if ! %{bundledoubleconversion}
	system_libs+=(double-conversion)
%endif
%if ! %{bundlelibsecret}
	system_libs+=(libsecret)
%endif
%if ! %{bundlesnappy}
	system_libs+=(snappy)
%endif
%if ! %{bundlelibXNVCtrl}
	system_libs+=(libXNVCtrl)
%endif
%if ! %{bundleflac}
	system_libs+=(flac)
%endif
%if ! %{bundlezstd}
	system_libs+=(zstd)
%endif
%if 0%{?noopenh264}
	system_libs+=(openh264)
%endif
%if ! %{bundlesimdutf}
   system_libs+=(simdutf)
%endif
build/linux/unbundle/replace_gn_files.py --system-libraries ${system_libs[@]}
if python3 -c 'import google ; print google.__path__' 2> /dev/null ; then \
    echo "Python 3 'google' module is defined, this will shadow modules of this build"; \
    exit 1 ; \
fi
tools/gn/bootstrap/bootstrap.py --gn-gen-args="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES"
DEPOT_TOOLS=%{_builddir}/chromium-%{chromium_version}/third_party/depot_tools
rm -f ${DEPOT_TOOLS}/ninja
export PATH=$PATH:$DEPOT_TOOLS
CEF_GN_DEFINES=""
CEF_GN_DEFINES+=' use_gtk=false use_qt5=false use_qt6=false enable_remoting=false'
CEF_GN_DEFINES+=' use_cups=false use_gio=false use_kerberos=false'
CEF_GN_DEFINES+=' use_libpci=false use_udev=false'
CEF_GN_DEFINES+=' cef_use_gtk=false'
GN_DEFINES="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES $CEF_GN_DEFINES" \
GN_ARGUMENTS="--script-executable=%{chromium_pybin}" \
%{chromium_pybin} cef/tools/gclient_hook.py
%build_target %{chromebuilddir} libcef
%build_target %{chromebuilddir} chrome_sandbox
sh %SOURCE23 cef/cef_api_versions.json > %{specpartsdir}/cef-api-versions.specpart
python3 cef/tools/make_distrib.py --distrib-subdir=distrib --output-dir=.. --ninja-build --%{chromium_arch}-build --minimal --no-docs --no-archive
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{chromium_path}
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{cef_wrapper_src_path}
mkdir -p %{buildroot}%{_includedir}/cef
mkdir -p %{buildroot}%{_datadir}/cmake/Modules
pushd ../distrib_minimal/Resources
  cp -a *.pak locales %{buildroot}%{chromium_path}
  cp -a icudtl.dat %{buildroot}%{chromium_path}
popd
pushd ../distrib_minimal/Release
  cp -a libvk_swiftshader.so* %{buildroot}%{chromium_path}
  cp -a libvulkan.so* %{buildroot}%{chromium_path}
  cp -a vk_swiftshader_icd.json %{buildroot}%{chromium_path}
  cp -a libcef.so %{buildroot}%{chromium_path}
  cp -a chrome-sandbox %{buildroot}%{chromium_path}/chrome-sandbox
  cp -a v8_context_snapshot.bin %{buildroot}%{chromium_path}
  cp -a libEGL.so* libGLESv2.so* %{buildroot}%{chromium_path}
popd
cp -a ../distrib_minimal/include %{buildroot}%{_includedir}/cef/include
cp -a ../distrib_minimal/libcef_dll %{buildroot}%{cef_wrapper_src_path}/libcef_dll
sed -i -e '/\.\.\/include/d' %{buildroot}%{cef_wrapper_src_path}/libcef_dll/CMakeLists.txt
sed \
  -e "s,__CEF_INCLUDE__,%{_includedir}/cef," \
  -e "s,__CEF_LIB__,%{chromium_path}," \
  -e "s,__CEF_SRC__,%{cef_wrapper_src_path}," \
  %{SOURCE24} >%{buildroot}%{_datadir}/cmake/Modules/FindCEF.cmake
echo '%%_cef_api_requires() Requires: cef%%{?1:(api) = %%1}%%{!?1:(abi) = %{cef_version}}' > %{buildroot}%{_rpmmacrodir}/macros.cef
mkdir -p .fedora-rpm/docs/
cp AUTHORS .fedora-rpm/docs/AUTHORS-CHROMIUM
cp cef/AUTHORS.txt .fedora-rpm/docs/AUTHORS-CEF
mkdir -p .fedora-rpm/license/
cp LICENSE .fedora-rpm/license/LICENSE-CHROMIUM
cp cef/LICENSE.txt .fedora-rpm/license/LICENSE-CEF
cp %{SOURCE1} .
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{undefined flatpak}
%post

if selinuxenabled; then
	semanage fcontext -a -t bin_t %{chromium_path} &>/dev/null || :
	semanage fcontext -a -t chrome_sandbox_exec_t %{chromium_path}/chrome-sandbox &>/dev/null || :
	restorecon -R -v %{chromium_path} &>/dev/null || :
fi
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
