%global source0_hash 5a1a8afbb13ed083be44d974f95d2093e541d43ce7bca787d49c0cd3d5aca04d

Name:           perl-Pod-Stripper
Version:        0.22
Release:        29%{?dist}
Summary:        Strip all pod, and output what's left
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Stripper
Source0:        https://cpan.metacpan.org/authors/id/P/PO/PODMASTER/Pod-Stripper-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Pod::Parser) >= 1.13
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Test) >= 1.15
Requires:       perl(Pod::Parser) >= 1.13

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Pod::Parser\\)\s*$

Provides:       perl(Pod::Stripper)
%description
This be Pod::Stripper, a subclass of Pod::Parser. It parses perl files,
stripping out the pod, and dumping the rest (presumably code) to wherever
you point it to (like you do with Pod::Parser).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Stripper-%{version}
sed -i 's/\r//' Changes README podstrip

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
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
