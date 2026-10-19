%global source0_hash e9c669c01d7c951f9bfee899c147fc8c8ddd98d3f32329f94000c7b02f53366b
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with perl_PPIx_Regexp_enables_optional_test
Name:           perl-PPIx-Regexp
Version:        0.092
Release:        1%{?dist}
Summary:        Represent a regular expression of some sort
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPIx-Regexp
Source0:        https://cpan.metacpan.org/authors/id/W/WY/WYANT/PPIx-Regexp-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_PPIx_Regexp_enables_optional_test}
%endif
Recommends:     perl(Encode)
Requires:       perl(PPI::Document) >= 1.238
Requires:       perl(PPI::Dumper) >= 1.238
Requires:       perl(Task::Weaken)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(PPI::Document\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(My::Module::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(My::Module::
Provides:       perl(PPIx::Regexp)
Provides:       perl(PPIx::Regexp::Util)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(charnames)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The purpose of the PPIx-Regexp package is to parse regular expressions in a
manner similar to the way the PPI package parses Perl. This class forms the
root of the parse tree, playing a role similar to PPI::Document.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(open)
Requires:       perl(PPI::Document) >= 1.238
%if %{with perl_PPIx_Regexp_enables_optional_test}
Requires:       perl(Time::HiRes)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n PPIx-Regexp-%{version}
chmod -x eg/*
perl -MConfig -i -p \
    -e 's{^#!/usr/(?:local/bin/|bin/env )perl\b}{$Config{startperl}}' \
    eg/*
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

unset MAKING_MODULE_DISTRIBUTION
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/inc/My/Module
cp -a inc/My/Module/{Mock_Tokenizer,Test}.pm %{buildroot}%{_libexecdir}/%{name}/inc/My/Module
mkdir -p %{buildroot}%{_libexecdir}/%{name}/eg
cp -a eg/predump %{buildroot}%{_libexecdir}/%{name}/eg
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING PPIX_REGEXP_TOKENIZER_TRACE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING PPIX_REGEXP_TOKENIZER_TRACE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-PPIx-Regexp-tests -f %{oreon_filedir}/perl-PPIx-Regexp-tests.list

%changelog

%autochangelog
