%global source0_hash 312d12393c060384f2e6ed14c7b4be37b3dd90249857485613c1a91b9a1abb5c
%bcond check 0
%global debug_package %{nil}
%global crate bssl-sys
Name:           rust-bssl-sys
Version:        0.1.0
Release:        1%{?dist}
Summary:        Placeholder package for boringssl bindings
License:        MIT
URL:            https://crates.io/crates/bssl-sys
Source0:        https://static.crates.io/crates/bssl-sys/bssl-sys-%{version}.crate
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
Summary:        Placeholder package for boringssl bindings
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
%files -n rust-bssl-sys-devel -f %{oreon_filedir}/rust-bssl-sys-devel.list

%changelog

%autochangelog
