%global source0_hash e251a51abc7d9ba3e708f73c2aa208e09d47a0c528d6254710fa78cc8d6885b5

Name:           perl-Dir-Self
Version:        0.11
Release:        31%{?dist}
Summary:        A __DIR__ constant for the directory your source file is in
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dir-Self
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAUKE/Dir-Self-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)

%description
Perl has two pseudo-constants describing the current location in your
source code, __FILE__ and __LINE__. This module adds __DIR__, which expands
to the directory your source file is in, as an absolute pathname.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dir-Self-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
