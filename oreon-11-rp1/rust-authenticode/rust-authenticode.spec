%global source0_hash 86c421a87e3dd1a3024c86e0787106b6ba40d9b434fe0ebeffbd24a242dc144d
%bcond check 1
%global debug_package %{nil}
%global crate authenticode
Name:           rust-authenticode
Version:        0.5.0
Release:        1%{?dist}
Summary:        Library for working with Authenticode (no-std)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/authenticode
Source0:        https://static.crates.io/crates/authenticode/authenticode-%{version}.crate
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
Summary:        Library for working with Authenticode (no-std)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+object-devel
Summary:        Library for working with Authenticode (no-std)
BuildArch:      noarch
%description -n %{name}+object-devel

This package contains library source intended for building other packages which
use the "object" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library for working with Authenticode (no-std)
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
%files -n rust-authenticode-devel -f %{oreon_filedir}/rust-authenticode-devel.list

%changelog

%autochangelog
