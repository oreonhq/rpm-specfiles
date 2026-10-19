%global source0_hash 655fcf261206c1adbc3038981790b116c31508485135c648093b99b3b3de09d2
Name:           perl-Pod-Weaver
Version:        4.020
Release:        1%{?dist}
Summary:        Weave together a POD document from an outline
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Weaver
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Pod-Weaver-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Config::MVP::Assembler)
Requires:       perl(Config::MVP::Assembler::WithBundles)
Requires:       perl(Config::MVP::Reader::Finder)
Requires:       perl(Config::MVP::Reader::INI)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::MVP)
BuildRequires:  perl(Config::MVP::Assembler)
BuildRequires:  perl(Config::MVP::Assembler::WithBundles)
BuildRequires:  perl(Config::MVP::Reader::Finder)
BuildRequires:  perl(Config::MVP::Reader::INI)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Dispatchouli)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Pod::Elemental)
BuildRequires:  perl(Pod::Elemental::Document)
BuildRequires:  perl(Pod::Elemental::Element::Nested)
BuildRequires:  perl(Pod::Elemental::Element::Pod5::Command)
BuildRequires:  perl(Pod::Elemental::Element::Pod5::Ordinary)
BuildRequires:  perl(Pod::Elemental::Element::Pod5::Region)
BuildRequires:  perl(Pod::Elemental::Element::Pod5::Verbatim)
BuildRequires:  perl(Pod::Elemental::Selectors)
BuildRequires:  perl(Pod::Elemental::Transformer::Gatherer)
BuildRequires:  perl(Pod::Elemental::Transformer::Nester)
BuildRequires:  perl(Pod::Elemental::Transformer::Pod5)
BuildRequires:  perl(Pod::Elemental::Types)
BuildRequires:  perl(Software::License::Artistic_1_0)
BuildRequires:  perl(Software::License::Perl_5)
BuildRequires:  perl(String::Flogger)
BuildRequires:  perl(String::Formatter)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Pod::Weaver is a system for building POD documents from templates.
It doesn't perform simple text substitution, but instead builds
a Pod::Elemental::Document. Its plugins sketch out a series of sections
that will be produced based on an existing POD document or other
provided information.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Weaver-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
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
%files -n perl-Pod-Weaver-tests -f %{oreon_filedir}/perl-Pod-Weaver-tests.list

%changelog

%autochangelog
