%global source0_hash 7d8fc09f81816d9530a29fc1a879c7b4a6b94c3a50bb9d5626a58ae15ca34360
%bcond check 0
%global debug_package %{nil}
%global crate plex
Name:           rust-plex
Version:        0.3.1
Release:        1%{?dist}
Summary:        Syntax extension for writing lexers and parsers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/plex
Source0:        https://static.crates.io/crates/plex/plex-%{version}.crate
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
Summary:        Syntax extension for writing lexers and parsers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+lalr-devel
Summary:        Syntax extension for writing lexers and parsers
BuildArch:      noarch
%description -n %{name}+lalr-devel

This package contains library source intended for building other packages which
use the "lalr" feature of the "%{crate}" crate.

%package     -n %{name}+lexer-devel
Summary:        Syntax extension for writing lexers and parsers
BuildArch:      noarch
%description -n %{name}+lexer-devel

This package contains library source intended for building other packages which
use the "lexer" feature of the "%{crate}" crate.

%package     -n %{name}+parser-devel
Summary:        Syntax extension for writing lexers and parsers
BuildArch:      noarch
%description -n %{name}+parser-devel

This package contains library source intended for building other packages which
use the "parser" feature of the "%{crate}" crate.

%package     -n %{name}+redfa-devel
Summary:        Syntax extension for writing lexers and parsers
BuildArch:      noarch
%description -n %{name}+redfa-devel

This package contains library source intended for building other packages which
use the "redfa" feature of the "%{crate}" crate.

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
%files -n rust-plex-devel -f %{oreon_filedir}/rust-plex-devel.list

%changelog

%autochangelog
