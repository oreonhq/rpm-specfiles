%global source0_hash 16adeb617b963d010179922c2e4e8762df77c75232e17320b459868c4970c44b

Name:           perl-MooX-Types-MooseLike-Numeric
Version:        1.03
Release:        28%{?dist}
Summary:        Moo types for numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Types-MooseLike-Numeric
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATEU/MooX-Types-MooseLike-Numeric-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Moo) > 1.004002
BuildRequires:  perl(MooX::Types::MooseLike) >= 0.23
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(MooX::Types::MooseLike) >= 0.23

# Filter under-specified requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooX::Types::MooseLike\\)$

%description
Moo types for numbers, adapted from MooseX::Types::Common::Numeric.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-Types-MooseLike-Numeric-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
