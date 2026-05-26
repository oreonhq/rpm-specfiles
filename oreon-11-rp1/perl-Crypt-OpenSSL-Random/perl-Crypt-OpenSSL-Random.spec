Name:           perl-Crypt-OpenSSL-Random
Version:        0.17
Release:        6%{?dist}
Summary:        OpenSSL/LibreSSL pseudo-random number generator access
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-Random
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Crypt-OpenSSL-Random-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 a571b24181baaa76c96704e92acffc6934ff593e380dade274db4e43c140ad51
%global source0_file Crypt-OpenSSL-Random-0.17.tar.gz
# oreon url source checksums end
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# perl-podlators for pod2text not needed if Random.pm is older than README
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::OpenSSL::Guess) >= 0.11
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00

%{?perl_default_filter}

%description
Crypt::OpenSSL::Random provides the ability to seed and query the OpenSSL
and LibreSSL library's pseudo-random number generators.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Crypt-OpenSSL-Random-0.17.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a571b24181baaa76c96704e92acffc6934ff593e380dade274db4e43c140ad51" || { echo "oreon: Source0 SHA256 mismatch for Crypt-OpenSSL-Random-0.17.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Crypt-OpenSSL-Random-%{version}
# Remove author-only tests that are always skipped
for F in t/z_kwalitee.t t/z_manifest.t t/z_meta.t t/z_perl_minimum_version.t \
     t/z_pod-coverage.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\E'"$F"'\Q}' MANIFEST
done;

%build
unset AUTOMATED_TESTING
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/z_pod.t
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
%{perl_vendorarch}/auto/Crypt/OpenSSL/Random
%dir %{perl_vendorarch}/Crypt
%dir %{perl_vendorarch}/Crypt/OpenSSL
%{perl_vendorarch}/Crypt/OpenSSL/Random.pm
%{_mandir}/man3/Crypt::OpenSSL::Random.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17-6
- Prepare for Oreon 11 (RP1)
