%global source0_hash b4ca4bea16ffc3f443cf7d866912118196bfef4c6a1556ca00f9f9b00bb43f7c
%bcond check 0
%global debug_package %{nil}
%global crate multiversion
Name:           rust-multiversion
Version:        0.9.0
Release:        1%{?dist}
Summary:        Easy function multiversioning
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/multiversion
Source0:        https://static.crates.io/crates/multiversion/multiversion-%{version}.crate
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
Summary:        Easy function multiversioning
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Easy function multiversioning
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Easy function multiversioning
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+target-features-devel
Summary:        Easy function multiversioning
BuildArch:      noarch
%description -n %{name}+target-features-devel

This package contains library source intended for building other packages which
use the "target-features" feature of the "%{crate}" crate.

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
%files -n rust-multiversion-devel -f %{oreon_filedir}/rust-multiversion-devel.list

%changelog

%autochangelog
