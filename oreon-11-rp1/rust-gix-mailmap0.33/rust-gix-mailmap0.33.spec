%global source0_hash a824767d38b81475059cb01f5020a13fb96e7ed6bbf9851c7112b46ada78db48
%bcond check 0
%global debug_package %{nil}
%global crate gix-mailmap
Name:           rust-gix-mailmap0.33
Version:        0.33.2
Release:        1%{?dist}
Summary:        A crate of the gitoxide project for parsing mailmap files
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-mailmap
Source0:        https://static.crates.io/crates/gix-mailmap/gix-mailmap-%{version}.crate
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

%package     -n %{name}+document-features-devel
Summary:        A crate of the gitoxide project for parsing mailmap files
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crate of the gitoxide project for parsing mailmap files
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-gix-mailmap0.33-devel -f %{oreon_filedir}/rust-gix-mailmap0.33-devel.list

%changelog

%autochangelog
