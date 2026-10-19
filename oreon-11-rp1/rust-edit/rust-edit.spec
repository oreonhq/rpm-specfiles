%global source0_hash f364860e764787163c8c8f58231003839be31276e821e2ad2092ddf496b1aa09
%bcond check 0
%global debug_package %{nil}
%global crate edit
Name:           rust-edit
Version:        0.1.5
Release:        1%{?dist}
Summary:        Open a file in the default text editor
License:        CC0-1.0
URL:            https://crates.io/crates/edit
Source0:        https://static.crates.io/crates/edit/edit-%{version}.crate
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
Summary:        Open a file in the default text editor
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+better-path-devel
Summary:        Open a file in the default text editor
BuildArch:      noarch
%description -n %{name}+better-path-devel

This package contains library source intended for building other packages which
use the "better-path" feature of the "%{crate}" crate.

%package     -n %{name}+quoted-env-devel
Summary:        Open a file in the default text editor
BuildArch:      noarch
%description -n %{name}+quoted-env-devel

This package contains library source intended for building other packages which
use the "quoted-env" feature of the "%{crate}" crate.

%package     -n %{name}+shell-words-devel
Summary:        Open a file in the default text editor
BuildArch:      noarch
%description -n %{name}+shell-words-devel

This package contains library source intended for building other packages which
use the "shell-words" feature of the "%{crate}" crate.

%package     -n %{name}+which-devel
Summary:        Open a file in the default text editor
BuildArch:      noarch
%description -n %{name}+which-devel

This package contains library source intended for building other packages which
use the "which" feature of the "%{crate}" crate.

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
%files -n rust-edit-devel -f %{oreon_filedir}/rust-edit-devel.list

%changelog

%autochangelog
