%global source0_hash 961fa9711d7a1d9ccc13ac55b65482f828399dda12a0be7fa4e059dca410d217
%bcond check 0
%global debug_package %{nil}
%global crate sequoia-man
Name:           rust-sequoia-man
Version:        0.3.2
Release:        1%{?dist}
Summary:        Man page generation for Sequoia PGP CLIs
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-man
Source0:        https://static.crates.io/crates/sequoia-man/sequoia-man-%{version}.crate
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
Summary:        Man page generation for Sequoia PGP CLIs
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
%files -n rust-sequoia-man-devel -f %{oreon_filedir}/rust-sequoia-man-devel.list

%changelog

%autochangelog
