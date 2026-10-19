%global source0_hash 20296a054f6fb573c1f73e49b0e3afd1efcc643548928fc9c21144f5ecf4f7e3
%bcond check 1
%global debug_package %{nil}
%global crate socketpair
Name:           rust-socketpair
Version:        0.19.8
Release:        1%{?dist}
Summary:        Cross-platform socketpair functionality
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/socketpair
Source0:        https://static.crates.io/crates/socketpair/socketpair-%{version}.crate
Patch:          socketpair-fix-metadata-auto.diff
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
Summary:        Cross-platform socketpair functionality
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Cross-platform socketpair functionality
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Cross-platform socketpair functionality
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+use_async_std-devel
Summary:        Cross-platform socketpair functionality
BuildArch:      noarch
%description -n %{name}+use_async_std-devel

This package contains library source intended for building other packages which
use the "use_async_std" feature of the "%{crate}" crate.

%package     -n %{name}+use_tokio-devel
Summary:        Cross-platform socketpair functionality
BuildArch:      noarch
%description -n %{name}+use_tokio-devel

This package contains library source intended for building other packages which
use the "use_tokio" feature of the "%{crate}" crate.

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
%files -n rust-socketpair-devel -f %{oreon_filedir}/rust-socketpair-devel.list

%changelog

%autochangelog
