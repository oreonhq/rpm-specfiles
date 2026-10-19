%global source0_hash 5d886e39ddc1a462479b0cd6fcdc7b1b2d2d086db53d65149c1cfe69b74b6baa
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_head
Name:           rust-uu_head
Version:        0.7.0
Release:        1%{?dist}
Summary:        head ~ (uutils) display the first lines of input
License:        MIT
URL:            https://crates.io/crates/uu_head
Source0:        https://static.crates.io/crates/uu_head/uu_head-%{version}.crate
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
Summary:        head ~ (uutils) display the first lines of input
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
%files -n rust-uu_head-devel -f %{oreon_filedir}/rust-uu_head-devel.list

%changelog

%autochangelog
