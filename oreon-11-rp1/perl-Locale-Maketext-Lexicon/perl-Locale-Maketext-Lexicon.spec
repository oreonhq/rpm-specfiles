%global source0_hash b73f6b04a58d3f0e38ebf2115a4c1532f1a4eef6fac5c6a2a449e4e14c1ddc7c

Name:           perl-Locale-Maketext-Lexicon
Version:        1.00
Release:        37%{?dist}
Summary:        Extract translatable strings from source
License:        MIT

URL:            https://metacpan.org/release/Locale-Maketext-Lexicon
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DRTECH/Locale-Maketext-Lexicon-%{version}.tar.gz

Requires:       perl(Encode)
Requires:       perl(File::Glob)
Requires:       perl(File::Spec)
Requires:       perl(FileHandle)
Requires:       perl(HTML::Parser) >= 3.56
Requires:       perl(Lingua::EN::Sentence) >= 0.25
Requires:       perl(Locale::Maketext) >= 1.17
Requires:       perl(PPI) >= 1.203
Requires:       perl(Template) >= 2.20
Requires:       perl(Template::Constants) >= 2.75
Requires:       perl(YAML::Loader) >= 0.66

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  %{__make}
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) > 6.76
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Parser) >= 3.56
# I18N::Langinfo is optional
BuildRequires:  perl(Lingua::EN::Sentence) >= 0.25
BuildRequires:  perl(Locale::Maketext) >= 1.17
BuildRequires:  perl(PPI) >= 1.203
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Template) >= 2.20
BuildRequires:  perl(Template::Constants) >= 2.75
BuildRequires:  perl(Template::Directive)
BuildRequires:  perl(Template::Parser)
BuildRequires:  perl(Text::Haml)
BuildRequires:  perl(YAML::Loader) >= 0.66
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

# Required by the tests
BuildRequires:  /usr/bin/msgunfmt
BuildRequires:  perl(FindBin)
# HTML::Mason is optional
BuildRequires:  perl(lib)
# Mason is optional
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(YAML) >= 0.66

BuildArch: noarch

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((PPI|Template::Constants|YAML::Loader)\\)$

%description
Locale::Maketext::Lexicon provides lexicon-handling backends for
Locale::Maketext to read from other localization formats, such as PO files,
MO files, or from databases via the "Tie" interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Locale-Maketext-Lexicon-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w ${RPM_BUILD_ROOT}/*

%check
%{__make} test

%files
%doc AUTHORS Changes README
%doc docs
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendorlib}/Locale
%{_mandir}/man3/*

%changelog
%autochangelog
