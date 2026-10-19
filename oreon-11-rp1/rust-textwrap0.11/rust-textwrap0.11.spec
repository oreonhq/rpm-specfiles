%global source0_hash d326610f408c7a4eb6f51c37c330e496b08506c9457c9d34287ecc38809fb060
%bcond check 0
%global debug_package %{nil}
%global crate textwrap
Name:           rust-textwrap0.11
Version:        0.11.0
Release:        1%{?dist}
Summary:        Textwrap is a small library for word wrapping, indenting, and
License:        MIT
URL:            https://crates.io/crates/textwrap
Source0:        https://static.crates.io/crates/textwrap/textwrap-%{version}.crate
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
Summary:        Textwrap is a small library for word wrapping, indenting, and
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+hyphenation-devel
Summary:        Textwrap is a small library for word wrapping, indenting, and
BuildArch:      noarch
%description -n %{name}+hyphenation-devel

This package contains library source intended for building other packages which
use the "hyphenation" feature of the "%{crate}" crate.

%package     -n %{name}+term_size-devel
Summary:        Textwrap is a small library for word wrapping, indenting, and
BuildArch:      noarch
%description -n %{name}+term_size-devel

This package contains library source intended for building other packages which
use the "term_size" feature of the "%{crate}" crate.

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
%files -n rust-textwrap0.11-devel -f %{oreon_filedir}/rust-textwrap0.11-devel.list

%changelog

%autochangelog
