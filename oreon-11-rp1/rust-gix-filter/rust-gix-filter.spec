%global source0_hash 9c30b28d957e2e6f1e1bbfbfd26b8e0bb0aab68d8a5e730fb4fd3049943575e3
%bcond check 0
%global debug_package %{nil}
%global crate gix-filter
Name:           rust-gix-filter
Version:        0.34.0
Release:        1%{?dist}
Summary:        Of the gitoxide project implementing git filters
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-filter
Source0:        https://static.crates.io/crates/gix-filter/gix-filter-%{version}.crate
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
Summary:        Of the gitoxide project implementing git filters
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Of the gitoxide project implementing git filters
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Of the gitoxide project implementing git filters
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha256-devel
Summary:        Of the gitoxide project implementing git filters
BuildArch:      noarch
%description -n %{name}+sha256-devel

This package contains library source intended for building other packages which
use the "sha256" feature of the "%{crate}" crate.

%package     -n %{name}+test-helper-devel
Summary:        Of the gitoxide project implementing git filters
BuildArch:      noarch
%description -n %{name}+test-helper-devel

This package contains library source intended for building other packages which
use the "test-helper" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f test-helper
%install
%cargo_install -f test-helper
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f test-helper
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-gix-filter-devel -f %{oreon_filedir}/rust-gix-filter-devel.list

%changelog

%autochangelog
