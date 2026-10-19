%global source0_hash 3afa277b2cd2843cbfab1339af6a1ae6e37073564d51b855402ccd4539f901a6
%bcond check 1
%global debug_package %{nil}
%global crate struct-patch-derive
Name:           rust-struct-patch-derive
Version:        0.9.5
Release:        1%{?dist}
Summary:        Library that helps you implement partial updates for your structs
License:        MIT
URL:            https://crates.io/crates/struct-patch-derive
Source0:        https://static.crates.io/crates/struct-patch-derive/struct-patch-derive-%{version}.crate
Patch:          struct-patch-derive-fix-metadata.diff
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
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+merge-devel
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+merge-devel

This package contains library source intended for building other packages which
use the "merge" feature of the "%{crate}" crate.

%package     -n %{name}+op-devel
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+op-devel

This package contains library source intended for building other packages which
use the "op" feature of the "%{crate}" crate.

%package     -n %{name}+status-devel
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+status-devel

This package contains library source intended for building other packages which
use the "status" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
grep -q 'use pretty_assertions_sorted' src/patch.rs
sed -i '/use pretty_assertions_sorted/d' src/patch.rs
sed -i 's/assert_eq_sorted/assert_eq/' src/patch.rs
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
%files -n rust-struct-patch-derive-devel -f %{oreon_filedir}/rust-struct-patch-derive-devel.list

%changelog

%autochangelog
