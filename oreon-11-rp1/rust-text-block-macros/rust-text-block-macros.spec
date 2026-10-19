%global source0_hash 7f8b59b4da1c1717deaf1de80f0179a9d8b4ac91c986d5fd9f4a8ff177b84049
%bcond check 0
%global debug_package %{nil}
%global crate text-block-macros
Name:           rust-text-block-macros
Version:        0.1.1
Release:        1%{?dist}
Summary:        Create a multiline string literal
License:        MIT
URL:            https://crates.io/crates/text-block-macros
Source0:        https://static.crates.io/crates/text-block-macros/text-block-macros-%{version}.crate
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
Summary:        Create a multiline string literal
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
%files -n rust-text-block-macros-devel -f %{oreon_filedir}/rust-text-block-macros-devel.list

%changelog

%autochangelog
