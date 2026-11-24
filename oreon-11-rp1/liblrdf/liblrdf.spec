# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8192f5286185a9472d46dfe2e9c3c55fc3717791d4fb9ab71b428d25792b711c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:      Library for manipulating RDF files describing LADSPA plugins
Name:         liblrdf
Version:      0.5.0
Release:      1%{?dist}
License:      GPL-2.0-or-later
URL:          https://github.com/swh/LRDF
Source0:      liblrdf-%{version}.tar.gz
Source1:      liblrdf-README.fedora
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: ladspa-devel
BuildRequires: openssl-devel
BuildRequires: raptor2-devel
BuildRequires: make
Requires:     ladspa

%description
liblrdf is a library to make it easy to manipulate RDF files describing
LADSPA plugins.

%package devel
Summary:      Library for manipulating RDF files describing LADSPA plugins
Requires:     liblrdf%{?_isa} = %{version}-%{release}
Requires:     raptor2-devel

%description devel
This is a library to make it easy to manipulate RDF files describing
LADSPA plugins. This package includes the development tools.

%prep
%oreon_sha256
%setup -q
cp -a %{SOURCE1} README.fedora

%build
%configure --disable-static

%install
%{make_install}
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/liblrdf.so.*
%{_datadir}/ladspa/rdf/ladspa.rdfs

%files devel
%doc ChangeLog README.fedora
%{_includedir}/*
%{_libdir}/liblrdf.so
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
