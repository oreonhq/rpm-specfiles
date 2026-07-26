%global source0_hash 6ee66d0eed81882ec4fa48fffe163a04fd98c4d56ac1e8cdc14a9f83bd1839bc

Name:           perl-Statistics-CaseResampling
Version:        0.17
Release:        3%{?dist}
Summary:        Resampling and calculation of medians with confidence intervals
# Mersenne Twister is somewhat bundled, CPAN RT#85284
# _mt.c, mt.h:  BSD-3-Clause (license text copied in mt19937ar.license,
#               <http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/MT2002/CODES/mt19937ar.c>)
#               OR "to be usable freely since 2001-04-06"
#               (<http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/MT2002/elicense.html>)
# lib/Statistics/CaseResampling.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# ppport.h:     GPL-1.0-or-later OR Artistic-1.0-Perl
# README:       GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause
URL:            https://metacpan.org/release/Statistics-CaseResampling
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Statistics-CaseResampling-%{version}.tar.gz
# An excerpt from
# <http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/MT2002/CODES/mt19937ar.c>.
Source1:        mt19937ar.license
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
Provides:       bundled(mt19937ar) = 20020126

%{?perl_default_filter}

%description
The purpose of this module is to calculate the median (or in principle also
other statistics) with confidence intervals on a sample. To do that, it uses
a technique called boot-strapping. In a nutshell, it resamples the sample
a lot of times and for each resample, it calculates the median. From the
distribution of medians, it then calculates the confidence limits.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Statistics-CaseResampling-%{version}
install -m 0644 %{SOURCE1} mt19937ar.license
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find "$RPM_BUILD_ROOT" -type f -name '*.bs' -size 0 -delete
%{_fixperms} "$RPM_BUILD_ROOT"/*
# Install tests
mkdir -p "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cp -a t "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cat > "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license mt19937ar.license
%doc Changes README
%dir %{perl_vendorarch}/auto/Statistics
%{perl_vendorarch}/auto/Statistics/CaseResampling
%dir %{perl_vendorarch}/Statistics
%{perl_vendorarch}/Statistics/CaseResampling.pm
%{_mandir}/man3/Statistics::CaseResampling.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
