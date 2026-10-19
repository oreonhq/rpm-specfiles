%global source0_hash b6f5e870be6c3b371b77fe0ee0bafb859fa4964b4404c27de1d380043c4dda20
%bcond check 1
%global debug_package %{nil}
%global crate typenum
Name:           rust-typenum
Version:        1.20.1
Release:        1%{?dist}
Summary:        Typenum is a Rust library for type-level numbers evaluated at
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/typenum
Source0:        https://static.crates.io/crates/typenum/typenum-%{version}.crate
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
Summary:        Typenum is a Rust library for type-level numbers evaluated at
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+const-generics-devel
Summary:        Typenum is a Rust library for type-level numbers evaluated at
BuildArch:      noarch
%description -n %{name}+const-generics-devel

This package contains library source intended for building other packages which
use the "const-generics" feature of the "%{crate}" crate.

%package     -n %{name}+i128-devel
Summary:        Typenum is a Rust library for type-level numbers evaluated at
BuildArch:      noarch
%description -n %{name}+i128-devel

This package contains library source intended for building other packages which
use the "i128" feature of the "%{crate}" crate.

%package     -n %{name}+scale_info-devel
Summary:        Typenum is a Rust library for type-level numbers evaluated at
BuildArch:      noarch
%description -n %{name}+scale_info-devel

This package contains library source intended for building other packages which
use the "scale_info" feature of the "%{crate}" crate.

%package     -n %{name}+strict-devel
Summary:        Typenum is a Rust library for type-level numbers evaluated at
BuildArch:      noarch
%description -n %{name}+strict-devel

This package contains library source intended for building other packages which
use the "strict" feature of the "%{crate}" crate.

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
%files -n rust-typenum-devel -f %{oreon_filedir}/rust-typenum-devel.list

%changelog

%autochangelog
