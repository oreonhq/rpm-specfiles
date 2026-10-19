%global source0_hash 060de1453b69f46304b28274f382132f4e72c55637cf362920926a70d090890d
%bcond check 0
%global debug_package %{nil}
%global crate ansi-str
Name:           rust-ansi-str
Version:        0.9.0
Release:        1%{?dist}
Summary:        Library which provides a set of methods to work with ANSI strings
License:        MIT
URL:            https://crates.io/crates/ansi-str
Source0:        https://static.crates.io/crates/ansi-str/ansi-str-%{version}.crate
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
Summary:        Library which provides a set of methods to work with ANSI strings
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
%files -n rust-ansi-str-devel -f %{oreon_filedir}/rust-ansi-str-devel.list

%changelog

%autochangelog
