%global source0_hash 37133eeb09d36da6d461546cc216b8f6a2297a43331c680a6848f3fff925975c
Name:           perl-Date-Manip
Version:        7.00
Release:        1%{?dist}
Summary:        Date manipulation routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-Manip
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBECK/Date-Manip-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Cwd)
Requires:       perl(File::Find)
Requires:       perl(File::Spec)
Provides: perl-DateManip = %{version}-%{release}
Obsoletes: perl-DateManip < 5.48-1
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(tests.pl\\)
Provides:       perl(Date::Manip)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Inter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/_pod*
rm -f %{buildroot}%{_libexecdir}/%{name}/t/_version.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset DATE_MANIP DATE_MANIP_DEBUG DATE_MANIP_DEBUG_ABBREVS \
    DATE_MANIP_DEBUG_ZONES Date_Manip_RELEASE_TESTING DATE_MANIP_TEST_DM5 \
    OS MULTINET_TIMEZONE 'SYS$TIMEZONE_DIFFERENTIAL' 'SYS$TIMEZONE_NAME' \
    'SYS$TIMEZONE_RULE' 'TCPIP$TZ' 'UCX$TZ'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset DATE_MANIP DATE_MANIP_DEBUG DATE_MANIP_DEBUG_ABBREVS \
    DATE_MANIP_DEBUG_ZONES Date_Manip_RELEASE_TESTING DATE_MANIP_TEST_DM5 \
    OS MULTINET_TIMEZONE 'SYS$TIMEZONE_DIFFERENTIAL' 'SYS$TIMEZONE_NAME' \
    'SYS$TIMEZONE_RULE' 'TCPIP$TZ' 'UCX$TZ'
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Date-Manip-tests -f %{oreon_filedir}/perl-Date-Manip-tests.list

%changelog

%autochangelog
