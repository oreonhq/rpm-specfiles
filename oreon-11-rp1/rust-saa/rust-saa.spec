%global source0_hash bd85992a680de788217d9c70b74aa7685b108cf1aba02f728fb27f1b27199ad1
%bcond check 1
%global debug_package %{nil}
%global crate saa
Name:           rust-saa
Version:        5.6.2
Release:        1%{?dist}
Summary:        Word-sized low-level synchronization primitives providing both asynchronous and synchronous interfaces
License:        Apache-2.0
URL:            https://crates.io/crates/saa
Source0:        https://static.crates.io/crates/saa/saa-%{version}.crate
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
Summary:        Word-sized low-level synchronization primitives providing both asynchronous and synchronous interfaces
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+lock_api-devel
Summary:        Word-sized low-level synchronization primitives providing both asynchronous and synchronous interfaces
BuildArch:      noarch
%description -n %{name}+lock_api-devel

This package contains library source intended for building other packages which
use the "lock_api" feature of the "%{crate}" crate.

%package     -n %{name}+loom-devel
Summary:        Word-sized low-level synchronization primitives providing both asynchronous and synchronous interfaces
BuildArch:      noarch
%description -n %{name}+loom-devel

This package contains library source intended for building other packages which
use the "loom" feature of the "%{crate}" crate.

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
%files -n rust-saa-devel -f %{oreon_filedir}/rust-saa-devel.list

%changelog

%autochangelog
