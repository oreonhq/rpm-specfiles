%global source0_hash df8535321eb92d71f93fbb1777ab8a5c36fe142cff8ab3825011b25da2de6d31

Name:           perl-HTML-TreeBuilderX-ASP_NET
Version:        0.09
Release:        37%{?dist}
Summary:        Scrape ASP.NET/VB.NET sites which utilize Javascript POST-backs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-TreeBuilderX-ASP_NET
Source0:        https://cpan.metacpan.org/authors/id/E/EC/ECARROLL/HTML-TreeBuilderX-ASP_NET-%{version}.tar.gz
# merged upstream https://github.com/EvanCarroll/perl-html-treebuilderx-asp_net/pull/1
Patch0:         HTML-TreeBuilderX-ASP_NET-new_moose.diff
Patch1:         HTML-TreeBuilderX-ASP_NET-0.09-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter >= 0:5.10.0
BuildRequires:  perl-generators
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Request::Form)
BuildRequires:  perl(Moose) >= 0.89
BuildRequires:  perl(MooseX::Traits)
BuildRequires:  perl(MooseX::Types) >= 0.19
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(mro)
BuildRequires:  perl(vars)
BuildRequires:  perl(strict)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(HTML::Element)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(CPAN)
Requires:       perl(Class::MOP)
Requires:       perl(HTML::TreeBuilder)
Requires:       perl(Moose) >= 0.89
Requires:       perl(MooseX::Traits)
Requires:       perl(MooseX::Types) >= 0.19

%global __requires_exclude perl\\(Moose|perl\\(MooseX::Types

%description
Scrape ASP.NET sites which utilize the language's __VIEWSTATE,
__EVENTTARGET, __EVENTARGUMENT, __LASTFOCUS, et al. This module returns a
HTTP::Response from the form with the use of the method ->httpResponse.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-TreeBuilderX-ASP_NET-%{version}
%patch -P0 -p0
%patch -P1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
