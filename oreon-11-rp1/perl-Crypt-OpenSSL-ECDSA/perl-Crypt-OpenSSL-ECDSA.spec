%global source0_hash 070b6829528c8111c01cd4d264c7cfb5bea7636e25d936f4f87fba8b4e46ff0a

Name:           perl-Crypt-OpenSSL-ECDSA
Version:        0.10
Release:        19%{?dist}
Summary:        Perl extension for OpenSSL ECDSA (Elliptic Curve Digital Signature Algorithm)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-ECDSA
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKEM/Crypt-OpenSSL-ECDSA-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Config)
# Use ExtUtils::Constant to regenerate XS code
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
# Crypt::OpenSSL::EC not used from typemap
# DynaLoader not used to prefer XSLoader
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Crypt::OpenSSL::EC) >= 0.05
BuildRequires:  perl(Test::More)
Requires:       perl(XSLoader)

%description
This package provides a Perl interface to the ECDSA (Elliptic Curve Digital
Signature Algorithm) functions from OpenSSL library.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Crypt::OpenSSL::EC) >= 0.05
Requires:       perl(Crypt::OpenSSL::ECDSA)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-OpenSSL-ECDSA-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
OPENSSL_PREFIX=%{_prefix} perl Makefile.PL INSTALLDIRS=vendor \
    NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
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
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
