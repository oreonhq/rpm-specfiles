%global source0_hash 8e81635cecd0c60176468a4d6ea89352285f3c4804636da8486a1f6c60fc9f64
%bcond check 0
%global debug_package %{nil}
%global crate gh-emoji
Name:           rust-gh-emoji
Version:        1.0.9
Release:        1%{?dist}
Summary:        Convert :emoji: to Unicode using GitHub's emoji names
License:        MIT
URL:            https://crates.io/crates/gh-emoji
Source0:        https://static.crates.io/crates/gh-emoji/gh-emoji-%{version}.crate
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
Summary:        Convert :emoji: to Unicode using GitHub's emoji names
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
%files -n rust-gh-emoji-devel -f %{oreon_filedir}/rust-gh-emoji-devel.list

%changelog

%autochangelog
