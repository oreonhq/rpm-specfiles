%global source0_hash e2953bfe4f93bbd20cc71198842756f77d161884c99ebbabc41d80231ded88d1
%bcond check 0
%global debug_package %{nil}
%global crate defmt
Name:           rust-defmt
Version:        1.1.1
Release:        1%{?dist}
Summary:        A highly efficient logging framework that targets resource-constraine...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/defmt
Source0:        https://static.crates.io/crates/defmt/defmt-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        A highly efficient logging framework that targets resource-constraine...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+avoid-default-panic-devel
Summary:        A highly efficient logging framework that targets resource-constraine...
BuildArch:      noarch
%description -n %{name}+avoid-default-panic-devel

This package contains library source intended for building other packages which
use the "avoid-default-panic" feature of the "%{crate}" crate.

%package     -n %{name}+encoding-raw-devel
Summary:        A highly efficient logging framework that targets resource-constraine...
BuildArch:      noarch
%description -n %{name}+encoding-raw-devel

This package contains library source intended for building other packages which
use the "encoding-raw" feature of the "%{crate}" crate.

%package     -n %{name}+encoding-rzcobs-devel
Summary:        A highly efficient logging framework that targets resource-constraine...
BuildArch:      noarch
%description -n %{name}+encoding-rzcobs-devel

This package contains library source intended for building other packages which
use the "encoding-rzcobs" feature of the "%{crate}" crate.

%package     -n %{name}+ip_in_core-devel
Summary:        A highly efficient logging framework that targets resource-constraine...
BuildArch:      noarch
%description -n %{name}+ip_in_core-devel

This package contains library source intended for building other packages which
use the "ip_in_core" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-test-devel
Summary:        A highly efficient logging framework that targets resource-constraine...
BuildArch:      noarch
%description -n %{name}+unstable-test-devel

This package contains library source intended for building other packages which
use the "unstable-test" feature of the "%{crate}" crate.

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
%files -n rust-defmt-devel -f %{oreon_filedir}/rust-defmt-devel.list

%changelog

%autochangelog
