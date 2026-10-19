%global source0_hash 16adeb617b963d010179922c2e4e8762df77c75232e17320b459868c4970c44b
Name:           perl-MooX-Types-MooseLike-Numeric
Version:        1.03
Release:        1%{?dist}
Summary:        Moo types for numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Types-MooseLike-Numeric
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATEU/MooX-Types-MooseLike-Numeric-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(MooX::Types::MooseLike) >= 0.23
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooX::Types::MooseLike\\)$
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
