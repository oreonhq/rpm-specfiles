%global source0_hash 65d24c9651604c841ca55d08c284d115959fb150b86343898716b2c04566b8fd
%global source1_hash none
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
%if 0%{?fedora} >= 42 || (0%{?oreon} >= 11)
%global build_tracing "false"
%else
%global build_tracing "true"
%endif
%global upstream_version 2.2.0
%global upstream_version_date 20251121
%global tarball %{upstream_version}-%{upstream_version_date}
Name:           udev-hid-bpf
Version:        %{upstream_version}.%{upstream_version_date}
Release:        1%{?dist}
Summary:        HID-BPF quirk loader tool
SourceLicense:  GPL-2.0-only
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
Source0:        https://gitlab.freedesktop.org/libevdev/%{name}/-/archive/%{tarball}/%{name}-%{tarball}.tar.bz2
Patch01:        0001-Bump-the-cargo-test-timeout-to-500s.patch
Patch02:        0001-Cargo.toml-drop-libbpf-sys-to-1.5.0.patch
Patch03:        udev-hid-bpf-2.2.0-20251121-stderrlog-0.6.patch
%if 0%{?rhel} || (0%{?oreon} >= 11)
%else
%endif
Requires:       systemd-udev
Requires:       %{name}-stable%{?_isa} = %{version}-%{release}
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  bpftool
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  pkgconfig(libbpf)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(udev)
BuildRequires:  python3-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -p1 -n %{name}-%{tarball}
%py3_shebang_fix $(git grep -l  '#!/usr/bin/.*python3')
%if 0%{?bundled_rust_deps}
cargo vendor --versioned-dirs
%else
%endif
%if ! 0%{?bundled_rust_deps}
%oreon_vendor_cargo
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n udev-hid-bpf-devel -f %{oreon_filedir}/udev-hid-bpf-devel.list
%files -n udev-hid-bpf-testing -f %{oreon_filedir}/udev-hid-bpf-testing.list
%files -n udev-hid-bpf-stable -f %{oreon_filedir}/udev-hid-bpf-stable.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.0.20251121-1
- Import
%endif
