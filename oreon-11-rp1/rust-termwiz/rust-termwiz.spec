%global source0_hash 4676b37242ccbd1aabf56edb093a4827dc49086c0ffd764a5705899e0f35f8f7
%bcond check 0
%global debug_package %{nil}
%global crate termwiz
Name:           rust-termwiz
Version:        0.23.3
Release:        1%{?dist}
Summary:        Terminal Wizardry for Unix and Windows
License:        MIT
URL:            https://crates.io/crates/termwiz
Source0:        https://static.crates.io/crates/termwiz/termwiz-%{version}.crate
Patch:          termwiz-fix-metadata-auto.diff
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

%package     -n %{name}+cassowary-devel
Summary:        Terminal Wizardry for Unix and Windows
BuildArch:      noarch
%description -n %{name}+cassowary-devel

This package contains library source intended for building other packages which
use the "cassowary" feature of the "%{crate}" crate.

%package     -n %{name}+docs-devel
Summary:        Terminal Wizardry for Unix and Windows
BuildArch:      noarch
%description -n %{name}+docs-devel

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%package     -n %{name}+fnv-devel
Summary:        Terminal Wizardry for Unix and Windows
BuildArch:      noarch
%description -n %{name}+fnv-devel

This package contains library source intended for building other packages which
use the "fnv" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        Terminal Wizardry for Unix and Windows
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Terminal Wizardry for Unix and Windows
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+use_image-devel
Summary:        Terminal Wizardry for Unix and Windows
BuildArch:      noarch
%description -n %{name}+use_image-devel

This package contains library source intended for building other packages which
use the "use_image" feature of the "%{crate}" crate.

%package     -n %{name}+use_serde-devel
Summary:        Terminal Wizardry for Unix and Windows
BuildArch:      noarch
%description -n %{name}+use_serde-devel

This package contains library source intended for building other packages which
use the "use_serde" feature of the "%{crate}" crate.

%package     -n %{name}+widgets-devel
Summary:        Terminal Wizardry for Unix and Windows
BuildArch:      noarch
%description -n %{name}+widgets-devel

This package contains library source intended for building other packages which
use the "widgets" feature of the "%{crate}" crate.

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
%files -n rust-termwiz-devel -f %{oreon_filedir}/rust-termwiz-devel.list

%changelog

%autochangelog
