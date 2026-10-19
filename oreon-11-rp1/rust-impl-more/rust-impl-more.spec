%global source0_hash e8a5a9a0ff0086c7a148acb942baaabeadf9504d10400b5a05645853729b9cd2
%bcond check 1
%global debug_package %{nil}
%global crate impl-more
Name:           rust-impl-more
Version:        0.1.9
Release:        1%{?dist}
Summary:        Concise, declarative trait implementation macros
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/impl-more
Source0:        https://static.crates.io/crates/impl-more/impl-more-%{version}.crate
Patch:          impl-more-fix-metadata.diff
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
Summary:        Concise, declarative trait implementation macros
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
%files -n rust-impl-more-devel -f %{oreon_filedir}/rust-impl-more-devel.list

%changelog

%autochangelog
