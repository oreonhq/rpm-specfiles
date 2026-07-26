%global source0_hash 3cafffb570b901408e0b4b7a1bfcb52a06bbc71251941b3b6ad265e4029bcf7c

Name:          perl-CSS
Version:       1.09
Release:       37%{?dist}
Summary:       Object oriented access to Cascading Style Sheets (CSS)
License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://metacpan.org/release/CSS
Source0:       https://cpan.metacpan.org/modules/by-module/CSS/CSS-%{version}.tar.gz
Source1:       perl-CSS-build-grammar.pl
BuildArch:     noarch
BuildRequires: coreutils
BuildRequires: dos2unix
BuildRequires: findutils
BuildRequires: glibc-common
BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(Parse::RecDescent)
BuildRequires: perl(Test::Simple)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
This module can be used, along with a CSS::Parse::* module, to parse
CSS data and represent it as a tree of objects. Using a
CSS::Adaptor::* module, the CSS data tree can then be transformed into
other formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n CSS-%{version}
# Regenerate CSS::Parse::CompiledGrammar (#564808, CPAN RT#53948)
%{__perl} %{SOURCE1} 
mv CompiledGrammar.pm CSS/Parse/

mv Changes Changes.iso88591
iconv -f ISO-8859-1 -t UTF-8 -o Changes Changes.iso88591
touch -r Changes.iso88591 Changes
rm -f Changes.iso88591
dos2unix -k examples/{dump,parsers,adapt}.pl Changes README t/css_simple

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
install -D -p -m 0644 t/css_simple examples/t/css_simple
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/CSS.pm
%{perl_vendorlib}/CSS
%{_mandir}/man3/CSS.*
%{_mandir}/man3/CSS::*

%changelog
%autochangelog
