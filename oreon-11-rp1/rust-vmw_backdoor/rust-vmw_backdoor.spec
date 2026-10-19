%global source0_hash 364f0e642713074c45b4f4a1ee7d0c582650d2a57567af5c4060527bd9d30e59
%bcond check 0
%global debug_package %{nil}
%global crate vmw_backdoor
Name:           rust-vmw_backdoor
Version:        0.2.4
Release:        1%{?dist}
Summary:        A pure-Rust library for VMware host-guest protocol ("VMXh backdoor")
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/vmw_backdoor
Source0:        https://static.crates.io/crates/vmw_backdoor/vmw_backdoor-%{version}.crate
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
Summary:        A pure-Rust library for VMware host-guest protocol ("VMXh backdoor")
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-vmw_backdoor-devel -f %{oreon_filedir}/rust-vmw_backdoor-devel.list

%changelog

%autochangelog
