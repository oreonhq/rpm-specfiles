%global source0_hash 4390796d1f70cfd2393ce3d6c8ba855352d5057e57f6527bca80a8638dd37d07
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_readlink
Name:           rust-uu_readlink
Version:        0.12.0
Release:        1%{?dist}
Summary:        readlink ~ (uutils) display resolved path of PATHNAME
License:        MIT
URL:            https://crates.io/crates/uu_readlink
Source0:        https://static.crates.io/crates/uu_readlink/uu_readlink-%{version}.crate
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
Summary:        readlink ~ (uutils) display resolved path of PATHNAME
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
%files -n rust-uu_readlink-devel -f %{oreon_filedir}/rust-uu_readlink-devel.list

%changelog

%autochangelog
