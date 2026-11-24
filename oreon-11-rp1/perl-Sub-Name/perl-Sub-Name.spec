# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 39c53f6b3b02cbc73176564413b51d3c0f375f9760983fd579c27f558b169cfc
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?oreon}
%bcond_with perl_Sub_Name_enables_optional_test
%else
%bcond_without perl_Sub_Name_enables_optional_test
%endif

Name:		perl-Sub-Name
Version:	0.28
Release:	1%{?dist}
Summary:	Name - or rename - a sub
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Sub-Name
Source0:	https://www.cpan.org/modules/by-module/Sub/Sub-Name-%{version}.tar.gz
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
BuildRequires:	perl(B)
BuildRequires:	perl(B::Deparse)
BuildRequires:	perl(Carp)
BuildRequires:	perl(feature)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(if)
BuildRequires:	perl(Test::More)
%if %{with perl_Sub_Name_enables_optional_test}
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(Devel::CheckBin)
%endif

%{?perl_default_filter}

%description
This module allows one to "name" or rename subroutines, including anonymous
ones.

Note that this is mainly for aid in debugging; you still cannot call the sub
by the new name (without some deep magic).

%prep
%oreon_sha256
%setup -q -n Sub-Name-%{version}

%build
perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	optimize="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorarch}/auto/Sub/
%{perl_vendorarch}/Sub/
%{_mandir}/man3/Sub::Name.3*

%changelog
%autochangelog
