%global source0_hash e182d6ec6f05393cc0e5ed1bf81ad6db3a8feedf8ee515ecdd369809bcce8082
%bcond check 0
%global debug_package %{nil}
%global crate serde_with_macros
Name:           rust-serde_with_macros1
Version:        1.5.2
Release:        1%{?dist}
Summary:        proc-macro library for serde_with
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_with_macros
Source0:        https://static.crates.io/crates/serde_with_macros/serde_with_macros-%{version}.crate
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
Summary:        proc-macro library for serde_with
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
%files -n rust-serde_with_macros1-devel -f %{oreon_filedir}/rust-serde_with_macros1-devel.list

%changelog

%autochangelog
