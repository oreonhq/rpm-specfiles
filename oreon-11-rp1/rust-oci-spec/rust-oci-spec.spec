%global source0_hash 3f5a3fe998d50101ae009351fec56d88a69f4ed182e11000e711068c2f5abf72
%bcond check 0
%global debug_package %{nil}
%global crate oci-spec
%global supported_arches x86_64 aarch64 ppc64le s390x
Name:           rust-oci-spec
Version:        0.6.8
Release:        1%{?dist}
Summary:        Open Container Initiative Specifictions in Rust
License:        Apache-2.0
URL:            https://crates.io/crates/oci-spec
Source0:        https://static.crates.io/crates/oci-spec/oci-spec-%{version}.crate
Patch:          oci-spec-fix-metadata.diff
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
Summary:        Open Container Initiative Specifictions in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+distribution-devel
Summary:        Open Container Initiative Specifictions in Rust
BuildArch:      noarch
%description -n %{name}+distribution-devel

This package contains library source intended for building other packages which
use the "distribution" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        Open Container Initiative Specifictions in Rust
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+proptests-devel
Summary:        Open Container Initiative Specifictions in Rust
BuildArch:      noarch
%description -n %{name}+proptests-devel

This package contains library source intended for building other packages which
use the "proptests" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        Open Container Initiative Specifictions in Rust
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-devel
Summary:        Open Container Initiative Specifictions in Rust
BuildArch:      noarch
%description -n %{name}+runtime-devel

This package contains library source intended for building other packages which
use the "runtime" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifarch %{supported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifarch %{supported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-oci-spec-devel -f %{oreon_filedir}/rust-oci-spec-devel.list

%changelog

%autochangelog
