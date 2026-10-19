%global source0_hash 5a46885ecbabe024b9e6e3ee9ee3a32ad05adf2b6269f45aa912793d9c54c805
%bcond check 1
%global debug_package %{nil}
%global crate imago
Name:           rust-imago
Version:        0.2.1
Release:        1%{?dist}
Summary:        Library for accessing virtual machine disk images
License:        MIT
URL:            https://crates.io/crates/imago
Source0:        https://static.crates.io/crates/imago/imago-%{version}.crate
Patch:          imago-fix-metadata-auto.diff
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
Summary:        Library for accessing virtual machine disk images
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+sync-wrappers-devel
Summary:        Library for accessing virtual machine disk images
BuildArch:      noarch
%description -n %{name}+sync-wrappers-devel

This package contains library source intended for building other packages which
use the "sync-wrappers" feature of the "%{crate}" crate.

%package     -n %{name}+vm-memory-devel
Summary:        Library for accessing virtual machine disk images
BuildArch:      noarch
%description -n %{name}+vm-memory-devel

This package contains library source intended for building other packages which
use the "vm-memory" feature of the "%{crate}" crate.

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
%files -n rust-imago-devel -f %{oreon_filedir}/rust-imago-devel.list

%changelog

%autochangelog
