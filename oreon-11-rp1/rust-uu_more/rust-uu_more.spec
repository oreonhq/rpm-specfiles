%global source0_hash 838664c9ce4830a1210289481404b1351e42276e0fd22a7cc17be79ae2c3efc8
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_more
Name:           rust-uu_more
Version:        0.7.0
Release:        1%{?dist}
Summary:        more ~ (uutils) input perusal filter
License:        MIT
URL:            https://crates.io/crates/uu_more
Source0:        https://static.crates.io/crates/uu_more/uu_more-%{version}.crate
Patch:          uu_more-fix-metadata-auto.diff
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
Summary:        more ~ (uutils) input perusal filter
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
%files -n rust-uu_more-devel -f %{oreon_filedir}/rust-uu_more-devel.list

%changelog

%autochangelog
