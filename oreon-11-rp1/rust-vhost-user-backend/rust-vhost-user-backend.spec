%global source1_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash e183205a9ba7cb9c47fcb0fc0a07fc295a110efbb11ab78ad0d793b0a38a7bde
%bcond check 0
%global debug_package %{nil}
%global crate vhost-user-backend
Name:           rust-vhost-user-backend
Version:        0.20.0
Release:        1%{?dist}
Summary:        Framework to build vhost-user backend service daemon
License:        Apache-2.0
URL:            https://crates.io/crates/vhost-user-backend
Source0:        https://static.crates.io/crates/vhost-user-backend/vhost-user-backend-%{version}.crate
Source1:        https://raw.githubusercontent.com/rust-vmm/vhost/main/LICENSE
ExcludeArch:    %{ix86}
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
Summary:        Framework to build vhost-user backend service daemon
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+postcopy-devel
Summary:        Framework to build vhost-user backend service daemon
BuildArch:      noarch
%description -n %{name}+postcopy-devel

This package contains library source intended for building other packages which
use the "postcopy" feature of the "%{crate}" crate.

%package     -n %{name}+userfaultfd-devel
Summary:        Framework to build vhost-user backend service daemon
BuildArch:      noarch
%description -n %{name}+userfaultfd-devel

This package contains library source intended for building other packages which
use the "userfaultfd" feature of the "%{crate}" crate.

%package     -n %{name}+xen-devel
Summary:        Framework to build vhost-user backend service daemon
BuildArch:      noarch
%description -n %{name}+xen-devel

This package contains library source intended for building other packages which
use the "xen" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-vhost-user-backend-devel -f %{oreon_filedir}/rust-vhost-user-backend-devel.list

%changelog

%autochangelog
