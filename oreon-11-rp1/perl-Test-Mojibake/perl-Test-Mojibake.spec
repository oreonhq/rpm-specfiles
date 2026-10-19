%global source0_hash 8ffe75ff9b69352488727dca73db91f8aa14b59f2fa104eb7717c0d71a5f1b33
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%global debug_package %{nil}
%undefine _package_note_file
Name:		perl-Test-Mojibake
Version:	1.3
Release:        35%{?dist}
Summary:        Check your source for encoding misbehavior
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Mojibake
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Mojibake-%{version}.tar.gz
BuildArch:	noarch
%if 0%{!?perl_bootstrap:1}
%if 0%{?fedora} < 39 && 0%{?rhel} < 10 && 0%{?oreon} < 11
%endif
%endif
Requires:	perl(Unicode::CheckUTF8)
Provides:       perl(Test::Mojibake)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::DistManifest)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::HasVersion)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(Test::Synopsis)
BuildRequires:  perl(Test::Version)
BuildRequires:  perl(Unicode::CheckUTF8)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test %{!?perl_bootstrap:AUTHOR_TESTING=1 RELEASE_TESTING=1} \
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
