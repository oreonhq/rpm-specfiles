%global source0_hash d92bec98840b8f03a5ff5413de5293bfcd8bf96467cf5452609f939ec6f5de16
%bcond check 0
%global debug_package %{nil}
%global crate ascii
Name:           rust-ascii
Version:        1.1.0
Release:        1%{?dist}
Summary:        ASCII-only equivalents to `char`, `str` and `String`.
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ascii
Source0:        https://static.crates.io/crates/ascii/ascii-%{version}.crate
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
Summary:        ASCII-only equivalents to `char`, `str` and `String`.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        ASCII-only equivalents to `char`, `str` and `String`.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        ASCII-only equivalents to `char`, `str` and `String`.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_test-devel
Summary:        ASCII-only equivalents to `char`, `str` and `String`.
BuildArch:      noarch
%description -n %{name}+serde_test-devel

This package contains library source intended for building other packages which
use the "serde_test" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        ASCII-only equivalents to `char`, `str` and `String`.
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
%files -n rust-ascii-devel -f %{oreon_filedir}/rust-ascii-devel.list

%changelog

%autochangelog
