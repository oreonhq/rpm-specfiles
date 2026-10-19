%global source0_hash 27004e6fc625e7a1a3bfbed4997a3372f59f66a895313c23d50af2c5ea6bab89
%bcond check 0
%global debug_package %{nil}
%global crate av1-grain
Name:           rust-av1-grain
Version:        0.5.0
Release:        1%{?dist}
Summary:        Helpers for generating and parsing AV1 film grain data
License:        BSD-2-Clause
URL:            https://crates.io/crates/av1-grain
Source0:        https://static.crates.io/crates/av1-grain/av1-grain-%{version}.crate
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
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+create-devel
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+create-devel

This package contains library source intended for building other packages which
use the "create" feature of the "%{crate}" crate.

%package     -n %{name}+diff-devel
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+diff-devel

This package contains library source intended for building other packages which
use the "diff" feature of the "%{crate}" crate.

%package     -n %{name}+estimate-devel
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+estimate-devel

This package contains library source intended for building other packages which
use the "estimate" feature of the "%{crate}" crate.

%package     -n %{name}+nom-devel
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+nom-devel

This package contains library source intended for building other packages which
use the "nom" feature of the "%{crate}" crate.

%package     -n %{name}+num-rational-devel
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+num-rational-devel

This package contains library source intended for building other packages which
use the "num-rational" feature of the "%{crate}" crate.

%package     -n %{name}+parse-devel
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+parse-devel

This package contains library source intended for building other packages which
use the "parse" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+v_frame-devel
Summary:        Helpers for generating and parsing AV1 film grain data
BuildArch:      noarch
%description -n %{name}+v_frame-devel

This package contains library source intended for building other packages which
use the "v_frame" feature of the "%{crate}" crate.

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
%files -n rust-av1-grain-devel -f %{oreon_filedir}/rust-av1-grain-devel.list

%changelog

%autochangelog
