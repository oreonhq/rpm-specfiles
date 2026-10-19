%global source0_hash 92d61dc1b14bc89adf7bae0ec0486b6e130f72021d0e80b56ba04148693bc6a9
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_uptime
Name:           rust-uu_uptime
Version:        0.7.0
Release:        1%{?dist}
Summary:        uptime ~ (uutils) display dynamic system information
License:        MIT
URL:            https://crates.io/crates/uu_uptime
Source0:        https://static.crates.io/crates/uu_uptime/uu_uptime-%{version}.crate
Patch:          uu_uptime-fix-metadata-auto.diff
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
Summary:        uptime ~ (uutils) display dynamic system information
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+feat_systemd_logind-devel
Summary:        uptime ~ (uutils) display dynamic system information
BuildArch:      noarch
%description -n %{name}+feat_systemd_logind-devel

This package contains library source intended for building other packages which
use the "feat_systemd_logind" feature of the "%{crate}" crate.

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
%files -n rust-uu_uptime-devel -f %{oreon_filedir}/rust-uu_uptime-devel.list

%changelog

%autochangelog
