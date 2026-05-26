Name:           perl-Digest-HMAC
Version:        1.05
Release:        4%{?dist}
Summary:        Keyed-Hashing for Message Authentication
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Digest-HMAC
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/Digest-HMAC-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 215cb59cba610745cfb2d4b3f8ef756d590e57e3ad7986a992e87c4969fcdc7a
%global source0_file Digest-HMAC-1.05.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Digest::MD5) >= 2
BuildRequires:  perl(Digest::SHA) >= 1
BuildRequires:  perl(Exporter)
BuildRequires:  perl(vars)
# Tests:
# Config not used on Linux
Requires:       perl(Digest::MD5) >= 2
Requires:       perl(Digest::SHA) >= 1

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Digest::(MD5|SHA)\\)$

%description
HMAC is used for message integrity checks between two parties that
share a secret key, and works in combination with some other Digest
algorithm, usually MD5 or SHA-1. The HMAC mechanism is described in
RFC 2104.

HMAC follow the common Digest:: interface, but the constructor takes
the secret key and the name of some other simple Digest:: as argument.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Digest-HMAC-1.05.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "215cb59cba610745cfb2d4b3f8ef756d590e57e3ad7986a992e87c4969fcdc7a" || { echo "oreon: Source0 SHA256 mismatch for Digest-HMAC-1.05.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Digest-HMAC-%{version} 

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
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
%{perl_vendorlib}/Digest/
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.05-4
- Prepare for Oreon 11 (RP1)
