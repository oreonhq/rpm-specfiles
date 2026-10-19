%global source0_hash 3f85ce2a7cd14ac0a30dc29a115de22466aeb8a029410f9f1e4f283443c959d1
%bcond check 1
%global debug_package %{nil}
%global crate avif-parse
Name:           rust-avif-parse
Version:        1.4.0
Release:        1%{?dist}
Summary:        Parser for AVIF image files
License:        MPL-2.0
URL:            https://crates.io/crates/avif-parse
Source0:        https://static.crates.io/crates/avif-parse/avif-parse-%{version}.crate
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
Summary:        Parser for AVIF image files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+mp4parse_fallible-devel
Summary:        Parser for AVIF image files
BuildArch:      noarch
%description -n %{name}+mp4parse_fallible-devel

This package contains library source intended for building other packages which
use the "mp4parse_fallible" feature of the "%{crate}" crate.

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
%files -n rust-avif-parse-devel -f %{oreon_filedir}/rust-avif-parse-devel.list

%changelog

%autochangelog
