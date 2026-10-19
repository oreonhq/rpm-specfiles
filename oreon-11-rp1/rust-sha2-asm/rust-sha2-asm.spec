%global source0_hash b845214d6175804686b2bd482bcffe96651bb2d1200742b712003504a2dac1ab
%bcond check 0
%global debug_package %{nil}
%global crate sha2-asm
Name:           rust-sha2-asm
Version:        0.6.4
Release:        1%{?dist}
Summary:        Assembly implementation of SHA-2 compression functions
License:        MIT
URL:            https://crates.io/crates/sha2-asm
Source0:        https://static.crates.io/crates/sha2-asm/sha2-asm-%{version}.crate
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
Summary:        Assembly implementation of SHA-2 compression functions
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
%files -n rust-sha2-asm-devel -f %{oreon_filedir}/rust-sha2-asm-devel.list

%changelog

%autochangelog
