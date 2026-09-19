%global source0_hash 596df01f8ab79ffffd450e94836a544371d8a4c93a15f7e88ea2f1b79c46849d

Name:           perl-Lingua-PT-Stemmer
Version:        0.02
Release:        28%{?dist}
Summary:        Portuguese language stemming
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-PT-Stemmer
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Lingua-PT-Stemmer-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# -
# Tests only
BuildRequires:  perl(Test)

%description
This module implements a Portuguese stemming algorithm proposed in the
paper A Stemming Algorithm for the Portuguese Language by Moreira, V.
and Huyck, C.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-PT-Stemmer-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
