%global source0_hash c325dfab65f261f386debee8b0969da215b3fa0037e74c8a1234db7ba986d803
%bcond check 0
%global debug_package %{nil}
%global crate mini-moka
Name:           rust-mini-moka
Version:        0.10.3
Release:        1%{?dist}
Summary:        A lighter edition of Moka, a fast and concurrent cache library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/mini-moka
Source0:        https://static.crates.io/crates/mini-moka/mini-moka-%{version}.crate
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
Summary:        A lighter edition of Moka, a fast and concurrent cache library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dashmap-devel
Summary:        A lighter edition of Moka, a fast and concurrent cache library
BuildArch:      noarch
%description -n %{name}+dashmap-devel

This package contains library source intended for building other packages which
use the "dashmap" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        A lighter edition of Moka, a fast and concurrent cache library
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

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
%files -n rust-mini-moka-devel -f %{oreon_filedir}/rust-mini-moka-devel.list

%changelog

%autochangelog
