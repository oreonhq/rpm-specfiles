%global source0_hash 2ba9ea76c049daf892ba2bdd85a07099a33be315876f55ed33a644d575324432
Name:           perl-Pod-Spell-CommonMistakes
Version:        1.002
Release:        1%{?dist}
Summary:        Catches common typos in POD
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Spell-CommonMistakes
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/Pod-Spell-CommonMistakes-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Pod::Spell::CommonMistakes)
Provides:       perl(Pod::Spell::CommonMistakes)
# oreon:deps
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Pod::Spell)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module looks for any typos in your POD. It differs from Pod::Spell or
Test::Spelling because it uses a custom word list and doesn't use the system
spellchecker. The idea for this came from the
<http://wiki.debian.org/Teams/Lintian> code in Debian, thanks!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Spell-CommonMistakes-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install "--destdir=$RPM_BUILD_ROOT" --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
