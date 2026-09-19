%global source0_hash a5f72fd2f22917fa2b4acbb2ee2c3d32903d97ee5b0e449b0f387018c77f4f0c

Name:           perl-Swim
Version:        0.1.48
Release:        19%{?dist}
Summary:        See What I Mean is a plain text markup language
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Swim
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Swim-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(HTML::Escape)
# IPC::Run not used
BuildRequires:  perl(Pegex) >= 0.41
BuildRequires:  perl(Pegex::Base)
BuildRequires:  perl(Pegex::Grammar)
BuildRequires:  perl(Pegex::Parser)
BuildRequires:  perl(Pegex::Tree)
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(YAML::XS)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
BuildRequires:  perl(TestML::Bridge)
BuildRequires:  perl(TestML::Run::TAP)
Requires:       perl(Hash::Merge)
Requires:       perl(IPC::Run)
Requires:       perl(Pegex) >= 0.41
Requires:       perl(Pegex::Grammar)
Requires:       perl(Pegex::Tree)
Requires:       perl(Text::Autoformat)
Requires:       perl(YAML::XS)

%description
Swim (See What I Mean) is a plain text markup language that converts to many
formats: HTML, MarkDown, POD, Formatted Plain Text, LaTeX, DocBook, roff,
AsciiDoc, MediaWiki. The Swim framework is easily extensible, so adding new
outputs is easy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Swim-%{version}
# Remove bundled modules
rm -rf ./inc/lib
perl -i -ne 'print $_ unless m{^inc/lib/}' MANIFEST
# Fix shebang
perl -i -pe 's/^#!.*/#!perl/' bin/swim

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING SWIM_LINK_FORMAT_HACK SWIM_PEGEX_DEBUG SWIM_PEGEX_TREE
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{_bindir}/swim
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
