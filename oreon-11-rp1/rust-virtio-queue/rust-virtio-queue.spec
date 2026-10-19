%global source2_hash a6d3ebd1c2f37d4fd83d0676621f695fc0cc2d8c6e646cdbb831b46e0650c208
%global source1_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash fb0479158f863e59323771a1f684d843962f76960b86fecfec2bfa9c8f0f9180
%bcond check 0
%global debug_package %{nil}
%global crate virtio-queue
Name:           rust-virtio-queue
Version:        0.16.0
Release:        1%{?dist}
Summary:        Virtio queue implementation
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/virtio-queue
Source0:        https://static.crates.io/crates/virtio-queue/virtio-queue-%{version}.crate
Source1:        https://raw.githubusercontent.com/rust-vmm/vm-virtio/main/LICENSE-APACHE
Source2:        https://raw.githubusercontent.com/rust-vmm/vm-virtio/main/LICENSE-BSD-3-Clause
Patch:          virtio-queue-fix-metadata.diff
ExcludeArch:    i686
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
Summary:        Virtio queue implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+test-utils-devel
Summary:        Virtio queue implementation
BuildArch:      noarch
%description -n %{name}+test-utils-devel

This package contains library source intended for building other packages which
use the "test-utils" feature of the "%{crate}" crate.

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

%cargo_test -f test-utils
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-virtio-queue-devel -f %{oreon_filedir}/rust-virtio-queue-devel.list

%changelog

%autochangelog
