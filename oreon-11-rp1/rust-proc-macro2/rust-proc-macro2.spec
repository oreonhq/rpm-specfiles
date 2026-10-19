%global source0_hash 985e7ec9bb745e6ce6535b544d84d6cd6f7ad8bd711c398938ae983b91a766d9
%bcond check 0
%global debug_package %{nil}
%global crate proc-macro2
Name:           rust-proc-macro2
Version:        1.0.107
Release:        1%{?dist}
Summary:        Substitute implementation of the Rust compiler's proc_macro API
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proc-macro2
Source0:        https://static.crates.io/crates/proc-macro2/proc-macro2-%{version}.crate
Patch:          proc-macro2-fix-metadata.diff
Patch2:         0001-ignore-one-doctest-block-that-adds-superfluous-dev-d.patch
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
Summary:        Substitute implementation of the Rust compiler's proc_macro API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro-devel
Summary:        Substitute implementation of the Rust compiler's proc_macro API
BuildArch:      noarch
%description -n %{name}+proc-macro-devel

This package contains library source intended for building other packages which
use the "proc-macro" feature of the "%{crate}" crate.

%package     -n %{name}+span-locations-devel
Summary:        Substitute implementation of the Rust compiler's proc_macro API
BuildArch:      noarch
%description -n %{name}+span-locations-devel

This package contains library source intended for building other packages which
use the "span-locations" feature of the "%{crate}" crate.

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

%cargo_test -- -- --skip 'src/lib.rs'
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-proc-macro2-devel -f %{oreon_filedir}/rust-proc-macro2-devel.list

%changelog

%autochangelog
