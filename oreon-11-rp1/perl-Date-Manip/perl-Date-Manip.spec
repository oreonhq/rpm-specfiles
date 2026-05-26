Name:           perl-Date-Manip
Version:        6.99
Release:        1%{?dist}
Summary:        Date manipulation routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-Manip
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBECK/Date-Manip-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 3239e5f671e1af74d4a91b8278f3ae64f214184f7fc27ed4f80409ec2e6c4f54
%global source0_file Date-Manip-6.99.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Carp)
# Cwd not used at tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
# File::Find not used at tests
# File::Spec not used at tests
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Storable)
BuildRequires:  perl(utf8)
# Win32::TieRegistry not used
# Tests only
# File::Basename not used
# File::Find::Rule not used
# lib not used
BuildRequires:  perl(Test::Inter) >= 1.09
BuildRequires:  perl(Test::More)
# Test::Pod 1.00 not used
# Test::Pod::Coverage 1.00 not used
Requires:       perl(Cwd)
Requires:       perl(File::Find)
Requires:       perl(File::Spec)

# This package was formerly known as perl-DateManip
Provides: perl-DateManip = %{version}-%{release}
Obsoletes: perl-DateManip < 5.48-1

%{?perl_default_filter}

# Filter modules bundled for tests
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(tests.pl\\)

%description
Date::Manip is a series of modules designed to make any common date/time
operation easy to do. Operations such as comparing two times, determining
a data a given amount of time from another, or parsing international times
are all easily done. It deals with time as it is used in the Gregorian
calendar (the one currently in use) with full support for time changes due
to daylight saving time.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Date-Manip-6.99.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3239e5f671e1af74d4a91b8278f3ae64f214184f7fc27ed4f80409ec2e6c4f54" || { echo "oreon: Source0 SHA256 mismatch for Date-Manip-6.99.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Date-Manip-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t t/*.pl; do
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
# Remove release tests
rm -f %{buildroot}%{_libexecdir}/%{name}/t/_pod*
rm -f %{buildroot}%{_libexecdir}/%{name}/t/_version.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset DATE_MANIP DATE_MANIP_DEBUG DATE_MANIP_DEBUG_ABBREVS \
    DATE_MANIP_DEBUG_ZONES Date_Manip_RELEASE_TESTING DATE_MANIP_TEST_DM5 \
    OS MULTINET_TIMEZONE 'SYS$TIMEZONE_DIFFERENTIAL' 'SYS$TIMEZONE_NAME' \
    'SYS$TIMEZONE_RULE' 'TCPIP$TZ' 'UCX$TZ'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset DATE_MANIP DATE_MANIP_DEBUG DATE_MANIP_DEBUG_ABBREVS \
    DATE_MANIP_DEBUG_ZONES Date_Manip_RELEASE_TESTING DATE_MANIP_TEST_DM5 \
    OS MULTINET_TIMEZONE 'SYS$TIMEZONE_DIFFERENTIAL' 'SYS$TIMEZONE_NAME' \
    'SYS$TIMEZONE_RULE' 'TCPIP$TZ' 'UCX$TZ'
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc README README.first
%dir %{perl_vendorlib}/Date
%{perl_vendorlib}/Date/Manip
%{perl_vendorlib}/Date/Manip.{pm,pod}
%{_mandir}/man1/dm_*.1*
%{_mandir}/man3/Date::Manip.3*
%{_mandir}/man3/Date::Manip::*.3*
%{_bindir}/dm_*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.99-1
- Prepare for Oreon 11 (RP1)
