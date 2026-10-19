%global source0_hash a3d13836796375d75d656d70d657d100ca3cf88e3b4bafa14bb1d654facb798f
%bcond check 1
%global debug_package %{nil}
%global crate gengo-language
Name:           rust-gengo-language
Version:        0.15.0
Release:        1%{?dist}
Summary:        Get the language distribution stats of your repository
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gengo-language
Source0:        https://static.crates.io/crates/gengo-language/gengo-language-%{version}.crate
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
Summary:        Get the language distribution stats of your repository
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
%files -n rust-gengo-language-devel -f %{oreon_filedir}/rust-gengo-language-devel.list

%changelog

%autochangelog
