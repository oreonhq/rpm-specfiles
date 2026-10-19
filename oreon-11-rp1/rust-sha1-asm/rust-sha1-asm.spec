%global source0_hash 286acebaf8b67c1130aedffad26f594eff0c1292389158135327d2e23aed582b
%bcond check 0
%global debug_package %{nil}
%global crate sha1-asm
Name:           rust-sha1-asm
Version:        0.5.3
Release:        1%{?dist}
Summary:        Assembly implementation of SHA-1 compression function
License:        MIT
URL:            https://crates.io/crates/sha1-asm
Source0:        https://static.crates.io/crates/sha1-asm/sha1-asm-%{version}.crate
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
Summary:        Assembly implementation of SHA-1 compression function
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
%files -n rust-sha1-asm-devel -f %{oreon_filedir}/rust-sha1-asm-devel.list

%changelog

%autochangelog
