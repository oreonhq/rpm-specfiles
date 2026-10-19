%global source0_hash fe52319a927259afbfa5180c5157cd8167edfd3e8c254f9558c7fef44c5649f2
%bcond check 1
%global debug_package %{nil}
%global crate serde_json_canonicalizer
Name:           rust-serde_json_canonicalizer
Version:        0.3.2
Release:        1%{?dist}
Summary:        JSON Canonicalization Scheme (JCS - RFC 8785) implementation
License:        MIT
URL:            https://crates.io/crates/serde_json_canonicalizer
Source0:        https://static.crates.io/crates/serde_json_canonicalizer/serde_json_canonicalizer-%{version}.crate
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
Summary:        JSON Canonicalization Scheme (JCS - RFC 8785) implementation
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
%files -n rust-serde_json_canonicalizer-devel -f %{oreon_filedir}/rust-serde_json_canonicalizer-devel.list

%changelog

%autochangelog
