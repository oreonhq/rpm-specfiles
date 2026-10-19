%global source0_hash f787efaf9b8dcd1b51085f190acdaae155007a78ba668ffe40d56226f5f2b488
Name:           perl-XML-Smart
Version:        1.79
Release:        36%{?dist}
Summary:        Smart, easy and powerful way to access/create XML files/data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Smart
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMHARISH/XML-Smart-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Requires:       perl(Devel::Cycle)
Requires:       perl(LWP)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Object::MultiType) >= 0.03
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Object::MultiType\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Object::MultiType)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides an easy way to access/create XML data. It's based on a
HASH tree created from the XML data, and enables dynamic access to it
through the standard Perl syntax for Hash and Array, without necessarily
caring about which you are working with. In other words, each point in the
tree works as a Hash and an Array at the same time!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Smart-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
