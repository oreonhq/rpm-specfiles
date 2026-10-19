%global source2_hash a88480961f4aa0ff5b0b7b84bd3c0b9564140f4fc012b5e27ff87428dbc82a21
%global source1_hash 31a729b6f143d872818b023a72114b924b6de49092a832a7f2057b8b05ab6812
%global source0_hash 81b2a5a8c497edf942225461585e70b20da4bb312f04d992711df3b89e7e27db
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 1
%bcond gpgcheck 1
%global soname libkryoptic_pkcs11
%global features kryoptic-lib/nssdb,kryoptic-lib/pqc,kryoptic-lib/standard,kryoptic-lib/dynamic
Name:           kryoptic
Version:        1.5.0
Release:        1%{?dist}
Summary:        PKCS #11 software token written in Rust
SourceLicense:  GPL-3.0-or-later
License: Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND GPL-3.0-or-later AND ISC AND MIT AND (MIT-0 OR Apache-2.0) AND (Unlicense OR MIT) AND Zlib
URL:            https://github.com/latchset/kryoptic
Source0:        https://github.com/latchset/kryoptic/releases/download/v%{version}/%{name}-%{version}.tar.gz
%if %{with gpgcheck}
Source1:        https://github.com/latchset/kryoptic/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        https://people.redhat.com/~ssorce/simo_redhat.asc
%endif
%if %{with gpgcheck}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gnupg2
BuildRequires:  openssl-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Supporting tools for kryoptic software token
%description tools
Supporting tools for kryoptic software token.
Most notably a migration tool for the SoftHSM database.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if %{with gpgcheck}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1
%oreon_vendor_cargo
%build

export CONFDIR=%{_sysconfdir}
%cargo_build -f %{features} -- --package kryoptic
%cargo_build -f %{features} -- --package kryoptic-tools
%{cargo_license_summary -f %{features}}
%{cargo_license -f %{features}} > LICENSE.dependencies
%install
install -Dp target/rpm/softhsm_migrate $RPM_BUILD_ROOT%{_bindir}/softhsm_migrate
install -Dp target/rpm/%{soname}.so $RPM_BUILD_ROOT%{_libdir}/pkcs11/%{soname}.so
mkdir -p $RPM_BUILD_ROOT%{_datadir}/p11-kit/modules/
echo "module: %{soname}.so" > $RPM_BUILD_ROOT%{_datadir}/p11-kit/modules/kryoptic.module
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -f %{features}
%endif
%files -f %{oreon_filedir}/main.list
%files -n kryoptic-tools -f %{oreon_filedir}/kryoptic-tools.list

%changelog

%autochangelog
