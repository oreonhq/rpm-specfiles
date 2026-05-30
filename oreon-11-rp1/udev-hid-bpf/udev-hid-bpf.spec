%global source0_hash 65d24c9651604c841ca55d08c284d115959fb150b86343898716b2c04566b8fd
%global source1_hash b39a98fa8b5871b2b357b8c9793a067fec2dbe778a2481c9770aa9fda86921d7

%bcond_without check
%global udevdir %(pkg-config --variable=udevdir udev)
%global cargo_install_lib 0
%global crate udev-hid-bpf
%global _firmware /usr/lib/firmware

%if 0%{?rhel} || (0%{?oreon} >= 11)
%global bundled_rust_deps 1
%global build_testing 0
%global build_tracing 1
%else
%global bundled_rust_deps 0
%global build_testing 1
%endif

# Fedora 42 never shipped a kernel 6.12 so no need for our tracing sources
%if 0%{?fedora} >= 42 || (0%{?oreon} >= 11)
%global build_tracing "false"
%else
%global build_tracing "true"
%endif

# Upstream uses 1.0.0-20240417 but rpm won't let us use the dash, so let's use a dot instead.
%global upstream_version 2.2.0
%global upstream_version_date 20251121
%global tarball %{upstream_version}-%{upstream_version_date}

Name:           udev-hid-bpf
Version:        %{upstream_version}.%{upstream_version_date}
Release:        %autorelease
Summary:        HID-BPF quirk loader tool

SourceLicense:  GPL-2.0-only
# Licenses of statically linked Rust dependencies:
#
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# BSD-2-Clause
# GPL-2.0-only
# LGPL-2.1-only OR BSD-2-Clause
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
    GPL-2.0-only AND
    BSD-2-Clause AND
    MIT AND
    Unicode-DFS-2016 AND
    (LGPL-2.1-only OR BSD-2-Clause) AND
    (MIT OR Apache-2.0) AND
    (Unlicense OR MIT)
    }
URL:            https://gitlab.freedesktop.org/libevdev/udev-hid-bpf/
Source0:        https://gitlab.freedesktop.org/libevdev/udev-hid-bpf/-/archive/2.2.0-20251121/udev-hid-bpf-2.2.0-20251121.tar.bz2
# To recreate tarball:
# $ centpkg prep (do not use fedpkg, it removes Cargo.lock)
# $ pushd udev-hid-bpf-...; cargo vendor && tar Jcvf ../$(basename $PWD)-vendor.tar.xz vendor/ ; popd
Source1:        %{name}-%{upstream_version}-%{upstream_version_date}-vendor.tar.xz

Patch01:        0001-Bump-the-cargo-test-timeout-to-500s.patch
Patch02:        0001-Cargo.toml-drop-libbpf-sys-to-1.5.0.patch
# Update stderrlog dependency from 0.5 to 0.6
# https://gitlab.freedesktop.org/libevdev/udev-hid-bpf/-/merge_requests/223
# Here, we still allow 0.5 as well for compatibility with vendored deps.
Patch03:        udev-hid-bpf-2.2.0-20251121-stderrlog-0.6.patch

%if 0%{?rhel} || (0%{?oreon} >= 11)
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros >= 26
%endif
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-rpm-macros
BuildRequires:  meson cargo
BuildRequires:  pkgconfig(udev)
BuildRequires:  clang
BuildRequires:  git
BuildRequires:  pkgconfig(libbpf) bpftool
BuildRequires:  pkgconfig(libudev)

Requires:       systemd-udev
Requires:       %{name}-stable%{?_isa} = %{version}-%{release}

# We don't have bpftool (#2294345)
ExcludeArch:    %{ix86}

%description
%{name} is a loader for HID eBPF programs aimed
at making it simple to develop and test eBPF programs
for HID devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries
and header files for developing applications
that use %{name}.

%if 0%{?build_testing}
%package        testing
Summary:        Testing eBPF programs for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    testing
The %{name}-testing package contains HID eBPF programs
for %{name} that have not yet been merged into
an upstream kernel.
%endif

%package        stable
Summary:        Stable eBPF programs for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    stable
The %{name}-stable package contains HID eBPF programs
for %{name} that have been merged into
an upstream kernel.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%autosetup -S git -p1 -n %{name}-%{tarball}
%py3_shebang_fix $(git grep -l  '#!/usr/bin/.*python3')

# Real build system is meson but upstream makes
# sure cargo on its own works too so this is safe to call here
%if 0%{?bundled_rust_deps}
tar xf %{SOURCE1}
%cargo_prep -v vendor
%else
%cargo_prep
%endif

%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires
%endif

%build
export RUSTFLAGS="%build_rustflags"
%if 0%{?build_testing}
%global bpf_set stable,testing
%else
%global bpf_set stable
%endif

%meson -Dudevdir=%{udevdir} \
       -Dbpfs=%{bpf_set} \
       -Dbpf-tracing=%{build_tracing} \
       -Dtests=disabled \
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif

%install
%meson_install

%if %{with check}
%check
%meson_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%license cargo-vendor.txt
%endif
%doc README.md
%{_bindir}/udev-hid-bpf
%{_mandir}/man1/udev-hid-bpf.1*
%{udevdir}/rules.d/81-hid-bpf.rules
%dir /usr/lib/firmware/hid/bpf
%dir /usr/lib/firmware/hid/

%files stable
%license LICENSE
%license LICENSE.dependencies
%{_udevhwdbdir}/81-hid-bpf-stable.hwdb
%{_firmware}/hid/bpf/*-FR-TEC__Raptor-Mach-2.bpf.o
%{_firmware}/hid/bpf/*-HP__Elite-Presenter.bpf.o
%{_firmware}/hid/bpf/*-Huion__Dial-2.bpf.o
%{_firmware}/hid/bpf/*-Huion__Inspiroy-2-M.bpf.o
%{_firmware}/hid/bpf/*-Huion__Inspiroy-2-S.bpf.o
%{_firmware}/hid/bpf/*-Huion__Kamvas-Pro-19.bpf.o
%{_firmware}/hid/bpf/*-Huion__Kamvas13Gen3.bpf.o
%{_firmware}/hid/bpf/*-Huion__Kamvas16Gen3.bpf.o
%{_firmware}/hid/bpf/*-Huion__KeydialK20.bpf.o
%{_firmware}/hid/bpf/*-IOGEAR__Kaliber-MMOmentum.bpf.o
%{_firmware}/hid/bpf/*-Logitech__SpaceNavigator.bpf.o
%{_firmware}/hid/bpf/*-Microsoft__Xbox-Elite-2.bpf.o
%{_firmware}/hid/bpf/*-Mistel__MD770.bpf.o
%{_firmware}/hid/bpf/*-Rapoo__M50-Plus-Silent.bpf.o
%{_firmware}/hid/bpf/*-TUXEDO__Sirius-16-Gen1-and-Gen2.bpf.o
%{_firmware}/hid/bpf/*-Thrustmaster__TCA-Yoke-Boeing.bpf.o
%{_firmware}/hid/bpf/*-WALTOP__Batteryless-Tablet.bpf.o
%{_firmware}/hid/bpf/*-Wacom__ArtPen.bpf.o
%{_firmware}/hid/bpf/*-XPPen__ACK05.bpf.o
%{_firmware}/hid/bpf/*-XPPen__Artist24.bpf.o
%{_firmware}/hid/bpf/*-XPPen__ArtistPro16Gen2.bpf.o
%{_firmware}/hid/bpf/*-XPPen__Deco01V3.bpf.o
%{_firmware}/hid/bpf/*-XPPen__Deco02.bpf.o
%{_firmware}/hid/bpf/*-XPPen__DecoMini4.bpf.o

%if 0%{?build_testing}
%files testing
%license LICENSE
%license LICENSE.dependencies
%{_udevhwdbdir}/81-hid-bpf-testing.hwdb
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.0.20251121-1
- Import
