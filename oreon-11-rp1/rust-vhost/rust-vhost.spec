%global source2_hash 384d909ea26750484e9b5f088aad6de12a900d62a3fe89b05d29768f639c028d
%global source1_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash 2a4dcad85a129d97d5d4b2f3c47a4affdeedd76bdcd02094bcb5d9b76cac2d05
%bcond check 0
%global debug_package %{nil}
%global crate vhost
Name:           rust-vhost
Version:        0.14.0
Release:        1%{?dist}
Summary:        Pure rust library for vdpa, vhost and vhost-user
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/vhost
Source0:        https://static.crates.io/crates/vhost/vhost-%{version}.crate
Source1:        https://raw.githubusercontent.com/rust-vmm/vhost/main/LICENSE
Source2:        https://raw.githubusercontent.com/rust-vmm/vhost/main/LICENSE-BSD-3-Clause
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
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+postcopy-devel
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+postcopy-devel

This package contains library source intended for building other packages which
use the "postcopy" feature of the "%{crate}" crate.

%package     -n %{name}+test-utils-devel
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+test-utils-devel

This package contains library source intended for building other packages which
use the "test-utils" feature of the "%{crate}" crate.

%package     -n %{name}+vhost-kern-devel
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+vhost-kern-devel

This package contains library source intended for building other packages which
use the "vhost-kern" feature of the "%{crate}" crate.

%package     -n %{name}+vhost-net-devel
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+vhost-net-devel

This package contains library source intended for building other packages which
use the "vhost-net" feature of the "%{crate}" crate.

%package     -n %{name}+vhost-user-devel
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+vhost-user-devel

This package contains library source intended for building other packages which
use the "vhost-user" feature of the "%{crate}" crate.

%package     -n %{name}+vhost-user-backend-devel
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+vhost-user-backend-devel

This package contains library source intended for building other packages which
use the "vhost-user-backend" feature of the "%{crate}" crate.

%package     -n %{name}+vhost-user-frontend-devel
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+vhost-user-frontend-devel

This package contains library source intended for building other packages which
use the "vhost-user-frontend" feature of the "%{crate}" crate.

%package     -n %{name}+vhost-vdpa-devel
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+vhost-vdpa-devel

This package contains library source intended for building other packages which
use the "vhost-vdpa" feature of the "%{crate}" crate.

%package     -n %{name}+vhost-vsock-devel
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+vhost-vsock-devel

This package contains library source intended for building other packages which
use the "vhost-vsock" feature of the "%{crate}" crate.

%package     -n %{name}+xen-devel
Summary:        Pure rust library for vdpa, vhost and vhost-user
BuildArch:      noarch
%description -n %{name}+xen-devel

This package contains library source intended for building other packages which
use the "xen" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp %{SOURCE1} .
cp %{SOURCE2} .
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
%files -n rust-vhost-devel -f %{oreon_filedir}/rust-vhost-devel.list

%changelog

%autochangelog
