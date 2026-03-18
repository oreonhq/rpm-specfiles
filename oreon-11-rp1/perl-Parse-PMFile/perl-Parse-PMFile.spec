# Run optional test
%bcond_without perl_Parse_PMFile_enables_optional_test

Name:           perl-Parse-PMFile
Version:        0.47
Release:        5%{?dist}
Summary:        Parses .pm file as PAUSE does
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parse-PMFile
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Parse-PMFile-%{version}.tar.gz
# Remove useless dependency on ExtUtils::MakeMaker::CPANfile
Patch0:         Parse-PMFile-0.41-Do-not-use-ExtUtils-MakeMaker-CPANfile.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Dumpvalue)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP) >= 2.00
BuildRequires:  perl(Safe)
BuildRequires:  perl(version) >= 0.83
# Tests
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Opcode)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_Parse_PMFile_enables_optional_test}
# Optional tests
# PAUSE::Permissions 0.08 not yet packaged
BuildRequires:  perl(version::vpp)
# Test::Pod not used
# Test::Pod::Coverage not used
%endif
Requires:       perl(JSON::PP) >= 2.00
Requires:       perl(version) >= 0.83

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((JSON::PP|version)\\)$

%description
The most of the code of this module is taken from the PAUSE code as of
April 2013 almost verbatim. Thus, the heart of this module should be quite
stable. However, I made it not to use pipe ("-|") as well as I stripped
database-related code. If you encounter any issue, that's most probably
because of my modification.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Parse-PMFile-%{version}
%patch -P0 -p1
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/99_pod*
for F in 10_self_check.t 80_version_overload.t 81_version_overload_with_explicit_vpp.t; do
    perl -i -pe 's{\$FindBin::Bin/../lib/}{%{perl_vendorlib}/}' %{buildroot}%{_libexecdir}/%{name}/t/$F
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset TEST_POD
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%{perl_vendorlib}/Parse*
%{_mandir}/man3/Parse::PMFile*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.47-5
- Prepare for Oreon 11 (RP1)
