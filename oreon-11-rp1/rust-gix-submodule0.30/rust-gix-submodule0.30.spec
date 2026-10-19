%global source0_hash 9fd5fc8692890bd71a596e540fd4c364f8460eaa82c4eaaedebde6e1e3eb4d91
%bcond check 0
%global debug_package %{nil}
%global crate gix-submodule
Name:           rust-gix-submodule0.30
Version:        0.30.0
Release:        1%{?dist}
Summary:        A crate of the gitoxide project dealing git submodules
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-submodule
Source0:        https://static.crates.io/crates/gix-submodule/gix-submodule-%{version}.crate
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

%package     -n %{name}+sha1-devel
Summary:        A crate of the gitoxide project dealing git submodules
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

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
%files -n rust-gix-submodule0.30-devel -f %{oreon_filedir}/rust-gix-submodule0.30-devel.list

%changelog

%autochangelog
