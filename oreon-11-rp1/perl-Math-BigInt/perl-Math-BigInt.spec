%global source0_hash c4adc1202349f7fcd14d01e6949fee0ec969049d45c9ca59aa29ec58a65966db
Name:           perl-Math-BigInt
Epoch:          1
%global cpan_version 2.005003
Version:        %(echo %{cpan_version} | sed 's/\(\.....\)/\1./')
Release:        1%{?dist}
Summary:        Arbitrary-size integer and float mathematics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-BigInt
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-2.005003.tar.gz
BuildArch:      noarch
Requires:       perl(Carp) >= 1.22
Requires:       perl(Math::Complex) >= 1.39
Conflicts:      perl < 4:5.22.0-347
Provides:       perl-Math-BigRat =  %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      perl-Math-BigRat < 0.2624-502
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::BigInt\\)\\s*$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Carp\\)\\s*$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(.::t/.*.inc\\)
%global __requires_exclude %{__requires_exclude}|perl\\(Math::BigFloat::(BareSubclass\|Subclass)\\)
%global __requires_exclude %{__requires_exclude}|perl\\(Math::BigInt::(BareCalc\|Scalar\|Subclass)\\)
%global __requires_exclude %{__requires_exclude}|perl\\(Math::BigInt::Lib::(Minimal\|TestUtil)\\)
%global __requires_exclude %{__requires_exclude}|perl\\(Math::BigRat::Subclass\\)
Provides:       perl(Math::BigInt)
Provides:       perl(Math::BigInt::Calc)
Provides:       perl(Math::BigInt::Lib)
Provides:       perl(Math::BigFloat)
Provides:       perl(Math::BigRat)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::Complex)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00sig.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset TEST_SIGNATURE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Math-BigInt-tests -f %{oreon_filedir}/perl-Math-BigInt-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:2.0050.03-4
- Import
