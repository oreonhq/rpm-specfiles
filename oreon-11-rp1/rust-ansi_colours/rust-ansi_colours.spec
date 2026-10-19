%global source0_hash 14eec43e0298190790f41679fe69ef7a829d2a2ddd78c8c00339e84710e435fe
%bcond check 0
%global debug_package %{nil}
%global crate ansi_colours
Name:           rust-ansi_colours
Version:        1.2.3
Release:        1%{?dist}
Summary:        true-colour ↔ ANSI terminal palette converter
License:        LGPL-3.0-or-later
URL:            https://crates.io/crates/ansi_colours
Source0:        https://static.crates.io/crates/ansi_colours/ansi_colours-%{version}.crate
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
Summary:        true-colour ↔ ANSI terminal palette converter
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansi_term-devel
Summary:        true-colour ↔ ANSI terminal palette converter
BuildArch:      noarch
%description -n %{name}+ansi_term-devel

This package contains library source intended for building other packages which
use the "ansi_term" feature of the "%{crate}" crate.

%package     -n %{name}+anstyle-devel
Summary:        true-colour ↔ ANSI terminal palette converter
BuildArch:      noarch
%description -n %{name}+anstyle-devel

This package contains library source intended for building other packages which
use the "anstyle" feature of the "%{crate}" crate.

%package     -n %{name}+rgb-devel
Summary:        true-colour ↔ ANSI terminal palette converter
BuildArch:      noarch
%description -n %{name}+rgb-devel

This package contains library source intended for building other packages which
use the "rgb" feature of the "%{crate}" crate.

%package     -n %{name}+termcolor-devel
Summary:        true-colour ↔ ANSI terminal palette converter
BuildArch:      noarch
%description -n %{name}+termcolor-devel

This package contains library source intended for building other packages which
use the "termcolor" feature of the "%{crate}" crate.

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
%files -n rust-ansi_colours-devel -f %{oreon_filedir}/rust-ansi_colours-devel.list

%changelog

%autochangelog
