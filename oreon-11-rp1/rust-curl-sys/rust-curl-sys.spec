%global source0_hash 97799a0d220bfb3361e0fe4936966ff8c4b24d65c3f06dfc70d7b680b44e7897
%bcond check 0
%global debug_package %{nil}
%global crate curl-sys
%global crate_version 0.4.90+curl-8.21.0
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-curl-sys
Version:        0.4.90+curl.8.21.0
Release:        1%{?dist}
Summary:        Native bindings to the libcurl library
License:        MIT
URL:            https://crates.io/crates/curl-sys
Source0:        https://static.crates.io/crates/curl-sys/curl-sys-%{version}.crate
Patch:          curl-sys-fix-metadata-auto.diff
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
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+force-system-lib-on-osx-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+force-system-lib-on-osx-devel

This package contains library source intended for building other packages which
use the "force-system-lib-on-osx" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+libnghttp2-sys-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+libnghttp2-sys-devel

This package contains library source intended for building other packages which
use the "libnghttp2-sys" feature of the "%{crate}" crate.

%package     -n %{name}+mesalink-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+mesalink-devel

This package contains library source intended for building other packages which
use the "mesalink" feature of the "%{crate}" crate.

%package     -n %{name}+ntlm-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+ntlm-devel

This package contains library source intended for building other packages which
use the "ntlm" feature of the "%{crate}" crate.

%package     -n %{name}+poll_7_68_0-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+poll_7_68_0-devel

This package contains library source intended for building other packages which
use the "poll_7_68_0" feature of the "%{crate}" crate.

%package     -n %{name}+protocol-ftp-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+protocol-ftp-devel

This package contains library source intended for building other packages which
use the "protocol-ftp" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-ffi-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+rustls-ffi-devel

This package contains library source intended for building other packages which
use the "rustls-ffi" feature of the "%{crate}" crate.

%package     -n %{name}+spnego-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+spnego-devel

This package contains library source intended for building other packages which
use the "spnego" feature of the "%{crate}" crate.

%package     -n %{name}+ssl-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+ssl-devel

This package contains library source intended for building other packages which
use the "ssl" feature of the "%{crate}" crate.

%package     -n %{name}+static-curl-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+static-curl-devel

This package contains library source intended for building other packages which
use the "static-curl" feature of the "%{crate}" crate.

%package     -n %{name}+static-ssl-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+static-ssl-devel

This package contains library source intended for building other packages which
use the "static-ssl" feature of the "%{crate}" crate.

%package     -n %{name}+upkeep_7_62_0-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+upkeep_7_62_0-devel

This package contains library source intended for building other packages which
use the "upkeep_7_62_0" feature of the "%{crate}" crate.

%package     -n %{name}+windows-static-ssl-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+windows-static-ssl-devel

This package contains library source intended for building other packages which
use the "windows-static-ssl" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-ng-compat-devel
Summary:        Native bindings to the libcurl library
BuildArch:      noarch
%description -n %{name}+zlib-ng-compat-devel

This package contains library source intended for building other packages which
use the "zlib-ng-compat" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-curl-sys-devel -f %{oreon_filedir}/rust-curl-sys-devel.list

%changelog

%autochangelog
