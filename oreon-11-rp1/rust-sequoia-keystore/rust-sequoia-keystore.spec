%global source0_hash 50e5887d0c3c5f0df1d1cab937ef7a5c398111ddfd911c714f28c904438f229c
%bcond check 0
%global debug_package %{nil}
%global crate sequoia-keystore
Name:           rust-sequoia-keystore
Version:        0.7.2
Release:        1%{?dist}
Summary:        Sequoia's private key store server.
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-keystore
Source0:        https://static.crates.io/crates/sequoia-keystore/sequoia-keystore-%{version}.crate
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
Summary:        Sequoia's private key store server.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gpg-agent-devel
Summary:        Sequoia's private key store server.
BuildArch:      noarch
%description -n %{name}+gpg-agent-devel

This package contains library source intended for building other packages which
use the "gpg-agent" feature of the "%{crate}" crate.

%package     -n %{name}+openpgp-card-devel
Summary:        Sequoia's private key store server.
BuildArch:      noarch
%description -n %{name}+openpgp-card-devel

This package contains library source intended for building other packages which
use the "openpgp-card" feature of the "%{crate}" crate.

%package     -n %{name}+softkeys-devel
Summary:        Sequoia's private key store server.
BuildArch:      noarch
%description -n %{name}+softkeys-devel

This package contains library source intended for building other packages which
use the "softkeys" feature of the "%{crate}" crate.

%package     -n %{name}+tpm-devel
Summary:        Sequoia's private key store server.
BuildArch:      noarch
%description -n %{name}+tpm-devel

This package contains library source intended for building other packages which
use the "tpm" feature of the "%{crate}" crate.

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
%files -n rust-sequoia-keystore-devel -f %{oreon_filedir}/rust-sequoia-keystore-devel.list

%changelog

%autochangelog
