%global commit 4f5c45238ef77e5d6b88bc403432bd59de7efde9
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           plotnetcfg
Version:        0.4.1
Release:        28%{?dist}
Summary:        A tool to plot network configuration

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/jbenc/plotnetcfg
Source0:        https://github.com/jbenc/plotnetcfg/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires: make
BuildRequires:  gcc, jansson-devel
Requires:       jansson

%description
plotnetcfg is a tool that output a diagram of network configuration on the
host in a form suitable for graphviz.

%prep
%setup -q -n %{name}-%{commit}

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install

%files
%license COPYING
%doc README
%{_sbindir}/plotnetcfg
%{_mandir}/man5/*
%{_mandir}/man8/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.1-28
- Import
