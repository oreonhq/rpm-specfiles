%global source0_hash 8fec0f0aef304996cf250b31b5a10dee7980c85da9d759361292b8bca5a18f06
%bcond check 1
%global debug_package %{nil}
%global crate strum
Name:           rust-strum0.26
Version:        0.26.3
Release:        1%{?dist}
Summary:        Helpful macros for working with enums and strings
License:        MIT
URL:            https://crates.io/crates/strum
Source0:        https://static.crates.io/crates/strum/strum-%{version}.crate
Patch:          strum-fix-metadata.diff
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

%cargo_build -f derive
%install
%cargo_install -f derive
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f derive
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-strum0.26-devel -f %{oreon_filedir}/rust-strum0.26-devel.list

%changelog

%autochangelog
