%global source0_hash b71da7748be3a0ab7c19fe8a3ddf7fec480180342c8e76654d28582281152e07

# Enable PPIx::Regexp optional feature
%bcond_without perl_PPIx_QuoteLike_enables_PPIx_Regexp

Name:           perl-PPIx-QuoteLike
Version:        0.024
Release:        1%{?dist}
Summary:        Parse Perl string literals and string-literal-like things
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPIx-QuoteLike
Source0:        https://cpan.metacpan.org/authors/id/W/WY/WYANT/PPIx-QuoteLike-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Metadata)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(PPI::Document) >= 1.238
BuildRequires:  perl(PPI::Dumper) >= 1.238
BuildRequires:  perl(re)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if %{with perl_PPIx_QuoteLike_enables_PPIx_Regexp}
# Optional run-time:
# Author states there is a build-cycle with PPIx::Regexp, but I cannot see
# any.
BuildRequires:  perl(PPIx::Regexp)
%endif
# Tests:
BuildRequires:  perl(charnames)
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Requires:       perl(PPI::Document) >= 1.238
Requires:       perl(PPI::Dumper) >= 1.238
%if %{with perl_PPIx_QuoteLike_enables_PPIx_Regexp}
Recommends:     perl(PPIx::Regexp)
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((PPI::Document|PPI::Dumper)\\)$

Provides:       perl(PPIx::QuoteLike)
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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE-Artistic LICENSE-GPL
%doc Changes CONTRIBUTING eg/ README SECURITY
%{perl_vendorlib}/PPIx/
%{_mandir}/man3/PPIx::QuoteLike*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
