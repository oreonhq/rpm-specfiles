%global source0_hash 7e56ceb44ea13f6bc4ea4e781854f05c63b8c9c240846a971d832ecaca6f9fb6
%bcond check 1
%global crate rpick
Name:           rust-rpick
Version:        0.9.1
Release:        1%{?dist}
Summary:        Helps you pick items from a list by various algorithms
License:        GPL-3.0-only
URL:            https://crates.io/crates/rpick
Source0:        https://static.crates.io/crates/rpick/rpick-%{version}.crate
Patch:          rpick-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Helps you pick items from a list by various algorithms
License:        Apache-2.0 AND BSD-3-Clause AND GPL-3.0-only AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Helps you pick items from a list by various algorithms
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
%files -n rpick -f %{oreon_filedir}/rpick.list
%files -n rust-rpick-devel -f %{oreon_filedir}/rust-rpick-devel.list

%changelog

%autochangelog
