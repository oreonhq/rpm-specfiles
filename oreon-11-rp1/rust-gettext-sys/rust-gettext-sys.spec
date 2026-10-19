%global source0_hash 4caa7e4460b196107cc1bb2629488e8b6dbb7f34f6683ea6753c4ac22f590785
%bcond check 1
%global debug_package %{nil}
%global crate gettext-sys
Name:           rust-gettext-sys
Version:        0.27.0
Release:        1%{?dist}
Summary:        Raw FFI bindings for gettext
License:        MIT
URL:            https://crates.io/crates/gettext-sys
Source0:        https://static.crates.io/crates/gettext-sys/gettext-sys-%{version}.crate
Patch:          gettext-sys-fix-metadata.diff
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
Summary:        Raw FFI bindings for gettext
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gettext-system-devel
Summary:        Raw FFI bindings for gettext
BuildArch:      noarch
%description -n %{name}+gettext-system-devel

This package contains library source intended for building other packages which
use the "gettext-system" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -v *.tar.xz
rm -v build.rs
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
%files -n rust-gettext-sys-devel -f %{oreon_filedir}/rust-gettext-sys-devel.list

%changelog

%autochangelog
