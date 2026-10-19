%global source0_hash 3ded4057c258ba199e2d26386d3af3780957ecaee6c4ef4041c6b4b8b97c0b06
%bcond check 0
%global debug_package %{nil}
%global crate bitflags
Name:           rust-bitflags
Version:        2.13.2
Release:        1%{?dist}
Summary:        Macro to generate structures which behave like bitflags
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bitflags
Source0:        https://static.crates.io/crates/bitflags/bitflags-%{version}.crate
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
Summary:        Macro to generate structures which behave like bitflags
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Macro to generate structures which behave like bitflags
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Macro to generate structures which behave like bitflags
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+example_generated-devel
Summary:        Macro to generate structures which behave like bitflags
BuildArch:      noarch
%description -n %{name}+example_generated-devel

This package contains library source intended for building other packages which
use the "example_generated" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Macro to generate structures which behave like bitflags
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_core-devel
Summary:        Macro to generate structures which behave like bitflags
BuildArch:      noarch
%description -n %{name}+serde_core-devel

This package contains library source intended for building other packages which
use the "serde_core" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Macro to generate structures which behave like bitflags
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
%files -n rust-bitflags-devel -f %{oreon_filedir}/rust-bitflags-devel.list

%changelog

%autochangelog
