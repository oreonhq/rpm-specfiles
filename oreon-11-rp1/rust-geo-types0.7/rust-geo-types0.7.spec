%global source0_hash 94776032c45f950d30a13af6113c2ad5625316c9abfbccee4dd5a6695f8fe0f5
%bcond check 0
%global debug_package %{nil}
%global crate geo-types
Name:           rust-geo-types0.7
Version:        0.7.20
Release:        1%{?dist}
Summary:        Geospatial primitive data types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/geo-types
Source0:        https://static.crates.io/crates/geo-types/geo-types-%{version}.crate
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
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__allow_deprecated_features-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+__allow_deprecated_features-devel

This package contains library source intended for building other packages which
use the "__allow_deprecated_features" feature of the "%{crate}" crate.

%package     -n %{name}+approx-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+approx-devel

This package contains library source intended for building other packages which
use the "approx" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+multithreading-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+multithreading-devel

This package contains library source intended for building other packages which
use the "multithreading" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+rstar-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+rstar-devel

This package contains library source intended for building other packages which
use the "rstar" feature of the "%{crate}" crate.

%package     -n %{name}+rstar_0_10-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+rstar_0_10-devel

This package contains library source intended for building other packages which
use the "rstar_0_10" feature of the "%{crate}" crate.

%package     -n %{name}+rstar_0_11-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+rstar_0_11-devel

This package contains library source intended for building other packages which
use the "rstar_0_11" feature of the "%{crate}" crate.

%package     -n %{name}+rstar_0_12-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+rstar_0_12-devel

This package contains library source intended for building other packages which
use the "rstar_0_12" feature of the "%{crate}" crate.

%package     -n %{name}+rstar_0_8-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+rstar_0_8-devel

This package contains library source intended for building other packages which
use the "rstar_0_8" feature of the "%{crate}" crate.

%package     -n %{name}+rstar_0_9-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+rstar_0_9-devel

This package contains library source intended for building other packages which
use the "rstar_0_9" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+spade_2-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+spade_2-devel

This package contains library source intended for building other packages which
use the "spade_2" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+use-rstar-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+use-rstar-devel

This package contains library source intended for building other packages which
use the "use-rstar" feature of the "%{crate}" crate.

%package     -n %{name}+use-rstar_0_10-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+use-rstar_0_10-devel

This package contains library source intended for building other packages which
use the "use-rstar_0_10" feature of the "%{crate}" crate.

%package     -n %{name}+use-rstar_0_11-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+use-rstar_0_11-devel

This package contains library source intended for building other packages which
use the "use-rstar_0_11" feature of the "%{crate}" crate.

%package     -n %{name}+use-rstar_0_12-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+use-rstar_0_12-devel

This package contains library source intended for building other packages which
use the "use-rstar_0_12" feature of the "%{crate}" crate.

%package     -n %{name}+use-rstar_0_8-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+use-rstar_0_8-devel

This package contains library source intended for building other packages which
use the "use-rstar_0_8" feature of the "%{crate}" crate.

%package     -n %{name}+use-rstar_0_9-devel
Summary:        Geospatial primitive data types
BuildArch:      noarch
%description -n %{name}+use-rstar_0_9-devel

This package contains library source intended for building other packages which
use the "use-rstar_0_9" feature of the "%{crate}" crate.

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
%files -n rust-geo-types0.7-devel -f %{oreon_filedir}/rust-geo-types0.7-devel.list

%changelog

%autochangelog
