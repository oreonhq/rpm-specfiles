%global source0_hash 0b946244a988c390a94667ae0e3958411fa40cc46ea496a929b263d883f5f9c3
%bcond check 0
%global debug_package %{nil}
%global crate concolor
Name:           rust-concolor
Version:        0.1.1
Release:        1%{?dist}
Summary:        Control console coloring across all dependencies
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/concolor
Source0:        https://static.crates.io/crates/concolor/concolor-%{version}.crate
Patch:          concolor-fix-metadata.diff
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
Summary:        Control console coloring across all dependencies
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+api-devel
Summary:        Control console coloring across all dependencies
BuildArch:      noarch
%description -n %{name}+api-devel

This package contains library source intended for building other packages which
use the "api" feature of the "%{crate}" crate.

%package     -n %{name}+auto-devel
Summary:        Control console coloring across all dependencies
BuildArch:      noarch
%description -n %{name}+auto-devel

This package contains library source intended for building other packages which
use the "auto" feature of the "%{crate}" crate.

%package     -n %{name}+clicolor-devel
Summary:        Control console coloring across all dependencies
BuildArch:      noarch
%description -n %{name}+clicolor-devel

This package contains library source intended for building other packages which
use the "clicolor" feature of the "%{crate}" crate.

%package     -n %{name}+core-devel
Summary:        Control console coloring across all dependencies
BuildArch:      noarch
%description -n %{name}+core-devel

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%package     -n %{name}+interactive-devel
Summary:        Control console coloring across all dependencies
BuildArch:      noarch
%description -n %{name}+interactive-devel

This package contains library source intended for building other packages which
use the "interactive" feature of the "%{crate}" crate.

%package     -n %{name}+no_color-devel
Summary:        Control console coloring across all dependencies
BuildArch:      noarch
%description -n %{name}+no_color-devel

This package contains library source intended for building other packages which
use the "no_color" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Control console coloring across all dependencies
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+term-devel
Summary:        Control console coloring across all dependencies
BuildArch:      noarch
%description -n %{name}+term-devel

This package contains library source intended for building other packages which
use the "term" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f api
%install
%cargo_install -f api
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f api
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-concolor-devel -f %{oreon_filedir}/rust-concolor-devel.list

%changelog

%autochangelog
