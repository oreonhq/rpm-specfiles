%global source0_hash b71da7748be3a0ab7c19fe8a3ddf7fec480180342c8e76654d28582281152e07
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without perl_PPIx_QuoteLike_enables_PPIx_Regexp
Name:           perl-PPIx-QuoteLike
Version:        0.024
Release:        1%{?dist}
Summary:        Parse Perl string literals and string-literal-like things
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPIx-QuoteLike
Source0:        https://cpan.metacpan.org/authors/id/W/WY/WYANT/PPIx-QuoteLike-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_PPIx_QuoteLike_enables_PPIx_Regexp}
%endif
Requires:       perl(PPI::Document) >= 1.238
Requires:       perl(PPI::Dumper) >= 1.238
%if %{with perl_PPIx_QuoteLike_enables_PPIx_Regexp}
Recommends:     perl(PPIx::Regexp)
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((PPI::Document|PPI::Dumper)\\)$
Provides:       perl(PPIx::QuoteLike)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(PPIx::Regexp)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(charnames)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl class parses Perl string literals and things that are reasonably
like string literals. Its real reason for being is to find interpolated
variables for Perl::Critic policies and similar code.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(open)
Requires:       perl(PPI::Document) >= 1.238
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n PPIx-QuoteLike-%{version}
# Fix shell bang and permissions
for F in eg/{pqldump,variables}; do
    perl -MConfig -p -i -e 's{\A#!/usr/bin/env perl\b}{$Config{startperl}}' \
        "$F"
    chmod -x "$F"
done
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
%{_fixperms} -c %{buildroot}
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
%files -n perl-PPIx-QuoteLike-tests -f %{oreon_filedir}/perl-PPIx-QuoteLike-tests.list

%changelog

%autochangelog
