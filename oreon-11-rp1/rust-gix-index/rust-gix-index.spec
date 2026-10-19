%global source0_hash 632e16cb48b0e88a747e106924cb2765194105d8070a7a961b0d080ed806c632
%bcond check 0
%global debug_package %{nil}
%global crate gix-index
Name:           rust-gix-index
Version:        0.55.0
Release:        1%{?dist}
Summary:        A work-in-progress crate of the gitoxide project dedicated implementi...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-index
Source0:        https://static.crates.io/crates/gix-index/gix-index-%{version}.crate
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
Summary:        A work-in-progress crate of the gitoxide project dedicated implementi...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A work-in-progress crate of the gitoxide project dedicated implementi...
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
%files -n rust-gix-index-devel -f %{oreon_filedir}/rust-gix-index-devel.list

%changelog

%autochangelog
