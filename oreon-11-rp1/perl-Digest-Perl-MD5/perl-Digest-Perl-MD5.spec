%global source0_hash 718e41717fb82a9ab3f0809d211fddcdbdef91dc198887d82b88723aa54afcd5

Name:		perl-Digest-Perl-MD5
Version:	1.91
Release:	1%{?dist}
Summary:	Perl implementation of Ron Rivest's MD5 Algorithm
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Digest-Perl-MD5
Source0:	https://cpan.metacpan.org/modules/by-module/Digest/Digest-Perl-MD5-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Exporter)
BuildRequires:	perl(integer)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(Test)
# Dependencies
Requires:	perl(Symbol)

%description
A pure-perl implementation of Ron Rivest's MD5 Algorithm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Digest-Perl-MD5-%{version}

# Remove spurious exec permissions
chmod -c -x lib/Digest/Perl/MD5.pm README.md

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
make pure_install DESTDIR=%{buildroot}
%{make_install}
%{_fixperms} -c %{buildroot}

%check
MD5_SPEED_TEST=500000 make test

%files
%doc CHANGES README.md
%{perl_vendorlib}/Digest/
%{_mandir}/man3/Digest::Perl::MD5.3*

%changelog
%autochangelog
