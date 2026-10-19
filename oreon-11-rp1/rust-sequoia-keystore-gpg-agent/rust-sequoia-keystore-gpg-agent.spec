%global source0_hash 7ad901f1f1d88b38f5f5738d5bf2b80136ec44e94a40716193be0bbf3314df2b
%bcond check 0
%global debug_package %{nil}
%global crate sequoia-keystore-gpg-agent
Name:           rust-sequoia-keystore-gpg-agent
Version:        0.5.0
Release:        1%{?dist}
Summary:        A gpg-agent backend for Sequoia's private key store.
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-keystore-gpg-agent
Source0:        https://static.crates.io/crates/sequoia-keystore-gpg-agent/sequoia-keystore-gpg-agent-%{version}.crate
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
Summary:        A gpg-agent backend for Sequoia's private key store.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-sequoia-keystore-gpg-agent-devel -f %{oreon_filedir}/rust-sequoia-keystore-gpg-agent-devel.list

%changelog

%autochangelog
