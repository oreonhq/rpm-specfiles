%global source0_hash 9900206b54a3527fdc7b8a938bffd94a568bac4f4aa8113b209df75a09c0dec2
%global debug_package %{nil}
%bcond check 1
%global crate semver-parser
Name:           rust-semver-parser
Version:        0.10.3
Release:        1%{?dist}
Summary:        Parsing of the semver spec
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/semver-parser
Source0:        https://static.crates.io/crates/semver-parser/semver-parser-%{version}.crate
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
Summary:        Parsing of the semver spec
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-semver-parser-devel -f %{oreon_filedir}/rust-semver-parser-devel.list

%changelog

%autochangelog
