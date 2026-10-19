%global source0_hash 9ca8a49c55b0396ae0a5326704130e9706fc09acd6180d795bff1154b60db708
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_expand
Name:           rust-uu_expand
Version:        0.7.0
Release:        1%{?dist}
Summary:        expand ~ (uutils) convert input tabs to spaces
License:        MIT
URL:            https://crates.io/crates/uu_expand
Source0:        https://static.crates.io/crates/uu_expand/uu_expand-%{version}.crate
Patch:          uu_expand-fix-metadata.diff
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
Summary:        expand ~ (uutils) convert input tabs to spaces
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
%files -n rust-uu_expand-devel -f %{oreon_filedir}/rust-uu_expand-devel.list

%changelog

%autochangelog
