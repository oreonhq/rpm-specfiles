%global source0_hash 6af6ae20167a9ece4bcb41af5b80f8a1f1df981f6391189ce00fd257af04126a
%bcond check 0
%global debug_package %{nil}
%global crate typed-arena
Name:           rust-typed-arena
Version:        2.0.2
Release:        2%{?dist}
Summary:        Arena, a fast but limited type of allocator
License:        MIT
URL:            https://crates.io/crates/typed-arena
Source0:        https://static.crates.io/crates/typed-arena/typed-arena-%{version}.crate
Patch:          typed-arena-fix-metadata.diff
Patch:          0001-Fix-dangerous_implicit_autorefs-error-in-crate_autho.patch
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
Summary:        Arena, a fast but limited type of allocator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Arena, a fast but limited type of allocator
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
%files -n rust-typed-arena-devel -f %{oreon_filedir}/rust-typed-arena-devel.list

%changelog

%autochangelog
