%global source0_hash 1c9a824ab323e3e58d9808011c10ad27589dba1202806278215012ca7f522875
Name:           perl-bignum
Version:        0.67
Release:        522%{?dist}
Summary:        Transparent big number support for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/bignum
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/bignum-%{version}.tar.gz
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
Requires:       perl(Carp) >= 1.22
Requires:       perl(Math::BigInt) >= 1.999830
Requires:       perl(Math::BigRat) >= 0.2623
Conflicts:      perl < 4:5.22.0-348
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Math::BigInt\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Math::BigRat\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Carp\\)$
Provides:       perl(bigint)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigInt::GMP)
BuildRequires:  perl(Math::BigRat)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package attempts to make it easier to write scripts that use BigInts and
BigFloats in a transparent way.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if !%{defined perl_bootstrap}
Requires:       perl(Math::BigInt::GMP)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n bignum-%{version}

# Correct shebangs and permission
for F in lib/Math/BigInt/Trace.pm lib/Math/BigFloat/Trace.pm; do
    perl -MConfig -pi -e 's{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod -x "$F"
done

# Help generators to recognize Perl scripts
for F in t/*.t; do
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
%files -n perl-bignum-tests -f %{oreon_filedir}/perl-bignum-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.67-522
- Prepare for Oreon 11 (RP1)
