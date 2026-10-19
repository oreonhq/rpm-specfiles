%global source0_hash 285bbc825d334001c7545f8ee0272f62ec304a63838dbfce79b324313d9e548d
%bcond check 0
%global cargo_install_lib 0
%global crate rublk
Name:           rust-rublk
Version:        0.2.12
Release:        1%{?dist}
Summary:        Rust ublk generic targets
License:        GPL-2.0-or-later
URL:            https://crates.io/crates/rublk
Source0:        https://static.crates.io/crates/rublk/rublk-%{version}.crate
Patch0:         0001-rublk-don-t-wakeup-task-for-timeout-IO.patch
%global build_rustflags %{build_rustflags} --cfg=io_uring_skip_arch_check
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  clang-libs
BuildRequires:  libstdc++-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Rust ublk generic targets
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND GPL-2.0-or-later AND MIT AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0+ AND (Unlicense OR MIT) AND Unicode-DFS-2016
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -N
%autopatch -p1
%oreon_vendor_cargo
%build

%cargo_build -f compress
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
%install
%cargo_install -f compress
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -f compress
%endif
%files -f %{oreon_filedir}/main.list
%files -n rublk -f %{oreon_filedir}/rublk.list

%changelog

%autochangelog
