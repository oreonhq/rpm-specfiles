%global source0_hash 45d3aca230fad2e6f6317ca0a72724338c4960cb97168a85cdee66df4a9a21a8
%bcond check 0
%global debug_package %{nil}
%global crate pest
Name:           rust-pest
Version:        2.9.2
Release:        1%{?dist}
Summary:        The Elegant Parser
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pest
Source0:        https://static.crates.io/crates/pest/pest-%{version}.crate
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
Summary:        The Elegant Parser
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+const_prec_climber-devel
Summary:        The Elegant Parser
BuildArch:      noarch
%description -n %{name}+const_prec_climber-devel

This package contains library source intended for building other packages which
use the "const_prec_climber" feature of the "%{crate}" crate.

%package     -n %{name}+miette-error-devel
Summary:        The Elegant Parser
BuildArch:      noarch
%description -n %{name}+miette-error-devel

This package contains library source intended for building other packages which
use the "miette-error" feature of the "%{crate}" crate.

%package     -n %{name}+pretty-print-devel
Summary:        The Elegant Parser
BuildArch:      noarch
%description -n %{name}+pretty-print-devel

This package contains library source intended for building other packages which
use the "pretty-print" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        The Elegant Parser
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+memchr-devel
Summary:        The Elegant Parser
BuildArch:      noarch
%description -n %{name}+memchr-devel

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

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
%files -n rust-pest-devel -f %{oreon_filedir}/rust-pest-devel.list

%changelog

%autochangelog
