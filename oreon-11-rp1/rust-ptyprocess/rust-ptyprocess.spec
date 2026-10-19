%global source0_hash 101be273c0b1680d7056afddbaa88f02b6e9f2dc161165c30bee9914b6025a79
%bcond check 0
%global debug_package %{nil}
%global crate ptyprocess
Name:           rust-ptyprocess
Version:        0.5.0
Release:        1%{?dist}
Summary:        A library to work with PTY/TTY on Unix systems
License:        MIT
URL:            https://crates.io/crates/ptyprocess
Source0:        https://static.crates.io/crates/ptyprocess/ptyprocess-%{version}.crate
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

%package     -n %{name}+close-range-devel
Summary:        A library to work with PTY/TTY on Unix systems
BuildArch:      noarch
%description -n %{name}+close-range-devel

This package contains library source intended for building other packages which
use the "close-range" feature of the "%{crate}" crate.

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
%files -n rust-ptyprocess-devel -f %{oreon_filedir}/rust-ptyprocess-devel.list

%changelog

%autochangelog
