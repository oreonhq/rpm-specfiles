%global base_version 1.32

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Locale_Maketext_enables_optional_test
%else
%bcond_with perl_Locale_Maketext_enables_optional_test
%endif

Name:           perl-Locale-Maketext
Version:        1.33
Release:        522%{?dist}
Summary:        Framework for localization
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-Maketext
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/Locale-Maketext-%{base_version}.tar.gz
# Unbundled from perl 5.37.11
Patch0:         Locale-Maketext-1.32-Upgrade-to-1.33.patch
# oreon url source checksums begin
%global source0_sha256 9cf49f5cb3db81a2db0459c7ddaa824edc0533ba233dc64b062b8f2f022d55d7
%global source0_file Locale-Maketext-1.32.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(I18N::LangTags) >= 0.31
BuildRequires:  perl(I18N::LangTags::Detect)
BuildRequires:  perl(integer)
# utf8 is used only if it has already been loaded
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Optional tests:
%if %{with perl_Locale_Maketext_enables_optional_test} && !%{defined perl_bootstrap}
BuildRequires:  perl(Test::Pod) >= 1.14
%endif
Requires:       perl(I18N::LangTags) >= 0.31
# utf8 is used only if it has already been loaded
Requires:       perl(warnings)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(I18N::LangTags\\)$

%description
It is a common feature of applications (whether run directly, or via the Web)
for them to be "localized" -- i.e., for them to present an English interface
to an English-speaker, a German interface to a German-speaker, and so on for
all languages it's programmed with. Locale::Maketext is a framework for
software localization; it provides you with the tools for organizing and
accessing the bits of text and text-processing code that you need for
producing localized applications.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Locale-Maketext-1.32.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9cf49f5cb3db81a2db0459c7ddaa824edc0533ba233dc64b062b8f2f022d55d7" || { echo "oreon: Source0 SHA256 mismatch for Locale-Maketext-1.32.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Locale-Maketext-%{base_version}
%patch -P0 -p1
perl -i -ne 'print $_ unless m{^t/00_load.t}' MANIFEST
perl -i -ne 'print $_ unless m{^t/pod.t}' MANIFEST

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
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.33-522
- Prepare for Oreon 11 (RP1)
