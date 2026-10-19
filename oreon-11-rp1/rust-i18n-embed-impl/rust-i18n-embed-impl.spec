%global source0_hash 0f2cc0e0523d1fe6fc2c6f66e5038624ea8091b3e7748b5e8e0c84b1698db6c2
%bcond check 1
%global debug_package %{nil}
%global crate i18n-embed-impl
Name:           rust-i18n-embed-impl
Version:        0.8.4
Release:        1%{?dist}
Summary:        Macro implementations for i18n-embed
License:        MIT
URL:            https://crates.io/crates/i18n-embed-impl
Source0:        https://static.crates.io/crates/i18n-embed-impl/i18n-embed-impl-%{version}.crate
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
Summary:        Macro implementations for i18n-embed
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+find-crate-devel
Summary:        Macro implementations for i18n-embed
BuildArch:      noarch
%description -n %{name}+find-crate-devel

This package contains library source intended for building other packages which
use the "find-crate" feature of the "%{crate}" crate.

%package     -n %{name}+fluent-system-devel
Summary:        Macro implementations for i18n-embed
BuildArch:      noarch
%description -n %{name}+fluent-system-devel

This package contains library source intended for building other packages which
use the "fluent-system" feature of the "%{crate}" crate.

%package     -n %{name}+gettext-system-devel
Summary:        Macro implementations for i18n-embed
BuildArch:      noarch
%description -n %{name}+gettext-system-devel

This package contains library source intended for building other packages which
use the "gettext-system" feature of the "%{crate}" crate.

%package     -n %{name}+i18n-config-devel
Summary:        Macro implementations for i18n-embed
BuildArch:      noarch
%description -n %{name}+i18n-config-devel

This package contains library source intended for building other packages which
use the "i18n-config" feature of the "%{crate}" crate.

%package     -n %{name}+quote-devel
Summary:        Macro implementations for i18n-embed
BuildArch:      noarch
%description -n %{name}+quote-devel

This package contains library source intended for building other packages which
use the "quote" feature of the "%{crate}" crate.

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
%files -n rust-i18n-embed-impl-devel -f %{oreon_filedir}/rust-i18n-embed-impl-devel.list

%changelog

%autochangelog
