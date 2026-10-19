%global source0_hash 65e94b453c0574ea58c643f327283f12384c985a9de4bdb5ab3393c50e73a05a
%bcond check 0
%global debug_package %{nil}
%global crate lv2-state
Name:           rust-lv2-state
Version:        2.0.0
Release:        1%{?dist}
Summary:        Rust-lv2's state handling library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lv2-state
Source0:        https://static.crates.io/crates/lv2-state/lv2-state-%{version}.crate
Patch:          lv2-state-fix-metadata.diff
ExcludeArch:    ppc64le s390x
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust-lv2's state handling library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%ifarch aarch64
rm tests/integration.rs
%endif
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-lv2-state-devel -f %{oreon_filedir}/rust-lv2-state-devel.list

%changelog

%autochangelog
