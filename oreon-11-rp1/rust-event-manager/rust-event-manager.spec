%global source0_hash 13bdac971eb2efaceffca0976058ab80c715945cc565c8a4aa1ed3bb0dc8d0e4
%bcond check 1
%global debug_package %{nil}
%global crate event-manager
Name:           rust-event-manager
Version:        0.4.2
Release:        1%{?dist}
Summary:        Abstractions for implementing event based systems
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/event-manager
Source0:        https://static.crates.io/crates/event-manager/event-manager-%{version}.crate
Patch:          event-manager-fix-metadata.diff
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
Summary:        Abstractions for implementing event based systems
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+remote_endpoint-devel
Summary:        Abstractions for implementing event based systems
BuildArch:      noarch
%description -n %{name}+remote_endpoint-devel

This package contains library source intended for building other packages which
use the "remote_endpoint" feature of the "%{crate}" crate.

%package     -n %{name}+test_utilities-devel
Summary:        Abstractions for implementing event based systems
BuildArch:      noarch
%description -n %{name}+test_utilities-devel

This package contains library source intended for building other packages which
use the "test_utilities" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-event-manager-devel -f %{oreon_filedir}/rust-event-manager-devel.list

%changelog

%autochangelog
