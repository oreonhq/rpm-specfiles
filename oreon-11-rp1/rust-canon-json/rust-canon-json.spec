%global source0_hash b5ae9f90437d2e2efba2a6c75b8279aa6b8f2f4017e0a4aeb64a76cd9d3a2bab
%bcond check 0
%global debug_package %{nil}
%global crate canon-json
Name:           rust-canon-json
Version:        0.2.1
Release:        1%{?dist}
Summary:        Serde_json Formatter to serialize as RFC 8785 canonical JSON
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/canon-json
Source0:        https://static.crates.io/crates/canon-json/canon-json-%{version}.crate
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
Summary:        Serde_json Formatter to serialize as RFC 8785 canonical JSON
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
%files -n rust-canon-json-devel -f %{oreon_filedir}/rust-canon-json-devel.list

%changelog

%autochangelog
