%global source0_hash b4e21dc59b30265eaaa41b705087ec03447d9c655a14ac40ff46e4de29eabf8e

Name:           perl-PBKDF2-Tiny
Version:        0.005
Release:        33%{?dist}
Summary:        Minimalist PBKDF2 (RFC 2898) with HMAC-SHA1 or HMAC-SHA2
# inc/MakeMaker.pm:     GPL-1.0-or-later OR Artistic-1.0-Perl (derived from
#                       Package-Stash:inc/MMPackageStash.pm)
# Makefile.PL:          GPL-1.0-or-later OR Artistic-1.0-Perl (parse_args()
#                       derived from ExtUtils-MakeMaker)
# other files:          Apache-2.0
License:        Apache-2.0
SourceLicense:  %{license} AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/PBKDF2-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/PBKDF2-Tiny-%{version}.tar.gz
BuildArch:      noarch
# The inc/MakeMaker.pm is not run
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Digest::SHA or Digest::SHA::::PurePerl
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter) >= 5.57
# Tests:
# CPAN::Meta 2.120900 not useful
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
# Digest::SHA or Digest::SHA::::PurePerl
Requires:       perl(Digest::SHA)

%description
This module provides an RFC 2898 compliant PBKDF2 implementation using
HMAC-SHA1 or HMAC-SHA2.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PBKDF2-Tiny-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
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
%dir %{perl_vendorlib}/PBKDF2
%{perl_vendorlib}/PBKDF2/Tiny.pm
%{_mandir}/man3/PBKDF2::Tiny.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
