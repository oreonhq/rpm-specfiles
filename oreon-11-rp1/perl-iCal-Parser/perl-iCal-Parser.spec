%global source0_hash 0d7939a644a8e67017ec7239d3d9604f3986bb9a4ff80be68fe7299ebfd2270c

Name:           perl-iCal-Parser
Version:        1.21
Release:        29%{?dist}
Summary:        Parse iCalendar files into a data structure
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/iCal-Parser
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIXED/iCal-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(DateTime::Format::ICal) >= 0.08
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::File) >= 1.1
BuildRequires:  perl(IO::String)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::vFile::asData) >= 0.02
# Tests:
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Span)
BuildRequires:  perl(FreezeThaw) >= 0.43
BuildRequires:  perl(Test::More) >= 0.54
Requires:       perl(DateTime::Format::ICal) >= 0.08
Requires:       perl(Text::vFile::asData) >= 0.02

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DateTime::Format::ICal|FreezeThaw|Test::More|Text::vFile::asData)\\)$
# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(t::Defrost\\)

%description
This Perl module processes iCalendar (vCalendar 2.0) files as specified in
RFC 2445 into a data structure. It handles recurrences (RRULEs), exclusions
(EXDATEs), event updates (events with a RECURRENCE-ID), and nested data
structures (ATTENDEES and VALARMs). It currently ignores the VTIMEZONE,
VJOURNAL and VFREEBUSY entry types.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(FreezeThaw) >= 0.43
Requires:       perl(Test::More) >= 0.54

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n iCal-Parser-%{version}
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
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc ChangeLog README
%dir %{perl_vendorlib}/iCal
%{perl_vendorlib}/iCal/Parser.pm
%{_mandir}/man3/iCal::Parser.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
