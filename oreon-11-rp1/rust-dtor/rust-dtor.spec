%global source0_hash cd3f6c362b2bbd7063090886afd78978f5dbf1f11da7efcc40f81d32c943fac1
%bcond check 0
%global debug_package %{nil}
%global crate dtor
Name:           rust-dtor
Version:        1.0.6
Release:        1%{?dist}
Summary:        __attribute__((destructor)) for Rust
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/dtor
Source0:        https://static.crates.io/crates/dtor/dtor-%{version}.crate
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
Summary:        __attribute__((destructor)) for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__no_warn_on_missing_unsafe-devel
Summary:        __attribute__((destructor)) for Rust
BuildArch:      noarch
%description -n %{name}+__no_warn_on_missing_unsafe-devel

This package contains library source intended for building other packages which
use the "__no_warn_on_missing_unsafe" feature of the "%{crate}" crate.

%package     -n %{name}+proc_macro-devel
Summary:        __attribute__((destructor)) for Rust
BuildArch:      noarch
%description -n %{name}+proc_macro-devel

This package contains library source intended for building other packages which
use the "proc_macro" feature of the "%{crate}" crate.

%package     -n %{name}+used_linker-devel
Summary:        __attribute__((destructor)) for Rust
BuildArch:      noarch
%description -n %{name}+used_linker-devel

This package contains library source intended for building other packages which
use the "used_linker" feature of the "%{crate}" crate.

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
%files -n rust-dtor-devel -f %{oreon_filedir}/rust-dtor-devel.list

%changelog

%autochangelog
