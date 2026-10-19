%global source0_hash 0128396dd7313f697ad05b21b1a7be7d4cbb81888704f55996e4a27db196bb4d
%bcond check 1
%global debug_package %{nil}
%global crate actix-utils
Name:           rust-actix-utils
Version:        3.0.2
Release:        1%{?dist}
Summary:        Various utilities used in the Actix ecosystem
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-utils
Source0:        https://static.crates.io/crates/actix-utils/actix-utils-%{version}.crate
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
Summary:        Various utilities used in the Actix ecosystem
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
%files -n rust-actix-utils-devel -f %{oreon_filedir}/rust-actix-utils-devel.list

%changelog

%autochangelog
