%global source0_hash 6ecfad6c3abc80a577f2b91c1e412ee57e7a060d430b553c1b0c940974ebcd49
%bcond check 0
%global debug_package %{nil}
%global crate textwrap
Name:           rust-textwrap
Version:        0.16.4
Release:        1%{?dist}
Summary:        Library for word wrapping, indenting, and dedenting strings. Has opti...
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
Summary:        Library for word wrapping, indenting, and dedenting strings. Has opti...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+hyphenation-devel
Summary:        Library for word wrapping, indenting, and dedenting strings. Has opti...
BuildArch:      noarch
%description -n %{name}+hyphenation-devel

This package contains library source intended for building other packages which
use the "hyphenation" feature of the "%{crate}" crate.

%package     -n %{name}+smawk-devel
Summary:        Library for word wrapping, indenting, and dedenting strings. Has opti...
BuildArch:      noarch
%description -n %{name}+smawk-devel

This package contains library source intended for building other packages which
use the "smawk" feature of the "%{crate}" crate.

%package     -n %{name}+terminal_size-devel
Summary:        Library for word wrapping, indenting, and dedenting strings. Has opti...
BuildArch:      noarch
%description -n %{name}+terminal_size-devel

This package contains library source intended for building other packages which
use the "terminal_size" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-linebreak-devel
Summary:        Library for word wrapping, indenting, and dedenting strings. Has opti...
BuildArch:      noarch
%description -n %{name}+unicode-linebreak-devel

This package contains library source intended for building other packages which
use the "unicode-linebreak" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-width-devel
Summary:        Library for word wrapping, indenting, and dedenting strings. Has opti...
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
%files -n rust-textwrap-devel -f %{oreon_filedir}/rust-textwrap-devel.list

%changelog

%autochangelog
