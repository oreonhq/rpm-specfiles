Name:           perl-DateTime-Locale
Version:        1.45
Release:        3%{?dist}
Summary:        Localization support for DateTime.pm
# Although the CLDR license is listed as "MIT" on the Fedora Wiki, it's more
# similar to recently added "Unicode-DFS-2015" license.
# some modules under DateTime/Locale:   Unicode (generated from data
#                                       provided by the CLDR project)
# LICENSE.cldr:         Unicode
# other files:          GPL-1.0-or-later OR Artistic-1.0-Perl
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND Unicode-DFS-2015
URL:            https://metacpan.org/release/DateTime-Locale
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Locale-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
# Dist::CheckConflicts 0.02 is optionaly used from Makefile.PL, but it has no
# meaning in minimal build root without useless Perl modules.
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(namespace::autoclean) >= 0.19
BuildRequires:  perl(Params::ValidationCompiler) >= 0.13
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::String)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::File::ShareDir::Dist)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test2::Plugin::UTF8)
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(utf8)
# Optional tests:
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Storable)
Requires:       perl(Dist::CheckConflicts) >= 0.02
# perl-DateTime-Locale used to be bundled with perl-DateTime
# ideally, this would be resolved with
# Requires:     perl-DateTime >= 2:0.70-1
# but DateTime::Locale doesn't strictly require DateTime
# and this would introduce circular build dependencies
Conflicts:      perl-DateTime <= 1:0.7000-3.fc16

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Dist::CheckConflicts\\)$

%description
DateTime::Locale is primarily a factory for the various locale sub-classes.
It also provides some functions for getting information on all the
available locales.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n DateTime-Locale-%{version}

# Help file to recognise the Perl scripts
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE LICENSE.cldr
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/DateTime*
%{perl_vendorlib}/auto/*
%{_mandir}/man3/DateTime::Locale*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.45-3
- Prepare for Oreon 11 (RP1)
