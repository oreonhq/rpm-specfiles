%global source0_hash fc652a48c352aef3ea3aed32080501cf3ef6ed5da78602a020c991775b0aff04
%bcond check 0
%global debug_package %{nil}
%global crate bytes
Name:           rust-bytes
Version:        1.12.1
Release:        2%{?dist}
Summary:        Types and traits for working with bytes
License:        MIT
URL:            https://crates.io/crates/bytes
Source0:        https://static.crates.io/crates/bytes/bytes-%{version}.crate
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
Summary:        Types and traits for working with bytes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+extra-platforms-devel
Summary:        Types and traits for working with bytes
BuildArch:      noarch
%description -n %{name}+extra-platforms-devel

This package contains library source intended for building other packages which
use the "extra-platforms" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Types and traits for working with bytes
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Types and traits for working with bytes
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-bytes-devel -f %{oreon_filedir}/rust-bytes-devel.list

%changelog

%autochangelog
