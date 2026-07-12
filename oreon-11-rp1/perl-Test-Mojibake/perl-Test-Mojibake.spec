%global source0_hash 8ffe75ff9b69352488727dca73db91f8aa14b59f2fa104eb7717c0d71a5f1b33

# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

# Similarly, for package note feature
%undefine _package_note_file

Name:		perl-Test-Mojibake
Version:	1.3
Release:	35%{?dist}
Summary:	Check your source for encoding misbehavior
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Mojibake
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Mojibake-%{version}.tar.gz
BuildArch:	noarch
# ===================================================================
# Module build requirements
# ===================================================================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(warnings)
# ===================================================================
# Optional module requirements
# ===================================================================
BuildRequires:	perl(Unicode::CheckUTF8)
# ===================================================================
# Regular test suite requirements
# ===================================================================
BuildRequires:	perl(blib)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::Script)
# ===================================================================
# Author/Release test requirements
#
# Don't run these tests or include their requirements if we're
# bootstrapping, as many of these modules require each other for
# their author/release tests.
# ===================================================================
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(Perl::Critic) >= 1.094
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::CPAN::Changes)
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::CPAN::Meta::JSON)
BuildRequires:	perl(Test::DistManifest)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::HasVersion)
BuildRequires:	perl(Test::MinimumVersion)
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
BuildRequires:	perl(Test::Portability::Files)
BuildRequires:	perl(Test::Synopsis)
%if 0%{?fedora} < 39 && 0%{?rhel} < 10
BuildRequires:	perl(Test::Vars)
%endif
BuildRequires:	perl(Test::Version)
# Modules only available from EL-8
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:	perl(Perl::Critic::Policy::Modules::ProhibitModuleShebang)
BuildRequires:	perl(Test::Kwalitee) >= 1.21
BuildRequires:	perl(Test::Pod::LinkCheck)
%endif
%endif
# ===================================================================
# Dependencies
# ===================================================================
# Unicode::CheckUTF8 is an optional requirement that significantly speeds up
# this module
Requires:	perl(Unicode::CheckUTF8)

Provides:       perl(Test::Mojibake)
%description
Many modern text editors automatically save files using UTF-8 codification.
However, the perl interpreter does not expect it by default. Whilst this does
not represent a big deal on (most) backend-oriented programs, Web framework
(Catalyst, Mojolicious) based applications will suffer so-called Mojibake
(literally: "unintelligible sequence of characters"). Even worse: if an editor
saves BOM (Byte Order Mark, U+FEFF character in Unicode) at the start of a
script with the executable bit set (on Unix systems), it won't execute at all,
due to shebang corruption.

Avoiding codification problems is quite simple:

 * Always use utf8/use common::sense when saving source as UTF-8
 * Always specify =encoding utf8 when saving POD as UTF-8
 * Do neither of above when saving as ISO-8859-1
 * Never save BOM (not that it's wrong; just avoid it as you'll barely
   notice its presence when in trouble)

However, if you find yourself upgrading old code to use UTF-8 or trying to
standardize a big project with many developers, each one using a different
platform/editor, reviewing all files manually can be quite painful, especially
in cases where some files have multiple encodings (note: it all started when I
realized that gedit and derivatives are unable to open files with character
conversion tables).

Enter the Test::Mojibake ;)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Mojibake-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test %{!?perl_bootstrap:AUTHOR_TESTING=1 RELEASE_TESTING=1} \
%if ! 0%{?fedora} && 0%{?rhel} < 8
	TEST_FILES="$(echo $(find t/ -name '*.t' | grep -Fv release-kwalitee.t))"
%endif

%files
%license LICENSE
%doc Changes README
%{_bindir}/scan_mojibake
%{perl_vendorlib}/Test/
%{_mandir}/man1/scan_mojibake.1*
%{_mandir}/man3/Test::Mojibake.3*

%changelog
%autochangelog
