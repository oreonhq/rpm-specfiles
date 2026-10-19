%global source0_hash 7c6ba7d4eec39eaa9ab24d44a0e73a7949a1095a8b3f3abb11eddf27dbb56a53
%bcond check 1
%global debug_package %{nil}
%global crate ego-tree
Name:           rust-ego-tree0.9
Version:        0.9.0
Release:        1%{?dist}
Summary:        Vec-backed ID-tree
License:        ISC
URL:            https://crates.io/crates/ego-tree
Source0:        https://static.crates.io/crates/ego-tree/ego-tree-%{version}.crate
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
Summary:        Vec-backed ID-tree
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Vec-backed ID-tree
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
%files -n rust-ego-tree0.9-devel -f %{oreon_filedir}/rust-ego-tree0.9-devel.list

%changelog

%autochangelog
