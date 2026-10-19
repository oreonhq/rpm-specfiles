%global source0_hash 57ae9afe4a6a602d1fb3752f63a55bea0957403b0fc3c244184ba6f9c1a65932
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_join
Name:           rust-uu_join
Version:        0.7.0
Release:        1%{?dist}
Summary:        join ~ (uutils) merge lines from inputs with matching join fields
License:        MIT
URL:            https://crates.io/crates/uu_join
Source0:        https://static.crates.io/crates/uu_join/uu_join-%{version}.crate
Patch:          uu_join-fix-metadata.diff
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
Summary:        join ~ (uutils) merge lines from inputs with matching join fields
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
%files -n rust-uu_join-devel -f %{oreon_filedir}/rust-uu_join-devel.list

%changelog

%autochangelog
