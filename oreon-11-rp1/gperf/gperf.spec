# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fd87e0aba7e43ae054837afd6cd4db03a3f2693deb3619085e6ed9d8d9604ad8

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Summary: A perfect hash function generator
Name: gperf
Version:        3.3
Release:        1%{?dist}
License: GPL-3.0-or-later
Source0:        https://mirror.cs.odu.edu/gnu/gperf/gperf-%{version}.tar.gz
URL: http://www.gnu.org/software/gperf/

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  oreon-rpm-macros

%description
Gperf is a perfect hash function generator written in C++. Simply
stated, a perfect hash function is a hash function and a data
structure that allows recognition of a key word in a set of words
using exactly one probe into the data structure.

%prep
%oreon_sha256

%setup -q

%build
%configure
%make_build

%install
#mkdir -p $RPM_BUILD_ROOT/usr/share/{man,info}
%make_install

# remove the stuff from the buildroot
rm -rf $RPM_BUILD_ROOT{%{_mandir}/{dvi,html},%{_datadir}/doc}

%files
%doc README NEWS doc/*.{html,pdf} COPYING
%{_bindir}/%{name}
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*

