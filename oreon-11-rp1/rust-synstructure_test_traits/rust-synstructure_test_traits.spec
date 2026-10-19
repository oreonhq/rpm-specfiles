%global source0_hash c6e0c1828b7994d45bbef3cbbe56a6157c42db92b82b1a5bf22fb09996d06eac
%global debug_package %{nil}
%bcond check 1
%global crate synstructure_test_traits
Name:           rust-synstructure_test_traits
Version:        0.1.0
Release:        1%{?dist}
Summary:        Helper test traits for synstructure doctests
License:        MIT
URL:            https://crates.io/crates/synstructure_test_traits
Source0:        https://static.crates.io/crates/synstructure_test_traits/synstructure_test_traits-%{version}.crate
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
Summary:        Helper test traits for synstructure doctests
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-synstructure_test_traits-devel -f %{oreon_filedir}/rust-synstructure_test_traits-devel.list

%changelog

%autochangelog
