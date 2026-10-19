%global source0_hash a8894febbff9f758034a5b8e12d87918f56dfc64a8e1fe757d65e29041538d93
%bcond check 0
%global debug_package %{nil}
%global crate block-padding
Name:           rust-block-padding0.3
Version:        0.3.3
Release:        1%{?dist}
Summary:        Padding and unpadding of messages divided into blocks.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/block-padding
Source0:        https://static.crates.io/crates/block-padding/block-padding-%{version}.crate
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

%package     -n %{name}+std-devel
Summary:        Padding and unpadding of messages divided into blocks.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-block-padding0.3-devel -f %{oreon_filedir}/rust-block-padding0.3-devel.list

%changelog

%autochangelog
