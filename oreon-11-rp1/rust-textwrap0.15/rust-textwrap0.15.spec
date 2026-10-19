%global source0_hash b7b3e525a49ec206798b40326a44121291b530c963cfb01018f63e135bac543d
%bcond check 1
%global debug_package %{nil}
%global crate textwrap
Name:           rust-textwrap0.15
Version:        0.15.2
Release:        1%{?dist}
Summary:        Powerful library for word wrapping, indenting, and dedenting strings
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
Summary:        Powerful library for word wrapping, indenting, and dedenting strings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+smawk-devel
Summary:        Powerful library for word wrapping, indenting, and dedenting strings
BuildArch:      noarch
%description -n %{name}+smawk-devel

This package contains library source intended for building other packages which
use the "smawk" feature of the "%{crate}" crate.

%package     -n %{name}+terminal_size-devel
Summary:        Powerful library for word wrapping, indenting, and dedenting strings
BuildArch:      noarch
%description -n %{name}+terminal_size-devel

This package contains library source intended for building other packages which
use the "terminal_size" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-linebreak-devel
Summary:        Powerful library for word wrapping, indenting, and dedenting strings
BuildArch:      noarch
%description -n %{name}+unicode-linebreak-devel

This package contains library source intended for building other packages which
use the "unicode-linebreak" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-width-devel
Summary:        Powerful library for word wrapping, indenting, and dedenting strings
BuildArch:      noarch
%description -n %{name}+unicode-width-devel

This package contains library source intended for building other packages which
use the "unicode-width" feature of the "%{crate}" crate.

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
%files -n rust-textwrap0.15-devel -f %{oreon_filedir}/rust-textwrap0.15-devel.list

%changelog

%autochangelog
