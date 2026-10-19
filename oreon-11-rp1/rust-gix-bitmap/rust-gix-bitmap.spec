%global source0_hash f17013c7ef5cb95ebb4bf4978201e6a8a42ffea9d666fd5388f1b7e742307d80
%bcond check 0
%global debug_package %{nil}
%global crate gix-bitmap
Name:           rust-gix-bitmap
Version:        0.4.0
Release:        1%{?dist}
Summary:        A crate of the gitoxide project dedicated implementing the standard g...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-bitmap
Source0:        https://static.crates.io/crates/gix-bitmap/gix-bitmap-%{version}.crate
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
Summary:        A crate of the gitoxide project dedicated implementing the standard g...
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
%files -n rust-gix-bitmap-devel -f %{oreon_filedir}/rust-gix-bitmap-devel.list

%changelog

%autochangelog
