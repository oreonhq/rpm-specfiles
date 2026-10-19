%global source0_hash 3b829e4e32b91e643de6eafe82b1d90675f5874230191a4ffbc1b336dec4d6bf
%bcond check 0
%global debug_package %{nil}
%global crate axum
Name:           rust-axum0.6
Version:        0.6.20
Release:        1%{?dist}
Summary:        Web framework that focuses on ergonomics and modularity
License:        MIT
URL:            https://crates.io/crates/axum
Source0:        https://static.crates.io/crates/axum/axum-%{version}.crate
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
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__private_docs-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+__private_docs-devel

This package contains library source intended for building other packages which
use the "__private_docs" feature of the "%{crate}" crate.

%package     -n %{name}+axum-macros-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+axum-macros-devel

This package contains library source intended for building other packages which
use the "axum-macros" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+form-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+form-devel

This package contains library source intended for building other packages which
use the "form" feature of the "%{crate}" crate.

%package     -n %{name}+headers-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+headers-devel

This package contains library source intended for building other packages which
use the "headers" feature of the "%{crate}" crate.

%package     -n %{name}+http1-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+http1-devel

This package contains library source intended for building other packages which
use the "http1" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+matched-path-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+matched-path-devel

This package contains library source intended for building other packages which
use the "matched-path" feature of the "%{crate}" crate.

%package     -n %{name}+multer-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+multer-devel

This package contains library source intended for building other packages which
use the "multer" feature of the "%{crate}" crate.

%package     -n %{name}+multipart-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+multipart-devel

This package contains library source intended for building other packages which
use the "multipart" feature of the "%{crate}" crate.

%package     -n %{name}+original-uri-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+original-uri-devel

This package contains library source intended for building other packages which
use the "original-uri" feature of the "%{crate}" crate.

%package     -n %{name}+query-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+query-devel

This package contains library source intended for building other packages which
use the "query" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+serde_path_to_error-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+serde_path_to_error-devel

This package contains library source intended for building other packages which
use the "serde_path_to_error" feature of the "%{crate}" crate.

%package     -n %{name}+serde_urlencoded-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+serde_urlencoded-devel

This package contains library source intended for building other packages which
use the "serde_urlencoded" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-tungstenite-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+tokio-tungstenite-devel

This package contains library source intended for building other packages which
use the "tokio-tungstenite" feature of the "%{crate}" crate.

%package     -n %{name}+tower-http-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+tower-http-devel

This package contains library source intended for building other packages which
use the "tower-http" feature of the "%{crate}" crate.

%package     -n %{name}+tower-log-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+tower-log-devel

This package contains library source intended for building other packages which
use the "tower-log" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+ws-devel
Summary:        Web framework that focuses on ergonomics and modularity
BuildArch:      noarch
%description -n %{name}+ws-devel

This package contains library source intended for building other packages which
use the "ws" feature of the "%{crate}" crate.

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
%files -n rust-axum0.6-devel -f %{oreon_filedir}/rust-axum0.6-devel.list

%changelog

%autochangelog
