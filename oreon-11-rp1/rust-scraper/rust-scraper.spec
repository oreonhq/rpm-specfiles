%global source0_hash 761fb705fdf625482d2ed91d3f0559dcfeab2798fe2771c69560a774865d0802
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate scraper
Name:           rust-scraper
Version:        0.19.1
Release:        1%{?dist}
Summary:        HTML parsing and querying with CSS selectors
License:        ISC
URL:            https://crates.io/crates/scraper
Source0:        https://static.crates.io/crates/scraper/scraper-%{version}.crate
Patch:          scraper-fix-metadata.diff
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
Summary:        HTML parsing and querying with CSS selectors
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+atomic-devel
Summary:        HTML parsing and querying with CSS selectors
BuildArch:      noarch
%description -n %{name}+atomic-devel

This package contains library source intended for building other packages which
use the "atomic" feature of the "%{crate}" crate.

%package     -n %{name}+deterministic-devel
Summary:        HTML parsing and querying with CSS selectors
BuildArch:      noarch
%description -n %{name}+deterministic-devel

This package contains library source intended for building other packages which
use the "deterministic" feature of the "%{crate}" crate.

%package     -n %{name}+errors-devel
Summary:        HTML parsing and querying with CSS selectors
BuildArch:      noarch
%description -n %{name}+errors-devel

This package contains library source intended for building other packages which
use the "errors" feature of the "%{crate}" crate.

%package     -n %{name}+getopts-devel
Summary:        HTML parsing and querying with CSS selectors
BuildArch:      noarch
%description -n %{name}+getopts-devel

This package contains library source intended for building other packages which
use the "getopts" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        HTML parsing and querying with CSS selectors
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+main-devel
Summary:        HTML parsing and querying with CSS selectors
BuildArch:      noarch
%description -n %{name}+main-devel

This package contains library source intended for building other packages which
use the "main" feature of the "%{crate}" crate.

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
%files -n rust-scraper-devel -f %{oreon_filedir}/rust-scraper-devel.list

%changelog

%autochangelog
