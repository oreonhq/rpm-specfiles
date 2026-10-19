%global source0_hash 1db1df1b8dd701aa57b41283b50b751b3ebc8fe1406955ec90c53b46b475fa56
%bcond check 0
%global debug_package %{nil}
%global crate minus
Name:           rust-minus
Version:        5.7.2
Release:        1%{?dist}
Summary:        Asynchronous data feedable terminal paging library for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/minus
Source0:        https://static.crates.io/crates/minus/minus-%{version}.crate
Patch:          minus-fix-metadata.diff
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
Summary:        Asynchronous data feedable terminal paging library for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dynamic_output-devel
Summary:        Asynchronous data feedable terminal paging library for Rust
BuildArch:      noarch
%description -n %{name}+dynamic_output-devel

This package contains library source intended for building other packages which
use the "dynamic_output" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Asynchronous data feedable terminal paging library for Rust
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+search-devel
Summary:        Asynchronous data feedable terminal paging library for Rust
BuildArch:      noarch
%description -n %{name}+search-devel

This package contains library source intended for building other packages which
use the "search" feature of the "%{crate}" crate.

%package     -n %{name}+static_output-devel
Summary:        Asynchronous data feedable terminal paging library for Rust
BuildArch:      noarch
%description -n %{name}+static_output-devel

This package contains library source intended for building other packages which
use the "static_output" feature of the "%{crate}" crate.

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

%cargo_test -f dynamic_output,static_output
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-minus-devel -f %{oreon_filedir}/rust-minus-devel.list

%changelog

%autochangelog
