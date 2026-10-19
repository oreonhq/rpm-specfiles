%global source0_hash 31b698c5f9a010f6573133b09e0de5408834d0c82f8d7475a89fc1867a71cd90
%bcond check 0
%global debug_package %{nil}
%global crate axum
Name:           rust-axum
Version:        0.8.9
Release:        1%{?dist}
Summary:        HTTP routing and request handling library
License:        MIT
URL:            https://crates.io/crates/axum
Source0:        https://static.crates.io/crates/axum/axum-%{version}.crate
Patch:          axum-fix-metadata.diff
Patch10:        0001-skip-doctest-with-unresolved-axum_extra-dependency.patch
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
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__private-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+__private-devel

This package contains library source intended for building other packages which
use the "__private" feature of the "%{crate}" crate.

%package     -n %{name}+form-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+form-devel

This package contains library source intended for building other packages which
use the "form" feature of the "%{crate}" crate.

%package     -n %{name}+http1-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+http1-devel

This package contains library source intended for building other packages which
use the "http1" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+matched-path-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+matched-path-devel

This package contains library source intended for building other packages which
use the "matched-path" feature of the "%{crate}" crate.

%package     -n %{name}+multipart-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+multipart-devel

This package contains library source intended for building other packages which
use the "multipart" feature of the "%{crate}" crate.

%package     -n %{name}+original-uri-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+original-uri-devel

This package contains library source intended for building other packages which
use the "original-uri" feature of the "%{crate}" crate.

%package     -n %{name}+query-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+query-devel

This package contains library source intended for building other packages which
use the "query" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tower-http-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+tower-http-devel

This package contains library source intended for building other packages which
use the "tower-http" feature of the "%{crate}" crate.

%package     -n %{name}+tower-log-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+tower-log-devel

This package contains library source intended for building other packages which
use the "tower-log" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+ws-devel
Summary:        HTTP routing and request handling library
BuildArch:      noarch
%description -n %{name}+ws-devel

This package contains library source intended for building other packages which
use the "ws" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-axum-devel -f %{oreon_filedir}/rust-axum-devel.list

%changelog

%autochangelog
