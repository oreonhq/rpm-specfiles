%global source0_hash c906aed1a3a713b7d06f9dfb44920f5e59cd4cd4b45c1d965a65da801cdf30bd
%bcond check 0
%global debug_package %{nil}
%global crate regorus
Name:           rust-regorus
Version:        0.2.6
Release:        1%{?dist}
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
License:        MIT AND Apache-2.0 AND BSD-3-Clause
URL:            https://crates.io/crates/regorus
Source0:        https://static.crates.io/crates/regorus/regorus-%{version}.crate
Patch:          regorus-fix-metadata.diff
Patch10:        regorus-0.2.6-missing-license-texts.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  git-core
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
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arc-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+arc-devel

This package contains library source intended for building other packages which
use the "arc" feature of the "%{crate}" crate.

%package     -n %{name}+ast-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+ast-devel

This package contains library source intended for building other packages which
use the "ast" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+base64url-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+base64url-devel

This package contains library source intended for building other packages which
use the "base64url" feature of the "%{crate}" crate.

%package     -n %{name}+coverage-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+coverage-devel

This package contains library source intended for building other packages which
use the "coverage" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+crypto-devel

This package contains library source intended for building other packages which
use the "crypto" feature of the "%{crate}" crate.

%package     -n %{name}+deprecated-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+deprecated-devel

This package contains library source intended for building other packages which
use the "deprecated" feature of the "%{crate}" crate.

%package     -n %{name}+full-opa-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+full-opa-devel

This package contains library source intended for building other packages which
use the "full-opa" feature of the "%{crate}" crate.

%package     -n %{name}+glob-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+glob-devel

This package contains library source intended for building other packages which
use the "glob" feature of the "%{crate}" crate.

%package     -n %{name}+graph-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+graph-devel

This package contains library source intended for building other packages which
use the "graph" feature of the "%{crate}" crate.

%package     -n %{name}+hex-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+hex-devel

This package contains library source intended for building other packages which
use the "hex" feature of the "%{crate}" crate.

%package     -n %{name}+http-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+http-devel

This package contains library source intended for building other packages which
use the "http" feature of the "%{crate}" crate.

%package     -n %{name}+jwt-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+jwt-devel

This package contains library source intended for building other packages which
use the "jwt" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

%package     -n %{name}+opa-no-std-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+opa-no-std-devel

This package contains library source intended for building other packages which
use the "opa-no-std" feature of the "%{crate}" crate.

%package     -n %{name}+opa-runtime-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+opa-runtime-devel

This package contains library source intended for building other packages which
use the "opa-runtime" feature of the "%{crate}" crate.

%package     -n %{name}+opa-testutil-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+opa-testutil-devel

This package contains library source intended for building other packages which
use the "opa-testutil" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+rego-extensions-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+rego-extensions-devel

This package contains library source intended for building other packages which
use the "rego-extensions" feature of the "%{crate}" crate.

%package     -n %{name}+semver-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+semver-devel

This package contains library source intended for building other packages which
use the "semver" feature of the "%{crate}" crate.

%package     -n %{name}+serde_yaml-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+serde_yaml-devel

This package contains library source intended for building other packages which
use the "serde_yaml" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+urlquery-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+urlquery-devel

This package contains library source intended for building other packages which
use the "urlquery" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-devel
Summary:        Fast, lightweight Rego (OPA policy language) interpreter
BuildArch:      noarch
%description -n %{name}+yaml-devel

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

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
%files -n rust-regorus-devel -f %{oreon_filedir}/rust-regorus-devel.list

%changelog

%autochangelog
