%global source0_hash 77b248d4cf7fecaa7e865930e72df0b9d5b333358d00c5bd45e2c71d5df113ad

Name:           perl-Log-Report-Optional
Version:        1.08
Release:        2%{?dist}
Summary:        Base class for large Log::Report and simple Log::Report::Minimal
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Report-Optional
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Log-Report-Optional-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Print) >= 0.91
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More) >= 0.86
Requires:       perl(String::Print) >= 0.91
# This package is a sprout of perl-Log-Report. It replaces parts of
# perl-Log-Report-0.998 and it's required by perl-Log-Report >= 1.01.
Conflicts:      perl-Log-Report < 0.999

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((String::Print|Test::More)\\)$

%description
This module will allow libraries (helper modules) to have a dependency to a
small module instead of the full Log-Report distribution. The full power of
Log::Report is only released when the main program uses that module. In
that case, the module using the 'Optional' will also use the full
Log::Report, otherwise the dressed-down Log::Report::Minimal version.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.86

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Report-Optional-%{version}
# Correct shebangs
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
%doc ChangeLog README.md
%dir %{perl_vendorlib}/Log
%dir %{perl_vendorlib}/Log/Report
%{perl_vendorlib}/Log/Report/Minimal
%{perl_vendorlib}/Log/Report/Minimal.{pm,pod}
%{perl_vendorlib}/Log/Report/Optional.{pm,pod}
%{perl_vendorlib}/Log/Report/Util.{pm,pod}
%{_mandir}/man3/Log::Report::Minimal.*
%{_mandir}/man3/Log::Report::Minimal::*
%{_mandir}/man3/Log::Report::Optional.*
%{_mandir}/man3/Log::Report::Util.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
