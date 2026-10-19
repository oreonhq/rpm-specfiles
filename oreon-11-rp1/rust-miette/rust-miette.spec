%global source0_hash 5f98efec8807c63c752b5bd61f862c165c115b0a35685bdcfd9238c7aeb592b7
%bcond check 0
%global debug_package %{nil}
%global crate miette
Name:           rust-miette
Version:        7.6.0
Release:        1%{?dist}
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
License:        Apache-2.0
URL:            https://crates.io/crates/miette
Source0:        https://static.crates.io/crates/miette/miette-%{version}.crate
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
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-ext-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+backtrace-ext-devel

This package contains library source intended for building other packages which
use the "backtrace-ext" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+fancy-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+fancy-devel

This package contains library source intended for building other packages which
use the "fancy" feature of the "%{crate}" crate.

%package     -n %{name}+fancy-base-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+fancy-base-devel

This package contains library source intended for building other packages which
use the "fancy-base" feature of the "%{crate}" crate.

%package     -n %{name}+fancy-no-backtrace-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+fancy-no-backtrace-devel

This package contains library source intended for building other packages which
use the "fancy-no-backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+fancy-no-syscall-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+fancy-no-syscall-devel

This package contains library source intended for building other packages which
use the "fancy-no-syscall" feature of the "%{crate}" crate.

%package     -n %{name}+miette-derive-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+miette-derive-devel

This package contains library source intended for building other packages which
use the "miette-derive" feature of the "%{crate}" crate.

%package     -n %{name}+no-format-args-capture-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+no-format-args-capture-devel

This package contains library source intended for building other packages which
use the "no-format-args-capture" feature of the "%{crate}" crate.

%package     -n %{name}+owo-colors-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+owo-colors-devel

This package contains library source intended for building other packages which
use the "owo-colors" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+supports-color-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+supports-color-devel

This package contains library source intended for building other packages which
use the "supports-color" feature of the "%{crate}" crate.

%package     -n %{name}+supports-hyperlinks-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+supports-hyperlinks-devel

This package contains library source intended for building other packages which
use the "supports-hyperlinks" feature of the "%{crate}" crate.

%package     -n %{name}+supports-unicode-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+supports-unicode-devel

This package contains library source intended for building other packages which
use the "supports-unicode" feature of the "%{crate}" crate.

%package     -n %{name}+syntect-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+syntect-devel

This package contains library source intended for building other packages which
use the "syntect" feature of the "%{crate}" crate.

%package     -n %{name}+syntect-highlighter-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+syntect-highlighter-devel

This package contains library source intended for building other packages which
use the "syntect-highlighter" feature of the "%{crate}" crate.

%package     -n %{name}+terminal_size-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+terminal_size-devel

This package contains library source intended for building other packages which
use the "terminal_size" feature of the "%{crate}" crate.

%package     -n %{name}+textwrap-devel
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals w...
BuildArch:      noarch
%description -n %{name}+textwrap-devel

This package contains library source intended for building other packages which
use the "textwrap" feature of the "%{crate}" crate.

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
%files -n rust-miette-devel -f %{oreon_filedir}/rust-miette-devel.list

%changelog

%autochangelog
