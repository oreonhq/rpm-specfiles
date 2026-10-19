%global source0_hash daf871488603e659b0501224cf0731ac317809b1d1701fc061cb4f6ae39a894f
%global with_debug 1
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif
Name: aardvark-dns
%if %{defined copr_username}
Epoch: 102
%else
Epoch: 2
%endif
Version: 2.1.0
License: Apache-2.0 AND MIT AND Zlib
Release:        1%{?dist}
%if %{defined golang_arches_future}
ExclusiveArch: %{golang_arches_future}
%else
ExclusiveArch: aarch64 ppc64le s390x x86_64
%endif
Summary:        Authoritative DNS server for A/AAAA container records
URL: https://github.com/containers/%{name}
Source0:        https://github.com/containers/aardvark-dns/archive/refs/tags/v2.1.0.tar.gz#/aardvark-dns-2.1.0.tar.gz
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  rustc
# /oreon:deps
%description
%{summary}

Forwards other request to configured resolvers.
Read more about configuration in `src/backend/mod.rs`.

%package tests
Summary: Tests for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: bats
Requires: bind-utils
Requires: jq
Requires: netavark
Requires: socat
Requires: dnsmasq
%description tests
%{summary}

This package contains system tests for %{name} and is only intended to be used
for gating tests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git %{name}-%{version}
%if !%{defined copr_username}
tar fx %{SOURCE1}
%if 0%{?fedora} || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%else
%endif
%endif
%oreon_vendor_cargo
%build

%{__make} CARGO="%{__cargo}" build
%if (0%{?fedora} || 0%{?rhel} >= 10 || 0%{?oreon} >= 11) && !%{defined copr_username}
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest
%endif
%install
%{__make} DESTDIR=%{buildroot} PREFIX=%{_prefix} install
%{__install} -d -p %{buildroot}%{_datadir}/%{name}/test
%{__cp} -rp test/* %{buildroot}%{_datadir}/%{name}/test/
%{__rm} -rf %{buildroot}%{_datadir}/%{name}/test/tmt/
%oreon_autofiles aardvark-dns-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n aardvark-dns-tests -f %{oreon_filedir}/aardvark-dns-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17.0-1
- Prepare for Oreon 11 (RP1)
