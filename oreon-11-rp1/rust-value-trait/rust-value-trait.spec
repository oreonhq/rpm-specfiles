%global source0_hash dad8db98c1e677797df21ba03fca7d3bf9bec3ca38db930954e4fe6e1ea27eb4
%bcond check 0
%global debug_package %{nil}
%global crate value-trait
Name:           rust-value-trait
Version:        0.8.1
Release:        1%{?dist}
Summary:        Traits to deal with JSONesque values
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/value-trait
Source0:        https://static.crates.io/crates/value-trait/value-trait-%{version}.crate
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
Summary:        Traits to deal with JSONesque values
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+128bit-devel
Summary:        Traits to deal with JSONesque values
BuildArch:      noarch
%description -n %{name}+128bit-devel

This package contains library source intended for building other packages which
use the "128bit" feature of the "%{crate}" crate.

%package     -n %{name}+abi_stable-devel
Summary:        Traits to deal with JSONesque values
BuildArch:      noarch
%description -n %{name}+abi_stable-devel

This package contains library source intended for building other packages which
use the "abi_stable" feature of the "%{crate}" crate.

%package     -n %{name}+c-abi-devel
Summary:        Traits to deal with JSONesque values
BuildArch:      noarch
%description -n %{name}+c-abi-devel

This package contains library source intended for building other packages which
use the "c-abi" feature of the "%{crate}" crate.

%package     -n %{name}+custom-types-devel
Summary:        Traits to deal with JSONesque values
BuildArch:      noarch
%description -n %{name}+custom-types-devel

This package contains library source intended for building other packages which
use the "custom-types" feature of the "%{crate}" crate.

%package     -n %{name}+halfbrown-devel
Summary:        Traits to deal with JSONesque values
BuildArch:      noarch
%description -n %{name}+halfbrown-devel

This package contains library source intended for building other packages which
use the "halfbrown" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        Traits to deal with JSONesque values
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+portable-devel
Summary:        Traits to deal with JSONesque values
BuildArch:      noarch
%description -n %{name}+portable-devel

This package contains library source intended for building other packages which
use the "portable" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-detection-devel
Summary:        Traits to deal with JSONesque values
BuildArch:      noarch
%description -n %{name}+runtime-detection-devel

This package contains library source intended for building other packages which
use the "runtime-detection" feature of the "%{crate}" crate.

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
%files -n rust-value-trait-devel -f %{oreon_filedir}/rust-value-trait-devel.list

%changelog

%autochangelog
