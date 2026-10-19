%global source0_hash a97512398a192253d9e9e164834be6469723b6b9502392c071a87978d4bb0b48
%bcond check 1
%global debug_package %{nil}
%global crate ovs-unixctl
Name:           rust-ovs-unixctl
Version:        0.1.0
Release:        1%{?dist}
Summary:        Control OVS daemons using the Unixctl interface (a.k.a ovs-appctl)
License:        LGPL-2.1-or-later
URL:            https://crates.io/crates/ovs-unixctl
Source0:        https://static.crates.io/crates/ovs-unixctl/ovs-unixctl-%{version}.crate
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
Summary:        Control OVS daemons using the Unixctl interface (a.k.a ovs-appctl)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+test_integration-devel
Summary:        Control OVS daemons using the Unixctl interface (a.k.a ovs-appctl)
BuildArch:      noarch
%description -n %{name}+test_integration-devel

This package contains library source intended for building other packages which
use the "test_integration" feature of the "%{crate}" crate.

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
%files -n rust-ovs-unixctl-devel -f %{oreon_filedir}/rust-ovs-unixctl-devel.list

%changelog

%autochangelog
