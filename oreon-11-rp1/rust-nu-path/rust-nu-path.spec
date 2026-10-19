%global source0_hash de17919a6834e6b773256a2f29632571473ee3c83a1530f6385c3a80d13b0564
%bcond check 1
%global debug_package %{nil}
%global crate nu-path
Name:           rust-nu-path
Version:        0.99.1
Release:        1%{?dist}
Summary:        Path handling library for Nushell
License:        MIT
URL:            https://crates.io/crates/nu-path
Source0:        https://static.crates.io/crates/nu-path/nu-path-%{version}.crate
Patch:          nu-path-fix-metadata-auto.diff
Patch:          nu-path-fix-metadata.diff
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
Summary:        Path handling library for Nushell
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
%files -n rust-nu-path-devel -f %{oreon_filedir}/rust-nu-path-devel.list

%changelog

%autochangelog
