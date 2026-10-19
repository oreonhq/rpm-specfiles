%global source0_hash 6b50826342786a51a89e2da3a28f1c32b06e387201bc2d19791f622c673706b1
%bcond check 1
%global debug_package %{nil}
%global crate criterion-plot
Name:           rust-criterion-plot0.5
Version:        0.5.0
Release:        1%{?dist}
Summary:        Criterion's plotting library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/criterion-plot
Source0:        https://static.crates.io/crates/criterion-plot/criterion-plot-%{version}.crate
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
Summary:        Criterion's plotting library
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
%files -n rust-criterion-plot0.5-devel -f %{oreon_filedir}/rust-criterion-plot0.5-devel.list

%changelog

%autochangelog
