%global source0_hash 9c9e4945611996e885dc4eeae23f3d6f20cfb6e8f4bad4985c2222bbcf9a9745
%bcond check 0
%global debug_package %{nil}
%global crate uuhelp_parser
Name:           rust-uuhelp_parser
Version:        0.2.2
Release:        1%{?dist}
Summary:        Collection of functions to parse the markdown code of help files
License:        MIT
URL:            https://crates.io/crates/uuhelp_parser
Source0:        https://static.crates.io/crates/uuhelp_parser/uuhelp_parser-%{version}.crate
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
Summary:        Collection of functions to parse the markdown code of help files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-uuhelp_parser-devel -f %{oreon_filedir}/rust-uuhelp_parser-devel.list

%changelog

%autochangelog
