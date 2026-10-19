%global source0_hash b99c867582a6d5d0eb6dd394ce32b7d8e75e79a76cf532fba7b52c94b0ca4ae0
%bcond check 1
%global debug_package %{nil}
%global crate rusty_paserk
Name:           rust-rusty_paserk
Version:        0.5.0
Release:        1%{?dist}
Summary:        Platform Agnostic Serializable Keys
License:        MIT
URL:            https://crates.io/crates/rusty_paserk
Source0:        https://static.crates.io/crates/rusty_paserk/rusty_paserk-%{version}.crate
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
Summary:        Platform Agnostic Serializable Keys
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Platform Agnostic Serializable Keys
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Platform Agnostic Serializable Keys
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+v3-devel
Summary:        Platform Agnostic Serializable Keys
BuildArch:      noarch
%description -n %{name}+v3-devel

This package contains library source intended for building other packages which
use the "v3" feature of the "%{crate}" crate.

%package     -n %{name}+v4-devel
Summary:        Platform Agnostic Serializable Keys
BuildArch:      noarch
%description -n %{name}+v4-devel

This package contains library source intended for building other packages which
use the "v4" feature of the "%{crate}" crate.

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
%files -n rust-rusty_paserk-devel -f %{oreon_filedir}/rust-rusty_paserk-devel.list

%changelog

%autochangelog
