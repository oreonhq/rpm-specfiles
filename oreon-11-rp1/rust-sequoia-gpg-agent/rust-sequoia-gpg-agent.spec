%global source0_hash 5c36b37720b61230507a953d9879eb0dd8c228d86948d37cba53ced942e862a1
%bcond check 0
%global debug_package %{nil}
%global crate sequoia-gpg-agent
Name:           rust-sequoia-gpg-agent
Version:        0.6.2
Release:        1%{?dist}
Summary:        A library for interacting with GnuPG's gpg-agent
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-gpg-agent
Source0:        https://static.crates.io/crates/sequoia-gpg-agent/sequoia-gpg-agent-%{version}.crate
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
Summary:        A library for interacting with GnuPG's gpg-agent
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
%files -n rust-sequoia-gpg-agent-devel -f %{oreon_filedir}/rust-sequoia-gpg-agent-devel.list

%changelog

%autochangelog
