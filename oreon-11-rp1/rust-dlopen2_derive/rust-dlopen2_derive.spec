%global source100_hash 39fa265207450e77c62e90c5594a06c085b655d8374c7ced4bf7894b6bd95dd2
%global source0_hash 1aacdd87ba97c2f83ff479e881e547f776b0a7c42921be22d4391f32b6284050
%bcond check 0
%global debug_package %{nil}
%global crate dlopen2_derive
Name:           rust-dlopen2_derive
Version:        0.5.0
Release:        1%{?dist}
Summary:        Derive macros for the dlopen2 crate
License:        MIT
URL:            https://crates.io/crates/dlopen2_derive
Source0:        https://static.crates.io/crates/dlopen2_derive/dlopen2_derive-%{version}.crate
Source100:      https://raw.githubusercontent.com/OpenByteDev/dlopen2/master/LICENSE
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
Summary:        Derive macros for the dlopen2 crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE100} .
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
%files -n rust-dlopen2_derive-devel -f %{oreon_filedir}/rust-dlopen2_derive-devel.list

%changelog

%autochangelog
