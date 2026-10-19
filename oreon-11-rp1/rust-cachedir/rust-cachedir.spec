%global source0_hash 4703f3937077db8fa35bee3c8789343c1aec2585f0146f09d658d4ccc0e8d873
%bcond check 0
%global debug_package %{nil}
%global crate cachedir
Name:           rust-cachedir
Version:        0.3.1
Release:        1%{?dist}
Summary:        Library to help interacting with cache directories and CACHEDIR.TAG files
License:        MIT
URL:            https://crates.io/crates/cachedir
Source0:        https://static.crates.io/crates/cachedir/cachedir-%{version}.crate
Patch:          cachedir-fix-metadata.diff
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
Summary:        Library to help interacting with cache directories and CACHEDIR.TAG files
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
%files -n rust-cachedir-devel -f %{oreon_filedir}/rust-cachedir-devel.list

%changelog

%autochangelog
