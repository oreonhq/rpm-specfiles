%global source0_hash cfab44b4bc17601cf226cce31c87462a4a5bd5d325948c8ebbc9e715660a1287
%bcond check 0
%global debug_package %{nil}
%global crate termimad
Name:           rust-termimad
Version:        0.20.6
Release:        1%{?dist}
Summary:        Markdown Renderer for the Terminal
License:        MIT
URL:            https://crates.io/crates/termimad
Source0:        https://static.crates.io/crates/termimad/termimad-%{version}.crate
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
Summary:        Markdown Renderer for the Terminal
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+special-renders-devel
Summary:        Markdown Renderer for the Terminal
BuildArch:      noarch
%description -n %{name}+special-renders-devel

This package contains library source intended for building other packages which
use the "special-renders" feature of the "%{crate}" crate.

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
%files -n rust-termimad-devel -f %{oreon_filedir}/rust-termimad-devel.list

%changelog

%autochangelog
