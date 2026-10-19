%global source0_hash 0c6b5c64445ba8094a6ab0c3cd2ad323e07171012d9c98b0b15651daf1787a10
%bcond check 0
%global debug_package %{nil}
%global crate structopt
Name:           rust-structopt
Version:        0.3.26
Release:        1%{?dist}
Summary:        Parse command line argument by defining a struct
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/structopt
Source0:        https://static.crates.io/crates/structopt/structopt-%{version}.crate
ExclusiveArch:  %{rust_arches}
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
Summary:        Parse command line argument by defining a struct
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        Parse command line argument by defining a struct
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Parse command line argument by defining a struct
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+doc-devel
Summary:        Parse command line argument by defining a struct
BuildArch:      noarch
%description -n %{name}+doc-devel

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%package     -n %{name}+no_cargo-devel
Summary:        Parse command line argument by defining a struct
BuildArch:      noarch
%description -n %{name}+no_cargo-devel

This package contains library source intended for building other packages which
use the "no_cargo" feature of the "%{crate}" crate.

%package     -n %{name}+suggestions-devel
Summary:        Parse command line argument by defining a struct
BuildArch:      noarch
%description -n %{name}+suggestions-devel

This package contains library source intended for building other packages which
use the "suggestions" feature of the "%{crate}" crate.

%package     -n %{name}+wrap_help-devel
Summary:        Parse command line argument by defining a struct
BuildArch:      noarch
%description -n %{name}+wrap_help-devel

This package contains library source intended for building other packages which
use the "wrap_help" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-devel
Summary:        Parse command line argument by defining a struct
BuildArch:      noarch
%description -n %{name}+yaml-devel

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

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

%cargo_test -- -- --skip flatten_twice --skip ui
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-structopt-devel -f %{oreon_filedir}/rust-structopt-devel.list

%changelog

%autochangelog
