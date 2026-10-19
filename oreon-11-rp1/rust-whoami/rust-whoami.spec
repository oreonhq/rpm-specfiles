%global source0_hash 998767ef88740d1f5b0682a9c53c24431453923962269c2db68ee43788c5a40d
%bcond check 0
%global debug_package %{nil}
%global crate whoami
Name:           rust-whoami
Version:        2.1.2
Release:        1%{?dist}
Summary:        Rust library for getting information about the current user and envir...
License:        Apache-2.0 OR BSL-1.0 OR MIT
URL:            https://crates.io/crates/whoami
Source0:        https://static.crates.io/crates/whoami/whoami-%{version}.crate
Patch:          whoami-fix-metadata.diff
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
Summary:        Rust library for getting information about the current user and envir...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+force-stub-devel
Summary:        Rust library for getting information about the current user and envir...
BuildArch:      noarch
%description -n %{name}+force-stub-devel

This package contains library source intended for building other packages which
use the "force-stub" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rust library for getting information about the current user and envir...
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
%files -n rust-whoami-devel -f %{oreon_filedir}/rust-whoami-devel.list

%changelog

%autochangelog
