# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 96c65cc96a2fe9fe9293cc496482c34bd2eed8a8b560db94506659cd2e5b87ca
%global source1_hash 3f3d9e0024b1921b067d6f7f88deb4a60cbe7a78e76c64e3f1d7fc3b779b9d04
%global source2_hash 8f50ad958916d6a8f79fba2363501475571acce752757f9126fe9d2f17dd920d

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%bcond_without  dafsa

Name:           publicsuffix-list
Version:        20260624
Release:        1%{?dist}
Summary:        Cross-vendor public domain suffix database

License:        MPL-2.0
URL:            https://publicsuffix.org/
Source0:        https://raw.githubusercontent.com/publicsuffix/list/18ecca5d54471f21918798da451dd8d03a18f3c7/public_suffix_list.dat
Source1:        https://www.mozilla.org/media/MPL/2.0/index.txt
Source2:        https://raw.githubusercontent.com/publicsuffix/list/18ecca5d54471f21918798da451dd8d03a18f3c7/tests/test_psl.txt

BuildArch:      noarch

%if %{with dafsa}
BuildRequires:  psl-make-dafsa
BuildRequires:  oreon-rpm-macros
%endif


%description
The Public Suffix List is a cross-vendor initiative to provide
an accurate list of domain name suffixes, maintained by the hard work 
of Mozilla volunteers and by submissions from registries.
Software using the Public Suffix List will be able to determine where 
cookies may and may not be set, protecting the user from being 
tracked across sites.

%if %{with dafsa}
%package dafsa
Summary:        Cross-vendor public domain suffix database in DAFSA form

%description dafsa
The Public Suffix List is a cross-vendor initiative to provide
an accurate list of domain name suffixes, maintained by the hard work 
of Mozilla volunteers and by submissions from registries.
Software using the Public Suffix List will be able to determine where 
cookies may and may not be set, protecting the user from being 
tracked across sites.

This package includes a DAFSA representation of the Public Suffix List
for runtime loading.
%endif


%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -

%setup -c -T
cp -av %{SOURCE0} .
install -m 644 -p -v %{SOURCE1} COPYING


%build
%if %{with dafsa}
LC_CTYPE=C.UTF-8 \
psl-make-dafsa --output-format=binary \
  public_suffix_list.dat public_suffix_list.dafsa
%endif


%install
%if %{with dafsa}
install -m 644 -p -D public_suffix_list.dafsa $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/public_suffix_list.dafsa
%endif
install -m 644 -p -D %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/public_suffix_list.dat
install -m 644 -p -D %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/test_psl.txt
ln -s public_suffix_list.dat $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/effective_tld_names.dat


%files
%license COPYING
%dir %{_datadir}/publicsuffix
%{_datadir}/publicsuffix/effective_tld_names.dat
%{_datadir}/publicsuffix/public_suffix_list.dat
%{_datadir}/publicsuffix/test_psl.txt

%if %{with dafsa}
%files dafsa
%license COPYING
%dir %{_datadir}/publicsuffix
%{_datadir}/publicsuffix/public_suffix_list.dafsa
%endif


