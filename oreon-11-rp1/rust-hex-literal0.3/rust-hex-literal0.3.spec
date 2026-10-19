%global source0_hash 7ebdb29d2ea9ed0083cd8cece49bbd968021bd99b0849edb4a9a7ee0fdf6a4e0
%bcond check 0
%global debug_package %{nil}
%global crate hex-literal
Name:           rust-hex-literal0.3
Version:        0.3.4
Release:        1%{?dist}
Summary:        Procedural macro for converting hexadecimal string to byte array at compile time
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hex-literal
Source0:        https://static.crates.io/crates/hex-literal/hex-literal-%{version}.crate
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
Summary:        Procedural macro for converting hexadecimal string to byte array at compile time
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
%files -n rust-hex-literal0.3-devel -f %{oreon_filedir}/rust-hex-literal0.3-devel.list

%changelog

%autochangelog
