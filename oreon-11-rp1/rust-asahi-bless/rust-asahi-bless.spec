%global source0_hash 1b1f6905316fcd1ec30e2ded7bf1ba1a8ba092f9d13bdf65fc98a5e528353112
%bcond check 0
%global crate asahi-bless
Name:           rust-asahi-bless
Version:        0.4.2
Release:        1%{?dist}
Summary:        Tool to select active boot partition on ARM Macs
License:        MIT
URL:            https://crates.io/crates/asahi-bless
Source0:        https://static.crates.io/crates/asahi-bless/asahi-bless-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Tool to select active boot partition on ARM Macs
License:        MIT AND Zlib AND (Apache-2.0 OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Tool to select active boot partition on ARM Macs
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
%files -n asahi-bless -f %{oreon_filedir}/asahi-bless.list
%files -n rust-asahi-bless-devel -f %{oreon_filedir}/rust-asahi-bless-devel.list

%changelog

%autochangelog
