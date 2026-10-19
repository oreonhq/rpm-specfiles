%global source0_hash 25f104b501bf2364e78d0d3974cbc774f738f5865306ed128e1e0d7499c0ad96
%bcond check 1
%global debug_package %{nil}
%global crate dialoguer
Name:           rust-dialoguer
Version:        0.12.0
Release:        1%{?dist}
Summary:        Command line prompting library
License:        MIT
URL:            https://crates.io/crates/dialoguer
Source0:        https://static.crates.io/crates/dialoguer/dialoguer-%{version}.crate
Patch:          dialoguer-fix-metadata.diff
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
Summary:        Command line prompting library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+completion-devel
Summary:        Command line prompting library
BuildArch:      noarch
%description -n %{name}+completion-devel

This package contains library source intended for building other packages which
use the "completion" feature of the "%{crate}" crate.

%package     -n %{name}+editor-devel
Summary:        Command line prompting library
BuildArch:      noarch
%description -n %{name}+editor-devel

This package contains library source intended for building other packages which
use the "editor" feature of the "%{crate}" crate.

%package     -n %{name}+fuzzy-matcher-devel
Summary:        Command line prompting library
BuildArch:      noarch
%description -n %{name}+fuzzy-matcher-devel

This package contains library source intended for building other packages which
use the "fuzzy-matcher" feature of the "%{crate}" crate.

%package     -n %{name}+fuzzy-select-devel
Summary:        Command line prompting library
BuildArch:      noarch
%description -n %{name}+fuzzy-select-devel

This package contains library source intended for building other packages which
use the "fuzzy-select" feature of the "%{crate}" crate.

%package     -n %{name}+history-devel
Summary:        Command line prompting library
BuildArch:      noarch
%description -n %{name}+history-devel

This package contains library source intended for building other packages which
use the "history" feature of the "%{crate}" crate.

%package     -n %{name}+password-devel
Summary:        Command line prompting library
BuildArch:      noarch
%description -n %{name}+password-devel

This package contains library source intended for building other packages which
use the "password" feature of the "%{crate}" crate.

%package     -n %{name}+tempfile-devel
Summary:        Command line prompting library
BuildArch:      noarch
%description -n %{name}+tempfile-devel

This package contains library source intended for building other packages which
use the "tempfile" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Command line prompting library
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-dialoguer-devel -f %{oreon_filedir}/rust-dialoguer-devel.list

%changelog

%autochangelog
