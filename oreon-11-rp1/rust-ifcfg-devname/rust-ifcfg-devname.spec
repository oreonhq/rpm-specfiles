%global source0_hash 673ee7820fb908d8e94f06f35cbb77f8c377ff5504ff15032485e9365f051849
%bcond check 0
%global crate ifcfg-devname
Name:           rust-ifcfg-devname
Version:        1.1.1
Release:        1%{?dist}
Summary:        Udev helper utility that provides network interface naming
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/ifcfg-devname
Source0:        https://static.crates.io/crates/ifcfg-devname/ifcfg-devname-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Udev helper utility that provides network interface naming
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND GPL-3.0-or-later AND (Unlicense OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Udev helper utility that provides network interface naming
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
%files -n ifcfg-devname -f %{oreon_filedir}/ifcfg-devname.list
%files -n rust-ifcfg-devname-devel -f %{oreon_filedir}/rust-ifcfg-devname-devel.list

%changelog

%autochangelog
