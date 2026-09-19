%global source0_hash 71f577ad4af10167515ca20ebbc83dbbf503bdc87aa99beffb3afeadb035a8d6

Name:           perl-Wiki-Toolkit
Version:        0.87
Release:        16%{?dist}
Summary:        Toolkit for building Wikis
# Wiki/Toolkit pod
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://metacpan.org/release/Wiki-Toolkit
Source0:        http://cpan.metacpan.org/authors/id/B/BO/BOB/Wiki-Toolkit-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(DBD::SQLite) >= 0.25
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Lingua::Stem)
BuildRequires:  perl(lib)
# runtime deps
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::PullParser)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Text::WikiFormat)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Time::Seconds)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# test deps
BuildRequires:  perl(Hook::LexWrap)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(warnings)

%{?perl_default_filter}

# There are several search backends provided by Wiki-Toolkit. Because we
# don't want to force one on our users, we filter all their requires out.
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Apache2::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBIx::FullTextSearch\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Lucy::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Plucene::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Search::

# Wiki-Toolkit can store configuration from previous tests runs. We
# don't want this so we exclude it from the requires
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Wiki::Toolkit::TestConfig\\)$

%description
Helps you develop Wikis quickly by taking care of the boring bits for you.
You will still need to write some code - this isn't an instant Wiki.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Wiki-Toolkit-%{version}
chmod -x lib/Wiki/Toolkit/Feed/{Atom,RSS}.pm

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Wiki*
%{_bindir}/wiki-toolkit-*
%{_mandir}/man1/wiki-toolkit*
%{_mandir}/man3/Wiki*

%changelog
%autochangelog
