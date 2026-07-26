%global source0_hash 810c429fb4647d7c5855eb07c1c7ed25fd1d5ffd2e4c24c589e1b4a480dfc95f

Name:           perl-SVN-Look
Version:        0.43
Release:        11%{?dist}
Summary:        Caching wrapper around the svnlook command
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SVN-Look
Source0:        https://cpan.metacpan.org/authors/id/G/GN/GNUSTAVO/SVN-Look-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(XML::Simple)
BuildRequires:  subversion
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::file)
Requires:       perl(File::Temp)
Requires:       perl(MIME::Base64)
Requires:       perl(XML::Simple)
Requires:       subversion

%description
The svnlook command is the workhorse of Subversion hook scripts, being used
to gather all sorts of information about a repository, its revisions, and
its transactions. This module provides a simple object oriented interface
to a specific svnlook invocation, to make it easier to hook writers to get
and use the information they need. Moreover, all the information gathered
by calling the svnlook command is cached in the object, avoiding
repetitious calls.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SVN-Look-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
