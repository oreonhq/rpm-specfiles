%global source0_hash 9af6bbdb3f3c62b4920407c479af1cc0beb27fd75a762782d48baed53d330958
%bcond check 1
%global debug_package %{nil}
%global crate gix-note
Name:           rust-gix-note
Version:        0.1.1
Release:        1%{?dist}
Summary:        Of the gitoxide project dealing with git notes
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-note
Source0:        https://static.crates.io/crates/gix-note/gix-note-%{version}.crate
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
Summary:        Of the gitoxide project dealing with git notes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Of the gitoxide project dealing with git notes
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha256-devel
Summary:        Of the gitoxide project dealing with git notes
BuildArch:      noarch
%description -n %{name}+sha256-devel

This package contains library source intended for building other packages which
use the "sha256" feature of the "%{crate}" crate.

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
%files -n rust-gix-note-devel -f %{oreon_filedir}/rust-gix-note-devel.list

%changelog

%autochangelog
