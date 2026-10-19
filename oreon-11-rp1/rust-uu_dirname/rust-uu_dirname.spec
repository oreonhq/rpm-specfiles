%global source0_hash 8954430cc6fc6d426905eea23c4aa13af3eb5260311ff712d698e208546b831c
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_dirname
Name:           rust-uu_dirname
Version:        0.7.0
Release:        1%{?dist}
Summary:        dirname ~ (uutils) display parent directory of PATHNAME
License:        MIT
URL:            https://crates.io/crates/uu_dirname
Source0:        https://static.crates.io/crates/uu_dirname/uu_dirname-%{version}.crate
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
Summary:        dirname ~ (uutils) display parent directory of PATHNAME
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
%files -n rust-uu_dirname-devel -f %{oreon_filedir}/rust-uu_dirname-devel.list

%changelog

%autochangelog
