%global source0_hash 8aeab8b648f09988ab259092d5327ee1db3d668695007595d87c6fbe0fab5e08

Name:           perl-Crypt-OpenSSL-PKCS10
Version:        0.37
Release:        1%{?dist}
Summary:        Perl interface to OpenSSL for PKCS10
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-PKCS10
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-OpenSSL-PKCS10-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
# It's required for successful Crypt::OpenSSL::Guess process.
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::OpenSSL::Guess) >= 0.11
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Crypt::OpenSSL::RSA)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(Test::Lib)
BuildRequires:  perl(Test::More)

# Remove private test modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::Crypt::OpenSSL::PKCS10|Test::Crypt::OpenSSL::PKCS10::Util\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Test::Crypt::OpenSSL::PKCS10|Test::Crypt::OpenSSL::PKCS10::Util\\)$

%description
Crypt::OpenSSL::PKCS10 Perl module provides the ability to create PKCS10
certificate requests using RSA key pairs.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       openssl
Requires:       perl(Crypt::OpenSSL::RSA)
Requires:       perl-Test-Harness

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Crypt-OpenSSL-PKCS10-%{version}
# Help file to recognize the Perl scripts and normalize shebangs
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
# Remove release/author tests
rm %{buildroot}/%{_libexecdir}/%{name}/t/author*
rm %{buildroot}/%{_libexecdir}/%{name}/t/release*
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING RELEASE_TESTING
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt*
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/Crypt::OpenSSL::PKCS10*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
