%global source0_hash 43c2fa4cf4f555a959216bea01be5f0f1ae106f7c311b5c187c6c377fd1864c4
%bcond check 0
%global crate busd
Name:           rust-busd
Version:        0.3.1
Release:        1%{?dist}
Summary:        D-Bus bus (broker) implementation
License:        MIT
URL:            https://crates.io/crates/busd
Source0:        https://static.crates.io/crates/busd/busd-%{version}.crate
Patch:          busd-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        D-Bus bus (broker) implementation
License:        ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        D-Bus bus (broker) implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-subscriber-devel
Summary:        D-Bus bus (broker) implementation
BuildArch:      noarch
%description -n %{name}+tracing-subscriber-devel

This package contains library source intended for building other packages which
use the "tracing-subscriber" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm LICENSE
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
%files -n busd -f %{oreon_filedir}/busd.list
%files -n rust-busd-devel -f %{oreon_filedir}/rust-busd-devel.list

%changelog

%autochangelog
