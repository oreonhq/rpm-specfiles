%global source0_hash 15242978b4e65431be4ccd5cf539d3c142518e114b7ecfa72ffd02cd6432e6e3
%bcond check 1
%global debug_package %{nil}
%global crate relm4-icons
Name:           rust-relm4-icons
Version:        0.9.0
Release:        1%{?dist}
Summary:        Icons for gtk-rs and Relm4 applications
License:        (Apache-2.0 OR MIT) AND CC0-1.0 AND MIT
URL:            https://crates.io/crates/relm4-icons
Source0:        https://static.crates.io/crates/relm4-icons/relm4-icons-%{version}.crate
Source100:      LICENSE-CC0-1.0
Patch:          relm4-icons-fix-metadata.diff
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
Summary:        Icons for gtk-rs and Relm4 applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        Icons for gtk-rs and Relm4 applications
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%package     -n %{name}+fluent-system-icons-devel
Summary:        Icons for gtk-rs and Relm4 applications
BuildArch:      noarch
%description -n %{name}+fluent-system-icons-devel

This package contains library source intended for building other packages which
use the "fluent-system-icons" feature of the "%{crate}" crate.

%package     -n %{name}+icon-development-kit-devel
Summary:        Icons for gtk-rs and Relm4 applications
BuildArch:      noarch
%description -n %{name}+icon-development-kit-devel

This package contains library source intended for building other packages which
use the "icon-development-kit" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE100} .
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
%files -n rust-relm4-icons-devel -f %{oreon_filedir}/rust-relm4-icons-devel.list

%changelog

%autochangelog
