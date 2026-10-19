%global source0_hash c55822eb586ae97da54c2b9ff924acd854e69b200cc728185c4e4a25492a8249
%global cpan_version 0.30
Name:       perl-Jemplate 
Version:    %{cpan_version}0
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        JavaScript Templating with Template Toolkit
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Jemplate-%{cpan_version}.tar.gz
Patch0:     Jemplate-0.27-Do-not-prune-INC.patch
Url:        https://metacpan.org/release/Jemplate
BuildArch:  noarch
Requires:   perl(File::Find::Rule) >= 0.33
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::MediaTypes)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::Base::Filter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
