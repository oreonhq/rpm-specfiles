%global source0_hash 3944826ff8fa8093089aba3acb4ef44b9446a99a16f3bf4e74af3f77d340ab7d
%bcond check 0
%global debug_package %{nil}
%global crate safe-transmute
Name:           rust-safe-transmute
Version:        0.11.3
Release:        1%{?dist}
Summary:        Safeguarded transmute() for Rust
License:        MIT
URL:            https://crates.io/crates/safe-transmute
Source0:        https://static.crates.io/crates/safe-transmute/safe-transmute-%{version}.crate
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
Summary:        Safeguarded transmute() for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Safeguarded transmute() for Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+const_generics-devel
Summary:        Safeguarded transmute() for Rust
BuildArch:      noarch
%description -n %{name}+const_generics-devel

This package contains library source intended for building other packages which
use the "const_generics" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Safeguarded transmute() for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-safe-transmute-devel -f %{oreon_filedir}/rust-safe-transmute-devel.list

%changelog

%autochangelog
