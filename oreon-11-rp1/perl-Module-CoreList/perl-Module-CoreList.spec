Name:           perl-Module-CoreList
# Epoch to compete with perl.spec
Epoch:          1
Version:        5.20260308
Release:        1%{?dist}
Summary:        What modules are shipped with versions of perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-CoreList
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Module-CoreList-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 df85be58cdf25dfe375820a9b3038972d75a12af75dc478003bd1442d5fac88a
%global source0_file Module-CoreList-5.20260308.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# File::Copy not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# feature not used at tests
# Getopt::Long not used at tests
BuildRequires:  perl(List::Util)
# Pod::Usage not used at tests
BuildRequires:  perl(version) >= 0.88
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(List::Util)
Requires:       perl(version) >= 0.88

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(version\\)$

%description
Module::CoreList provides information on which core and dual-life modules
are shipped with each version of perl.

%package tools
Summary:        Tool for listing modules shipped with perl
Requires:       perl(feature)
Requires:       perl(version) >= 0.88
Requires:       perl-Module-CoreList = %{epoch}:%{version}-%{release}
# The files were distributed with perl.spec's subpackage
# perl-Module-CoreList <= 1:5.020001-309
Conflicts:      perl-Module-CoreList < 1:5.20140914

%description tools
This package provides a corelist(1) tool which can be used to query what
modules were shipped with given perl version.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-tools = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Module-CoreList-5.20260308.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "df85be58cdf25dfe375820a9b3038972d75a12af75dc478003bd1442d5fac88a" || { echo "oreon: Source0 SHA256 mismatch for Module-CoreList-5.20260308.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Module-CoreList-%{version}

# Help file to recognise the Perl scripts and normalize shebangs
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
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
rm -f %{buildroot}/%{_libexecdir}/%{name}/t/pod.t
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset PERL_CORE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
unset PERL_CORE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%{perl_vendorlib}/Module
%{_mandir}/man3/Module::CoreList*

%files tools
%doc README
%{_bindir}/corelist
%{_mandir}/man1/corelist.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.20260308-1
- Prepare for Oreon 11 (RP1)
