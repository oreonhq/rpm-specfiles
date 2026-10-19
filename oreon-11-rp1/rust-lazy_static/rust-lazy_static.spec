%global source0_hash bbd2bcb4c963f2ddae06a2efc7e9f3591312473c50c6685e1f298068316e66fe
%bcond_without check
%global debug_package %{nil}
%global crate lazy_static
Name:           rust-lazy_static
Version:        1.5.0
Release:        1%{?dist}
Summary:        Macro for declaring lazily evaluated statics in Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lazy_static
Source0:        https://static.crates.io/crates/lazy_static/lazy_static-%{version}.crate
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
Summary:        Macro for declaring lazily evaluated statics in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+spin-devel
Summary:        Macro for declaring lazily evaluated statics in Rust
BuildArch:      noarch
%description -n %{name}+spin-devel

This package contains library source intended for building other packages which
use the "spin" feature of the "%{crate}" crate.

%package     -n %{name}+spin_no_std-devel
Summary:        Macro for declaring lazily evaluated statics in Rust
BuildArch:      noarch
%description -n %{name}+spin_no_std-devel

This package contains library source intended for building other packages which
use the "spin_no_std" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip ui
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-lazy_static-devel -f %{oreon_filedir}/rust-lazy_static-devel.list

%changelog

%autochangelog
