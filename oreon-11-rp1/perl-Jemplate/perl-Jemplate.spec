%global source0_hash c55822eb586ae97da54c2b9ff924acd854e69b200cc728185c4e4a25492a8249

%global cpan_version 0.30

Name:       perl-Jemplate 
# Keep 3-digit version for history
Version:    %{cpan_version}0
Release:    31%{?dist}
# lib/Jemplate.pm -> GPL+ or Artistic
# lib/Jemplate/Directive.pm -> GPL+ or Artistic
# lib/Jemplate/Parser.pm -> GPL+ or Artistic
# lib/Jemplate/Runtime.pm -> GPL+ or Artistic
# lib/Jemplate/Runtime/Compact.pm -> GPL+ or Artistic
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    JavaScript Templating with Template Toolkit 
Source:     https://cpan.metacpan.org/authors/id/I/IN/INGY/Jemplate-%{cpan_version}.tar.gz 
# Do not prune INC, CPAN RT#87546
Patch0:     Jemplate-0.27-Do-not-prune-INC.patch
Url:        https://metacpan.org/release/Jemplate
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires: perl(strict)
# Run-time:
BuildRequires: perl(base)
BuildRequires: perl(bytes)
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(constant)
BuildRequires: perl(Encode)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
# File::Find::Rule is bundled
BuildRequires: perl(File::Find::Rule) >= 0.33
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
# Number::Compare is bundled
BuildRequires: perl(overload)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Template) >= 2.25
# Template is bundled
# Template::Base is bundled
# Template::Config is bundled
# Template::Constants is bundled
# Template::Directive is bundled
# Template::Document is bundled
# Template::Exception is bundled
# Template::Grammar is bundled
# Template::Parser is bundled
# Template::Provider is bundled
# Template::Service is bundled
# Template::TieString is bundled
# Text::Glob is bundled
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
# Tests
BuildRequires: perl(HTTP::Daemon)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(IO::All)
BuildRequires: perl(JSON)
BuildRequires: perl(lib)
BuildRequires: perl(LWP::MediaTypes)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Test::Base)
BuildRequires: perl(Test::Base::Filter)
BuildRequires: perl(Test::More)
BuildRequires: perl(YAML)
# Optional tests
#BuildRequires: perl(JavaScript::V8x::TestMoreish)

Requires:   perl(File::Find::Rule) >= 0.33

%description
Jemplate is a templating framework for JavaScript that is built over
Perl's Template Toolkit (TT2). Jemplate parses TT2 templates using the
TT2 Perl framework, but with a twist. Instead of compiling the templates
into Perl code, it compiles them into JavaScript. Jemplate then provides
a JavaScript run-time module for processing the template code. Presto, we
have full featured JavaScript templating language!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Jemplate-%{cpan_version}
%patch -P0 -p1
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST

cat doc/text/Jemplate.text | iconv -f iso-8859-1 -t utf-8 > foo
cat foo > doc/text/Jemplate.text
rm foo

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes LICENSE README doc/ examples/ 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*
%{_bindir}/jemplate
%{_mandir}/man1/jemplate.1.gz

%changelog
%autochangelog
