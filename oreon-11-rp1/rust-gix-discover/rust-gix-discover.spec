%global source0_hash ec32a30ec2934735599c2545f30067e80bd255fd3454b52a5d59bc02b52874a3
%bcond check 0
%global debug_package %{nil}
%global crate gix-discover
Name:           rust-gix-discover
Version:        0.55.0
Release:        1%{?dist}
Summary:        Discover git repositories and check if a directory is a git repository
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-discover
Source0:        https://static.crates.io/crates/gix-discover/gix-discover-%{version}.crate
Patch:          gix-discover-fix-metadata-auto.diff
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
Summary:        Discover git repositories and check if a directory is a git repository
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
%files -n rust-gix-discover-devel -f %{oreon_filedir}/rust-gix-discover-devel.list

%changelog

%autochangelog
