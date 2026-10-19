%global source0_hash ae6371b8bdc8b7d3959e9cf7b22d4435ef3e79e138688421ec654acf8c81b008
%bcond check 0
%global debug_package %{nil}
%global crate clap_derive
Name:           rust-clap_derive3
Version:        3.2.25
Release:        1%{?dist}
Summary:        Parse command line argument by defining a struct, derive crate.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/clap_derive
Source0:        https://static.crates.io/crates/clap_derive/clap_derive-%{version}.crate
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
Summary:        Parse command line argument by defining a struct, derive crate.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Parse command line argument by defining a struct, derive crate.
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+deprecated-devel
Summary:        Parse command line argument by defining a struct, derive crate.
BuildArch:      noarch
%description -n %{name}+deprecated-devel

This package contains library source intended for building other packages which
use the "deprecated" feature of the "%{crate}" crate.

%package     -n %{name}+raw-deprecated-devel
Summary:        Parse command line argument by defining a struct, derive crate.
BuildArch:      noarch
%description -n %{name}+raw-deprecated-devel

This package contains library source intended for building other packages which
use the "raw-deprecated" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-v4-devel
Summary:        Parse command line argument by defining a struct, derive crate.
BuildArch:      noarch
%description -n %{name}+unstable-v4-devel

This package contains library source intended for building other packages which
use the "unstable-v4" feature of the "%{crate}" crate.

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
%files -n rust-clap_derive3-devel -f %{oreon_filedir}/rust-clap_derive3-devel.list

%changelog

%autochangelog
