%global source0_hash 964de6e86d545b246d84badc0fef527924ace5134f30641c203ef52ba83f58d5
%bcond check 0
%global debug_package %{nil}
%global crate indenter
Name:           rust-indenter
Version:        0.3.4
Release:        1%{?dist}
Summary:        A formatter wrapper that indents the text, designed for error display...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/indenter
Source0:        https://static.crates.io/crates/indenter/indenter-%{version}.crate
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
Summary:        A formatter wrapper that indents the text, designed for error display...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A formatter wrapper that indents the text, designed for error display...
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
%files -n rust-indenter-devel -f %{oreon_filedir}/rust-indenter-devel.list

%changelog

%autochangelog
