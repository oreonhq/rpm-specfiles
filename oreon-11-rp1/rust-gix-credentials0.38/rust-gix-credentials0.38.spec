%global source0_hash e8a0fcfcd73229d1a9c34e04edd05dbcb80364ec6f3788d24c546de2916671eb
%bcond check 0
%global debug_package %{nil}
%global crate gix-credentials
Name:           rust-gix-credentials0.38
Version:        0.38.2
Release:        1%{?dist}
Summary:        A crate of the gitoxide project to interact with git credentials helpers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-credentials
Source0:        https://static.crates.io/crates/gix-credentials/gix-credentials-%{version}.crate
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
Summary:        A crate of the gitoxide project to interact with git credentials helpers
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crate of the gitoxide project to interact with git credentials helpers
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
%files -n rust-gix-credentials0.38-devel -f %{oreon_filedir}/rust-gix-credentials0.38-devel.list

%changelog

%autochangelog
