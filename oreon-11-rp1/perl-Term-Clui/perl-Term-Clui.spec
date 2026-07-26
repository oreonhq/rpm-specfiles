%global source0_hash b8ee8cd2252a43244d1f84b76eb0407e72eafc24e5d53aabac719d869dfbf11f

Name:           perl-Term-Clui
Version:        1.76
Release:        19%{?dist}
Summary:        Perl module offering a Command-Line User Interface
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Term-Clui
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Term-Clui-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(Term::Size)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::ReadLine::Gnu)
Requires:       perl(Term::Size)
Requires:       perl(strict)
Requires:       perl(warnings)

%{?perl_default_filter}

%description
Term::Clui offers a high-level user interface to give the user of command-
line applications a consistent "look and feel". Its metaphor for the
computer is as a human-like conversation-partner, and as each
question/response is completed it is summarized onto one line, and remains
on screen, so that the history of the session gradually accumulates on the
screen and is available for review, or for cut/paste. This user interface
can therefore be intermixed with standard applications which write to
STDOUT or STDERR, such as make, pgp, rcs etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-Clui-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README examples
%license LICENSE
%{perl_vendorlib}/Term*
%{_mandir}/man3/Term*

%changelog
%autochangelog
