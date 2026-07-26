%global source0_hash 60bfdd6d4c158b88d370133fc65b20485a36a45b12d906000b81c78ca524163d

Name:           perl-Term-UI
Version:        0.50
Release:        15%{?dist}
Summary:        Term::ReadLine user interface made easy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-UI
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Term-UI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(if)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Log::Message)
BuildRequires:  perl(Log::Message::Simple)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.31
Requires:       perl(deprecate)
Requires:       perl(Exporter)
Requires:       perl(Log::Message::Simple)

%description
Term::UI is a transparent way of eliminating the overhead of having to
format a question and then validate the reply, informing the user if the
answer was not proper and re-issuing the question.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-UI-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
