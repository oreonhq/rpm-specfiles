%global source0_hash 5ec4425c6bc22207889630be7350d99686e62a44c6136960110203cd594ae0ea

Name:           perl-Crypt-RC4
Version:        2.02
Release:        43%{?dist}
Summary:        Perl implementation of the RC4 encryption algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-RC4
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIFUKURT/Crypt-RC4-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%description
A simple implementation of the RC4 algorithm, developed by RSA Security,
Inc. Here is the description from RSA's website:

RC4 is a stream cipher designed by Rivest for RSA Data Security (now RSA
Security). It is a variable key-size stream cipher with byte-oriented
operations. The algorithm is based on the use of a random permutation. Analysis
shows that the period of the cipher is overwhelmingly likely to be greater than
10100. Eight to sixteen machine operations are required per output byte, and
the cipher can be expected to run very quickly in software. Independent analysts
have scrutinized the algorithm and it is considered secure.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-RC4-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a test.pl %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . test.pl
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc Changes
%dir %{perl_vendorlib}/Crypt
%{perl_vendorlib}/Crypt/RC4.pm
%{_mandir}/man3/Crypt::RC4.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
