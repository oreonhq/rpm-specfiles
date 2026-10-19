%global source0_hash 7bddcd3bf5144b6392de80e04c347cd7fab2508f6df16a85fc496ecd5cec39bc
%bcond check 0
%global crate names
Name:           rust-names
Version:        0.14.0
Release:        1%{?dist}
Summary:        Random name generator
License:        MIT
URL:            https://crates.io/crates/names
Source0:        https://static.crates.io/crates/names/names-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Random name generator
License:        MIT AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Random name generator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+application-devel
Summary:        Random name generator
BuildArch:      noarch
%description -n %{name}+application-devel

This package contains library source intended for building other packages which
use the "application" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Random name generator
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n names -f %{oreon_filedir}/names.list
%files -n rust-names-devel -f %{oreon_filedir}/rust-names-devel.list

%changelog

%autochangelog
