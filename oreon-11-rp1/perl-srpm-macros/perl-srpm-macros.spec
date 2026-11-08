# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c53fce1e43c393b643425d857cd327a02612e645412dfbb774304053ea5e1d4b


%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:       perl-srpm-macros    
Version:        1
Release:        2%{?dist}
Summary:    RPM macros for building Perl source package from source repository
License:    GPL-3.0-or-later
Source0:    macros.perl-srpm
BuildArch:  noarch
BuildRequires:  oreon-rpm-macros

%description
These RPM macros are used for building Perl source packages from source
repositories. They influence build-requires set into the source package.

%prep
%oreon_sha256

%install
install -m 644 -D "%{SOURCE0}" \
    '%{buildroot}%{_rpmconfigdir}/macros.d/macros.perl-srpm'

%files
%{_rpmconfigdir}/macros.d/macros.perl-srpm

