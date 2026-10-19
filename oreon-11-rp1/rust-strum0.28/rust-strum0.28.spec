%global source0_hash 9628de9b8791db39ceda2b119bbe13134770b56c138ec1d3af810d045c04f9bd
%bcond check 0
%global debug_package %{nil}
%global crate strum
Name:           rust-strum0.28
Version:        0.28.0
Release:        1%{?dist}
Summary:        Helpful macros for working with enums and strings
License:        MIT
URL:            https://crates.io/crates/strum
Source0:        https://static.crates.io/crates/strum/strum-%{version}.crate
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
Summary:        Helpful macros for working with enums and strings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Helpful macros for working with enums and strings
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+phf-devel
Summary:        Helpful macros for working with enums and strings
BuildArch:      noarch
%description -n %{name}+phf-devel

This package contains library source intended for building other packages which
use the "phf" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Helpful macros for working with enums and strings
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+strum_macros-devel
Summary:        Helpful macros for working with enums and strings
BuildArch:      noarch
%description -n %{name}+strum_macros-devel

This package contains library source intended for building other packages which
use the "strum_macros" feature of the "%{crate}" crate.

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
%files -n rust-strum0.28-devel -f %{oreon_filedir}/rust-strum0.28-devel.list

%changelog

%autochangelog
