%global source0_hash 0cee260920954a806e73a39a52aa47d6fcb84dad81b2c08af1f9ae0f25d8be1e

Name:           perl-Text-Shellwords
Version:        1.08
Release:        52%{?dist}
Summary:        A thin wrapper around the shellwords.pl package

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Shellwords
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDS/Text-Shellwords-1.08.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(vars)
# Test:
BuildRequires:  perl(Test)

%description
This is a thin wrapper around the shellwords.pl package, which comes
preinstalled with Perl.  This module imports a single subroutine,
shellwords().  The shellwords() routine parses lines of text and
returns a set of tokens using the same rules that the Unix shell does
for its command-line arguments.  Tokens are separated by whitespace,
and can be delimited by single or double quotes.  The module also
respects backslash escapes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Shellwords-%{version}
# Clean up /usr/local/bin/perl mess
#%%{__perl} -pi -e 's|/usr/local/bin/perl\b|%%{__perl}|' \
#  qd.pl bdf_scripts/cvtbdf.pl demos/{*.{pl,cgi},truetype_test}

# avoid dependencies
#chmod 644 examples/* 

%build 
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags} 

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
