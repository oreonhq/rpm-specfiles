%global source0_hash 0f699d73703af4e54446295dce395f66b95efc4c6ba45d4c69eff12d668792ee

Name:           perl-Crypt-OpenSSL-AES
Version:        0.21
Release:        7%{?dist}
Summary:        Perl interface to OpenSSL for AES
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-AES
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Crypt-OpenSSL-AES-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
# openssl for /usr/bin/openssl used by Crypt::OpenSSL::Guess
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::OpenSSL::Guess) >= 0.10
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::More)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Crypt::OpenSSL::Guess\\)$

%description
This module implements a wrapper around OpenSSL. Specifically, it wraps the
methods related to the US Government's Advanced Encryption Standard (the
Rijndael algorithm).

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# openssl for /usr/bin/openssl used by Crypt::OpenSSL::Guess and
# t/00-openssl-version.t.
Requires:       openssl
Requires:       perl-Test-Harness
Requires:       perl(Crypt::OpenSSL::Guess) >= 0.10

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-OpenSSL-AES-%{version}
# Remove always skipped tests
for F in t/01-crypt-cbc.t t/author-pod-spell.t t/author-pod-syntax.t \
        t/release-meta-json.t t/release-kwalitee.t; do
    rm -- "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
unset AUTHOR_TESTING
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorarch}/auto/Crypt
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL
%{perl_vendorarch}/auto/Crypt/OpenSSL/AES
%dir %{perl_vendorarch}/Crypt
%dir %{perl_vendorarch}/Crypt/OpenSSL
%{perl_vendorarch}/Crypt/OpenSSL/AES.pm
%{_mandir}/man3/Crypt::OpenSSL::AES.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
