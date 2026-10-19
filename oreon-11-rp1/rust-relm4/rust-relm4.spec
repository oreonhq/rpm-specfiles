%global source0_hash 30837553c1a8cfea1a404c83ec387c5c8ff9358e1060b057c274c5daa5035ad1
%bcond check 1
%global debug_package %{nil}
%global crate relm4
Name:           rust-relm4
Version:        0.9.1
Release:        1%{?dist}
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/relm4
Source0:        https://static.crates.io/crates/relm4/relm4-%{version}.crate
Patch:          relm4-fix-metadata.diff
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
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+adw-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+adw-devel

This package contains library source intended for building other packages which
use the "adw" feature of the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%package     -n %{name}+css-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+css-devel

This package contains library source intended for building other packages which
use the "css" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_42-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+gnome_42-devel

This package contains library source intended for building other packages which
use the "gnome_42" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_43-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+gnome_43-devel

This package contains library source intended for building other packages which
use the "gnome_43" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_44-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+gnome_44-devel

This package contains library source intended for building other packages which
use the "gnome_44" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_45-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+gnome_45-devel

This package contains library source intended for building other packages which
use the "gnome_45" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_46-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+gnome_46-devel

This package contains library source intended for building other packages which
use the "gnome_46" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_47-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+gnome_47-devel

This package contains library source intended for building other packages which
use the "gnome_47" feature of the "%{crate}" crate.

%package     -n %{name}+libadwaita-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+libadwaita-devel

This package contains library source intended for building other packages which
use the "libadwaita" feature of the "%{crate}" crate.

%package     -n %{name}+libpanel-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+libpanel-devel

This package contains library source intended for building other packages which
use the "libpanel" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+panel-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+panel-devel

This package contains library source intended for building other packages which
use the "panel" feature of the "%{crate}" crate.

%package     -n %{name}+relm4-css-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+relm4-css-devel

This package contains library source intended for building other packages which
use the "relm4-css" feature of the "%{crate}" crate.

%package     -n %{name}+relm4-macros-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+relm4-macros-devel

This package contains library source intended for building other packages which
use the "relm4-macros" feature of the "%{crate}" crate.

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
%files -n rust-relm4-devel -f %{oreon_filedir}/rust-relm4-devel.list

%changelog

%autochangelog
