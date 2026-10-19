%global source0_hash a259e51c18c778763a8687c3026dfc7aca615e8f2747fb2689335c2d88290c81
%bcond check 1
%global debug_package %{nil}
%global crate delicious-adwaita
Name:           rust-delicious-adwaita
Version:        0.3.2
Release:        1%{?dist}
Summary:        Color scheme manager for gtk4 libadwaita applications
License:        LGPL-2.1-or-later
URL:            https://crates.io/crates/delicious-adwaita
Source0:        https://static.crates.io/crates/delicious-adwaita/delicious-adwaita-%{version}.crate
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
Summary:        Color scheme manager for gtk4 libadwaita applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all_themes-devel
Summary:        Color scheme manager for gtk4 libadwaita applications
BuildArch:      noarch
%description -n %{name}+all_themes-devel

This package contains library source intended for building other packages which
use the "all_themes" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Color scheme manager for gtk4 libadwaita applications
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+theme_catppuccin-devel
Summary:        Color scheme manager for gtk4 libadwaita applications
BuildArch:      noarch
%description -n %{name}+theme_catppuccin-devel

This package contains library source intended for building other packages which
use the "theme_catppuccin" feature of the "%{crate}" crate.

%package     -n %{name}+theme_everforest-devel
Summary:        Color scheme manager for gtk4 libadwaita applications
BuildArch:      noarch
%description -n %{name}+theme_everforest-devel

This package contains library source intended for building other packages which
use the "theme_everforest" feature of the "%{crate}" crate.

%package     -n %{name}+theme_solarized-devel
Summary:        Color scheme manager for gtk4 libadwaita applications
BuildArch:      noarch
%description -n %{name}+theme_solarized-devel

This package contains library source intended for building other packages which
use the "theme_solarized" feature of the "%{crate}" crate.

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
%files -n rust-delicious-adwaita-devel -f %{oreon_filedir}/rust-delicious-adwaita-devel.list

%changelog

%autochangelog
