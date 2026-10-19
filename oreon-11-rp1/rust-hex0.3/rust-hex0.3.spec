%global source0_hash 805026a5d0141ffc30abb3be3173848ad46a1b1664fe632428479619a3644d77
%bcond check 0
%global debug_package %{nil}
%global crate hex
Name:           rust-hex0.3
Version:        0.3.2
Release:        1%{?dist}
Summary:        Encoding and decoding data into/from hexadecimal representation.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hex
Source0:        https://static.crates.io/crates/hex/hex-%{version}.crate
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

%package     -n %{name}+benchmarks-devel
Summary:        Encoding and decoding data into/from hexadecimal representation.
BuildArch:      noarch
%description -n %{name}+benchmarks-devel

This package contains library source intended for building other packages which
use the "benchmarks" feature of the "%{crate}" crate.

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
%files -n rust-hex0.3-devel -f %{oreon_filedir}/rust-hex0.3-devel.list

%changelog

%autochangelog
