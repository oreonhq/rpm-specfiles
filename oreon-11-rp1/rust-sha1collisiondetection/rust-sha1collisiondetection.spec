%global source0_hash 1f606421e4a6012877e893c399822a4ed4b089164c5969424e1b9d1e66e6964b
%bcond check 0
%global debug_package %{nil}
%global crate sha1collisiondetection
Name:           rust-sha1collisiondetection
Version:        0.3.4
Release:        1%{?dist}
Summary:        SHA-1 hash function with collision detection and mitigation
License:        MIT
URL:            https://crates.io/crates/sha1collisiondetection
Source0:        https://static.crates.io/crates/sha1collisiondetection/sha1collisiondetection-%{version}.crate
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
Summary:        SHA-1 hash function with collision detection and mitigation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        SHA-1 hash function with collision detection and mitigation
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+clap_mangen-devel
Summary:        SHA-1 hash function with collision detection and mitigation
BuildArch:      noarch
%description -n %{name}+clap_mangen-devel

This package contains library source intended for building other packages which
use the "clap_mangen" feature of the "%{crate}" crate.

%package     -n %{name}+const-oid-devel
Summary:        SHA-1 hash function with collision detection and mitigation
BuildArch:      noarch
%description -n %{name}+const-oid-devel

This package contains library source intended for building other packages which
use the "const-oid" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        SHA-1 hash function with collision detection and mitigation
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+digest-trait-devel
Summary:        SHA-1 hash function with collision detection and mitigation
BuildArch:      noarch
%description -n %{name}+digest-trait-devel

This package contains library source intended for building other packages which
use the "digest-trait" feature of the "%{crate}" crate.

%package     -n %{name}+oid-devel
Summary:        SHA-1 hash function with collision detection and mitigation
BuildArch:      noarch
%description -n %{name}+oid-devel

This package contains library source intended for building other packages which
use the "oid" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        SHA-1 hash function with collision detection and mitigation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-sha1collisiondetection-devel -f %{oreon_filedir}/rust-sha1collisiondetection-devel.list

%changelog

%autochangelog
