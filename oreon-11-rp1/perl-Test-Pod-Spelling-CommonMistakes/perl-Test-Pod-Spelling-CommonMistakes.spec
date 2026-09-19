%global source0_hash 1fdcd2cc6b86edfaf0486b3a107653a3163fcbf2d1924456f648ee323ee99f39

Name:           perl-Test-Pod-Spelling-CommonMistakes
Version:        1.001
Release:        33%{?dist}
Summary:        Checks POD for common spelling mistakes
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Pod-Spelling-CommonMistakes
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/Test-Pod-Spelling-CommonMistakes-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Spell::CommonMistakes) >= 0.01
BuildRequires:  perl(Test::Builder) >= 0.94
BuildRequires:  perl(Test::Pod) >= 1.40
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88

%description
This module checks your POD for common spelling errors. This differs from
Test::Spelling because it doesn't use your system spellchecker and instead
uses Pod::Spell::CommonMistakes for the heavy lifting. Using it is the same
as any standard Test::* module, as seen here.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Pod-Spelling-CommonMistakes-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install "--destdir=$RPM_BUILD_ROOT" --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes CommitLog examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
