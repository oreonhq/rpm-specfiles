%global source0_hash c43e7fd8284f025d0bd143c2855618ecdf697db55bde39211e5c9faec7669173
%bcond check 0
%global debug_package %{nil}
%global crate ansi-parser
Name:           rust-ansi-parser
Version:        0.9.1
Release:        1%{?dist}
Summary:        Library using nom for parsing ANSI Escape Codes
License:        MPL-2.0
URL:            https://crates.io/crates/ansi-parser
Source0:        https://static.crates.io/crates/ansi-parser/ansi-parser-%{version}.crate
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
Summary:        Library using nom for parsing ANSI Escape Codes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library using nom for parsing ANSI Escape Codes
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
%files -n rust-ansi-parser-devel -f %{oreon_filedir}/rust-ansi-parser-devel.list

%changelog

%autochangelog
