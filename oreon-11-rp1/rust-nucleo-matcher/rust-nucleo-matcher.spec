%global source0_hash bf33f538733d1a5a3494b836ba913207f14d9d4a1d3cd67030c5061bdd2cac85
%bcond check 1
%global debug_package %{nil}
%global crate nucleo-matcher
Name:           rust-nucleo-matcher
Version:        0.3.1
Release:        1%{?dist}
Summary:        Plug and play high performance fuzzy matcher
License:        MPL-2.0
URL:            https://crates.io/crates/nucleo-matcher
Source0:        https://static.crates.io/crates/nucleo-matcher/nucleo-matcher-%{version}.crate
Patch:          nucleo-matcher-fix-metadata.diff
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
Summary:        Plug and play high performance fuzzy matcher
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-casefold-devel
Summary:        Plug and play high performance fuzzy matcher
BuildArch:      noarch
%description -n %{name}+unicode-casefold-devel

This package contains library source intended for building other packages which
use the "unicode-casefold" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-normalization-devel
Summary:        Plug and play high performance fuzzy matcher
BuildArch:      noarch
%description -n %{name}+unicode-normalization-devel

This package contains library source intended for building other packages which
use the "unicode-normalization" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-segmentation-devel
Summary:        Plug and play high performance fuzzy matcher
BuildArch:      noarch
%description -n %{name}+unicode-segmentation-devel

This package contains library source intended for building other packages which
use the "unicode-segmentation" feature of the "%{crate}" crate.

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
%files -n rust-nucleo-matcher-devel -f %{oreon_filedir}/rust-nucleo-matcher-devel.list

%changelog

%autochangelog
