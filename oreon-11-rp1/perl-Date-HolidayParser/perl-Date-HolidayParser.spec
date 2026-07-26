%global source0_hash d61f6850e669e41d221e598fd09d9ec2f29a8138d9679609f02a31bb817e0a6b

Name:           perl-Date-HolidayParser
Version:        0.43
Release:        16%{?dist}
Summary:        Parser for .holiday-files
# COPYING:      GPL-3.0-or-later OR Artistic-1.0-Perl
# COPYING.artistic:     Artistic-1.0-Perl text
# COPYING.gpl:          GPL-3.0 text
# lib/Date/HolidayParser.pm:            GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Date/HolidayParser/iCalendar.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# Makefile.PL:                          GPL-1.0-or-later OR Artistic-1.0-Perl
# README:                               GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-3.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/Date-HolidayParser
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZERODOGG/Date-HolidayParser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Moo)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(POSIX)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This is a module that parses .holiday-style files. These are files that
define holidays in various parts of the world. The files are easy to write
and easy for humans to read, but can be hard to parse because the format
allows many different ways to write it.

%package tests
Summary:        Tests for %{name}
License:        GPL-3.0-or-later
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn Date-HolidayParser-%{version}

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
%license COPYING*
%doc Changes README
%dir %{perl_vendorlib}/Date
%{perl_vendorlib}/Date/HolidayParser
%{perl_vendorlib}/Date/HolidayParser.pm
%{_mandir}/man3/Date::HolidayParser.*
%{_mandir}/man3/Date::HolidayParser::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
