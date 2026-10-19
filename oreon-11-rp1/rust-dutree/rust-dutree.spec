%global source0_hash 1d55fc4eb114ad99f46b3b989aad4d809f8f7e31dc34a69b95a33a148f802198
%bcond check 0
%global crate dutree
Name:           rust-dutree
Version:        0.2.18
Release:        1%{?dist}
Summary:        Command line tool to analyze disk usage
License:        GPL-3.0-only
URL:            https://crates.io/crates/dutree
Source0:        https://static.crates.io/crates/dutree/dutree-%{version}.crate
Patch:          dutree-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Command line tool to analyze disk usage
License:        GPL-3.0-only AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Command line tool to analyze disk usage
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n dutree -f %{oreon_filedir}/dutree.list
%files -n rust-dutree-devel -f %{oreon_filedir}/rust-dutree-devel.list

%changelog

%autochangelog
