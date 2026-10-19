%global source0_hash 11331a1b48f99ea6bb27faae41399d08783d055ddee131e1b1b70a854207ebf8
%bcond check 0
%global debug_package %{nil}
%global crate vsort
Name:           rust-vsort
Version:        0.2.0
Release:        1%{?dist}
Summary:        GNU Version Sort Rust implementation
License:        MIT
URL:            https://crates.io/crates/vsort
Source0:        https://static.crates.io/crates/vsort/vsort-%{version}.crate
Patch:          vsort-fix-metadata.diff
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
Summary:        GNU Version Sort Rust implementation
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
%files -n rust-vsort-devel -f %{oreon_filedir}/rust-vsort-devel.list

%changelog

%autochangelog
