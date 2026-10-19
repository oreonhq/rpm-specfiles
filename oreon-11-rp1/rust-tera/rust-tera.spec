%global source0_hash e8004bca281f2d32df3bacd59bc67b312cb4c70cea46cbd79dbe8ac5ed206722
%bcond check 0
%global debug_package %{nil}
%global crate tera
Name:           rust-tera
Version:        1.20.1
Release:        1%{?dist}
Summary:        Template engine based on Jinja2/Django templates
License:        MIT
URL:            https://crates.io/crates/tera
Source0:        https://static.crates.io/crates/tera/tera-%{version}.crate
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
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+builtins-devel
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+builtins-devel

This package contains library source intended for building other packages which
use the "builtins" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-tz-devel
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+chrono-tz-devel

This package contains library source intended for building other packages which
use the "chrono-tz" feature of the "%{crate}" crate.

%package     -n %{name}+date-locale-devel
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+date-locale-devel

This package contains library source intended for building other packages which
use the "date-locale" feature of the "%{crate}" crate.

%package     -n %{name}+humansize-devel
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+humansize-devel

This package contains library source intended for building other packages which
use the "humansize" feature of the "%{crate}" crate.

%package     -n %{name}+percent-encoding-devel
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+percent-encoding-devel

This package contains library source intended for building other packages which
use the "percent-encoding" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+preserve_order-devel

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+slug-devel
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+slug-devel

This package contains library source intended for building other packages which
use the "slug" feature of the "%{crate}" crate.

%package     -n %{name}+urlencode-devel
Summary:        Template engine based on Jinja2/Django templates
BuildArch:      noarch
%description -n %{name}+urlencode-devel

This package contains library source intended for building other packages which
use the "urlencode" feature of the "%{crate}" crate.

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
%files -n rust-tera-devel -f %{oreon_filedir}/rust-tera-devel.list

%changelog

%autochangelog
