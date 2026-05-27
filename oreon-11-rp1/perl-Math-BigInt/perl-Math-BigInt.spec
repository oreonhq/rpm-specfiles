%global source0_hash c4adc1202349f7fcd14d01e6949fee0ec969049d45c9ca59aa29ec58a65966db

Name:           perl-Math-BigInt
Epoch:          1
%global cpan_version 2.005003
# Keep 4-digit version to compete with perl.spec
Version:        %(echo %{cpan_version} | sed 's/\(\.....\)/\1./')
Release:        4%{?dist}
Summary:        Arbitrary-size integer and float mathematics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-BigInt
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(Math::Complex) >= 1.39
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
# Module::Signature not used
# Socket not used
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Carp) >= 1.22
Requires:       perl(Math::Complex) >= 1.39
Conflicts:      perl < 4:5.22.0-347

Provides:       perl-Math-BigRat =  %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      perl-Math-BigRat < 0.2624-502

# Do not export unversioned module
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::BigInt\\)\\s*$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Carp\\)\\s*$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(.::t/.*.inc\\)
%global __requires_exclude %{__requires_exclude}|perl\\(Math::BigFloat::(BareSubclass\|Subclass)\\)
%global __requires_exclude %{__requires_exclude}|perl\\(Math::BigInt::(BareCalc\|Scalar\|Subclass)\\)
%global __requires_exclude %{__requires_exclude}|perl\\(Math::BigInt::Lib::(Minimal\|TestUtil)\\)
%global __requires_exclude %{__requires_exclude}|perl\\(Math::BigRat::Subclass\\)

%description
This provides Perl modules for arbitrary-size integer and float mathematics.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Math-BigInt-%{cpan_version}

# Help generators to recognize Perl scripts
for F in t/*.t t/alias.inc; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
rm %{buildroot}%{_libexecdir}/%{name}/t/00sig.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset TEST_SIGNATURE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# NEW file is useless
%doc BUGS CHANGES CREDITS examples GOALS HISTORY README TODO
%{perl_vendorlib}/Math*
%{_mandir}/man3/Math::Big*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:2.0050.03-4
- Import
