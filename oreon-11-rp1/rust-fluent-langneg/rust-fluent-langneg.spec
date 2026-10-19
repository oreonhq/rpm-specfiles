%global source1_hash b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1
%global source0_hash 1d5439a5e4ef14dc761bfe1d6ecbc4ba6fd698814ee65e7e623fa85aa9348dcc
%bcond check 0
%global debug_package %{nil}
%global crate fluent-langneg
Name:           rust-fluent-langneg
Version:        0.14.2
Release:        1%{?dist}
Summary:        Library for language and locale negotiation
License:        Apache-2.0
URL:            https://crates.io/crates/fluent-langneg
Source0:        https://static.crates.io/crates/fluent-langneg/fluent-langneg-%{version}.crate
Source1:        https://github.com/projectfluent/fluent-langneg-rs/raw/29007f8/LICENSE
Patch:          fluent-langneg-fix-metadata.diff
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
Summary:        Library for language and locale negotiation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cldr-devel
Summary:        Library for language and locale negotiation
BuildArch:      noarch
%description -n %{name}+cldr-devel

This package contains library source intended for building other packages which
use the "cldr" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-fluent-langneg-devel -f %{oreon_filedir}/rust-fluent-langneg-devel.list

%changelog

%autochangelog
