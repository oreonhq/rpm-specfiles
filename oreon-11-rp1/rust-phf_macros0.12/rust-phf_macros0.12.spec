%global source0_hash d713258393a82f091ead52047ca779d37e5766226d009de21696c4e667044368
%bcond check 0
%global debug_package %{nil}
%global crate phf_macros
Name:           rust-phf_macros0.12
Version:        0.12.1
Release:        1%{?dist}
Summary:        Macros to generate types in the phf crate
License:        MIT
URL:            https://crates.io/crates/phf_macros
Source0:        https://static.crates.io/crates/phf_macros/phf_macros-%{version}.crate
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

%package     -n %{name}+uncased-devel
Summary:        Macros to generate types in the phf crate
BuildArch:      noarch
%description -n %{name}+uncased-devel

This package contains library source intended for building other packages which
use the "uncased" feature of the "%{crate}" crate.

%package     -n %{name}+uncased_-devel
Summary:        Macros to generate types in the phf crate
BuildArch:      noarch
%description -n %{name}+uncased_-devel

This package contains library source intended for building other packages which
use the "uncased_" feature of the "%{crate}" crate.

%package     -n %{name}+unicase-devel
Summary:        Macros to generate types in the phf crate
BuildArch:      noarch
%description -n %{name}+unicase-devel

This package contains library source intended for building other packages which
use the "unicase" feature of the "%{crate}" crate.

%package     -n %{name}+unicase_-devel
Summary:        Macros to generate types in the phf crate
BuildArch:      noarch
%description -n %{name}+unicase_-devel

This package contains library source intended for building other packages which
use the "unicase_" feature of the "%{crate}" crate.

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
%files -n rust-phf_macros0.12-devel -f %{oreon_filedir}/rust-phf_macros0.12-devel.list

%changelog

%autochangelog
