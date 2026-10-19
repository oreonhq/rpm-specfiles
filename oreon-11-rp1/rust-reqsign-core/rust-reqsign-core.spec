%global source0_hash b10302cf0a7d7e7352ba211fc92c3c5bebf1286153e49cc5aa87348078a8e102
%bcond check 1
%global debug_package %{nil}
%global crate reqsign-core
Name:           rust-reqsign-core
Version:        3.0.0
Release:        1%{?dist}
Summary:        Signing API requests without effort
License:        Apache-2.0
URL:            https://crates.io/crates/reqsign-core
Source0:        https://static.crates.io/crates/reqsign-core/reqsign-core-%{version}.crate
Patch:          reqsign-core-fix-metadata-auto.diff
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
Summary:        Signing API requests without effort
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
%files -n rust-reqsign-core-devel -f %{oreon_filedir}/rust-reqsign-core-devel.list

%changelog

%autochangelog
