%global source0_hash a0610544180c38b88101fecf2dd634b174a62eef6946f84dfc6a7127512b381c
%bcond check 0
%global debug_package %{nil}
%global crate clap
Name:           rust-clap2
Version:        2.34.0
Release:        1%{?dist}
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
License:        MIT
URL:            https://crates.io/crates/clap
Source0:        https://static.crates.io/crates/clap/clap-%{version}.crate
Patch:          clap-fix-metadata-auto.diff
Patch:          0001-Replace-atty-with-std-io-IsTerminal.patch
Patch:          0001-Fix-dangerous_implicit_autorefs-error-in-crate_autho.patch
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
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+atty-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+atty-devel

This package contains library source intended for building other packages which
use the "atty" feature of the "%{crate}" crate.

%package     -n %{name}+clippy-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+clippy-devel

This package contains library source intended for building other packages which
use the "clippy" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+doc-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+doc-devel

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+no_cargo-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+no_cargo-devel

This package contains library source intended for building other packages which
use the "no_cargo" feature of the "%{crate}" crate.

%package     -n %{name}+strsim-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+strsim-devel

This package contains library source intended for building other packages which
use the "strsim" feature of the "%{crate}" crate.

%package     -n %{name}+suggestions-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+suggestions-devel

This package contains library source intended for building other packages which
use the "suggestions" feature of the "%{crate}" crate.

%package     -n %{name}+term_size-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+term_size-devel

This package contains library source intended for building other packages which
use the "term_size" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+vec_map-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+vec_map-devel

This package contains library source intended for building other packages which
use the "vec_map" feature of the "%{crate}" crate.

%package     -n %{name}+wrap_help-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+wrap_help-devel

This package contains library source intended for building other packages which
use the "wrap_help" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+yaml-devel

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-rust-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+yaml-rust-devel

This package contains library source intended for building other packages which
use the "yaml-rust" feature of the "%{crate}" crate.

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
%files -n rust-clap2-devel -f %{oreon_filedir}/rust-clap2-devel.list

%changelog

%autochangelog
