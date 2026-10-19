%global source0_hash 052ff849639942444955d93311f17caa86c9d77164a3dfc3b477b066246a5a79
%bcond check 0
%global debug_package %{nil}
%global crate parse-zoneinfo
Name:           rust-parse-zoneinfo
Version:        0.5.0
Release:        1%{?dist}
Summary:        Parse zoneinfo files from the IANA database
License:        MIT
URL:            https://crates.io/crates/parse-zoneinfo
Source0:        https://static.crates.io/crates/parse-zoneinfo/parse-zoneinfo-%{version}.crate
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
Summary:        Parse zoneinfo files from the IANA database
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
%files -n rust-parse-zoneinfo-devel -f %{oreon_filedir}/rust-parse-zoneinfo-devel.list

%changelog

%autochangelog
