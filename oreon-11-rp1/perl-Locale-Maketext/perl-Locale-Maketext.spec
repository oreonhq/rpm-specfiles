%global source0_hash 9cf49f5cb3db81a2db0459c7ddaa824edc0533ba233dc64b062b8f2f022d55d7
%global base_version 1.32
%bcond_with perl_Locale_Maketext_enables_optional_test
Name:           perl-Locale-Maketext
Version:        1.33
Release:        1%{?dist}
Summary:        Framework for localization
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-Maketext
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/Locale-Maketext-1.32.tar.gz
Patch0:         Locale-Maketext-1.32-Upgrade-to-1.33.patch
BuildArch:      noarch
%if %{with perl_Locale_Maketext_enables_optional_test} && !%{defined perl_bootstrap}
%endif
Requires:       perl(I18N::LangTags) >= 0.31
Requires:       perl(warnings)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(I18N::LangTags\\)$
Provides:       perl(Locale::Maketext::Simple)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(I18N::LangTags)
BuildRequires:  perl(I18N::LangTags::Detect)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(integer)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Locale-Maketext-tests -f %{oreon_filedir}/perl-Locale-Maketext-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.33-522
- Prepare for Oreon 11 (RP1)
