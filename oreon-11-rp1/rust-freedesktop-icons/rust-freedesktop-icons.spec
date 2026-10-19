%global source0_hash 95f87364ea709292a3b3f74014ce3ee78412c89807eea75a358c8e029b000994
%bcond check 1
%global debug_package %{nil}
%global crate freedesktop-icons
Name:           rust-freedesktop-icons
Version:        0.4.0
Release:        1%{?dist}
Summary:        Freedesktop Icons lookup crate
License:        MIT
URL:            https://crates.io/crates/freedesktop-icons
Source0:        https://static.crates.io/crates/freedesktop-icons/freedesktop-icons-%{version}.crate
Patch:          freedesktop-icons-fix-metadata.diff
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
Summary:        Freedesktop Icons lookup crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+local_tests-devel
Summary:        Freedesktop Icons lookup crate
BuildArch:      noarch
%description -n %{name}+local_tests-devel

This package contains library source intended for building other packages which
use the "local_tests" feature of the "%{crate}" crate.

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

%{cargo_test -- -- --exact %{shrink:
    --skip theme::parse::test::should_get_theme_parents
    --skip theme::test::should_get_png_first
    --skip theme::test::should_get_svg_first
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-freedesktop-icons-devel -f %{oreon_filedir}/rust-freedesktop-icons-devel.list

%changelog

%autochangelog
