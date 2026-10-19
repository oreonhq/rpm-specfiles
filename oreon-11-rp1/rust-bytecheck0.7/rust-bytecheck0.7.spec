%global source0_hash 41502630fe304ce54cbb2f8389e017784dee2b0328147779fcbe43b9db06d35d
%bcond check 0
%global debug_package %{nil}
%global crate bytecheck
Name:           rust-bytecheck0.7
Version:        0.7.0
Release:        1%{?dist}
Summary:        Derive macro for bytecheck
License:        MIT
URL:            https://crates.io/crates/bytecheck
Source0:        https://static.crates.io/crates/bytecheck/bytecheck-%{version}.crate
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
Summary:        Derive macro for bytecheck
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+simdutf8-devel
Summary:        Derive macro for bytecheck
BuildArch:      noarch
%description -n %{name}+simdutf8-devel

This package contains library source intended for building other packages which
use the "simdutf8" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Derive macro for bytecheck
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Derive macro for bytecheck
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+verbose-devel
Summary:        Derive macro for bytecheck
BuildArch:      noarch
%description -n %{name}+verbose-devel

This package contains library source intended for building other packages which
use the "verbose" feature of the "%{crate}" crate.

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
%files -n rust-bytecheck0.7-devel -f %{oreon_filedir}/rust-bytecheck0.7-devel.list

%changelog

%autochangelog
