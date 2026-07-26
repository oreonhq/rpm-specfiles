%global source0_hash f186ca66c7579d0ca8f673c0c096603089ea8ecc88b3e14260d0a1b11f4f94fe

Name:           perl-Term-Prompt
Version:        1.04
Release:        46%{?dist}
Summary:        Perl extension for prompting a user for information
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Prompt
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERSICOM/Term-Prompt-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ReadKey) >= 1
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)

%description
This main function of this module is to accept interactive input. You
specify the type of inputs allowed, a prompt, help text and defaults and it
will deal with the user interface, (and the user!), by displaying the
prompt, showing the default, and checking to be sure that the response is
one of the legal choices. Additional 'types' that could be added would be a
phone type, a social security type, a generic numeric pattern type...

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-Prompt-%{version}
for f in $(find . -type f); do
    chmod a-x -c $f
    perl -pi -e 's/\r//g' $f
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
