%global source0_hash c92e44c63ba53bb55aa88ee48847664beae9446417621582fb14dfc69b2f8c72
%bcond check 0
%global debug_package %{nil}
%global crate gix-pathspec
Name:           rust-gix-pathspec
Version:        0.20.0
Release:        1%{?dist}
Summary:        Of the gitoxide project dealing magical pathspecs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-pathspec
Source0:        https://static.crates.io/crates/gix-pathspec/gix-pathspec-%{version}.crate
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
Summary:        Of the gitoxide project dealing magical pathspecs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Of the gitoxide project dealing magical pathspecs
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

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
%files -n rust-gix-pathspec-devel -f %{oreon_filedir}/rust-gix-pathspec-devel.list

%changelog

%autochangelog
