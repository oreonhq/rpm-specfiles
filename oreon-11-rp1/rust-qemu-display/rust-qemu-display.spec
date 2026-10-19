%global source0_hash 683d6f72f46a55ce209b948767a8311fdd3beaccd06c489ad2ae7bf946af19cd
%bcond check 1
%global debug_package %{nil}
%global crate qemu-display
Name:           rust-qemu-display
Version:        0.2.1
Release:        1%{?dist}
Summary:        Helper library to communicate with qemu -display dbus
License:        MIT
URL:            https://crates.io/crates/qemu-display
Source0:        https://static.crates.io/crates/qemu-display/qemu-display-%{version}.crate
Patch:          qemu-display-fix-metadata-auto.diff
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
Summary:        Helper library to communicate with qemu -display dbus
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+qmp-devel
Summary:        Helper library to communicate with qemu -display dbus
BuildArch:      noarch
%description -n %{name}+qmp-devel

This package contains library source intended for building other packages which
use the "qmp" feature of the "%{crate}" crate.

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
%files -n rust-qemu-display-devel -f %{oreon_filedir}/rust-qemu-display-devel.list

%changelog

%autochangelog
