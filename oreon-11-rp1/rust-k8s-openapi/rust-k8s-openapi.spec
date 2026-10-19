%global source0_hash 19501afb943ae5806548bc3ebd7f3374153ca057a38f480ef30adfde5ef09755
%bcond check 0
%global debug_package %{nil}
%global crate k8s-openapi
Name:           rust-k8s-openapi
Version:        0.22.0
Release:        1%{?dist}
Summary:        Bindings for the Kubernetes client API
License:        Apache-2.0
URL:            https://crates.io/crates/k8s-openapi
Source0:        https://static.crates.io/crates/k8s-openapi/k8s-openapi-%{version}.crate
Patch:          0001-fix-invalid-code-block-syntax-in-documentation.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  fdupes
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
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+earliest-devel
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+earliest-devel

This package contains library source intended for building other packages which
use the "earliest" feature of the "%{crate}" crate.

%package     -n %{name}+latest-devel
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+latest-devel

This package contains library source intended for building other packages which
use the "latest" feature of the "%{crate}" crate.

%package     -n %{name}+schemars-devel
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+schemars-devel

This package contains library source intended for building other packages which
use the "schemars" feature of the "%{crate}" crate.

%package     -n %{name}+v1_24-devel
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+v1_24-devel

This package contains library source intended for building other packages which
use the "v1_24" feature of the "%{crate}" crate.

%package     -n %{name}+v1_25-devel
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+v1_25-devel

This package contains library source intended for building other packages which
use the "v1_25" feature of the "%{crate}" crate.

%package     -n %{name}+v1_26-devel
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+v1_26-devel

This package contains library source intended for building other packages which
use the "v1_26" feature of the "%{crate}" crate.

%package     -n %{name}+v1_27-devel
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+v1_27-devel

This package contains library source intended for building other packages which
use the "v1_27" feature of the "%{crate}" crate.

%package     -n %{name}+v1_28-devel
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+v1_28-devel

This package contains library source intended for building other packages which
use the "v1_28" feature of the "%{crate}" crate.

%package     -n %{name}+v1_29-devel
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+v1_29-devel

This package contains library source intended for building other packages which
use the "v1_29" feature of the "%{crate}" crate.

%package     -n %{name}+v1_30-devel
Summary:        Bindings for the Kubernetes client API
BuildArch:      noarch
%description -n %{name}+v1_30-devel

This package contains library source intended for building other packages which
use the "v1_30" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f latest
%install
%cargo_install -f latest
%fdupes %{buildroot}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f latest
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-k8s-openapi-devel -f %{oreon_filedir}/rust-k8s-openapi-devel.list

%changelog

%autochangelog
