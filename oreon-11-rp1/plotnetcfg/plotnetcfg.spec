%global source0_hash 4f6c3204ac8ddb7115e6fa50ec4c1ec4e537b85a16e1e9104c5d68faac8aba1a
%global commit 4f5c45238ef77e5d6b88bc403432bd59de7efde9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           plotnetcfg
Version:        0.4.1
Release:        28%{?dist}
Summary:        A tool to plot network configuration
License:        GPL-2.0-or-later
URL:            https://github.com/jbenc/plotnetcfg
Source0:        https://github.com/jbenc/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       jansson
# oreon:deps
BuildRequires:  gcc
BuildRequires:  jansson-devel
BuildRequires:  make
# /oreon:deps
%description
plotnetcfg is a tool that output a diagram of network configuration on the
host in a form suitable for graphviz.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{commit}

%build

make %{?_smp_mflags} CFLAGS="%{optflags}"
%install
install -D -m 0755 plotnetcfg %{buildroot}%{_sbindir}/plotnetcfg
install -D -m 0644 plotnetcfg-json.5 %{buildroot}%{_mandir}/man5/plotnetcfg-json.5
install -D -m 0644 plotnetcfg.8 %{buildroot}%{_mandir}/man8/plotnetcfg.8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.1-28
- Import
