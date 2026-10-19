%global source0_hash d9b39be18770d11421cdb1b9947a45dd3f37e93092cbf377614828a319d5fee8
%bcond check 0
%global debug_package %{nil}
%global crate atty
Name:           rust-atty
Version:        0.2.14
Release:        1%{?dist}
Summary:        A simple interface for querying atty
License:        MIT
URL:            https://crates.io/crates/atty
Source0:        https://static.crates.io/crates/atty/atty-%{version}.crate
Patch:          atty-fix-metadata-auto.diff
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
Summary:        A simple interface for querying atty
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
%files -n rust-atty-devel -f %{oreon_filedir}/rust-atty-devel.list

%changelog

%autochangelog
