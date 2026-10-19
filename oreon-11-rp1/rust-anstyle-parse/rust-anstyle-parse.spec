%global source0_hash 52ce7f38b242319f7cabaa6813055467063ecdc9d355bbb4ce0c68908cd8130e
%bcond check 0
%global debug_package %{nil}
%global crate anstyle-parse
Name:           rust-anstyle-parse
Version:        1.0.0
Release:        1%{?dist}
Summary:        Parse ANSI Style Escapes
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/anstyle-parse
Source0:        https://static.crates.io/crates/anstyle-parse/anstyle-parse-%{version}.crate
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
Summary:        Parse ANSI Style Escapes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+core-devel
Summary:        Parse ANSI Style Escapes
BuildArch:      noarch
%description -n %{name}+core-devel

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%package     -n %{name}+utf8-devel
Summary:        Parse ANSI Style Escapes
BuildArch:      noarch
%description -n %{name}+utf8-devel

This package contains library source intended for building other packages which
use the "utf8" feature of the "%{crate}" crate.

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
%files -n rust-anstyle-parse-devel -f %{oreon_filedir}/rust-anstyle-parse-devel.list

%changelog

%autochangelog
