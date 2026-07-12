%global source0_hash ecd42cc2927d2ed89e80d7571e34ba443765140e51215d659583a8da49d319f0

# Perform optional tests
%bcond_without perl_Syntax_Keyword_Junction_enables_optional_test

Name:           perl-Syntax-Keyword-Junction
Version:        0.003009
Release:        4%{?dist}
Summary:        Perl6 style Junction operators in Perl5
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Keyword-Junction
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Syntax-Keyword-Junction-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(if)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001006
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs) >= 0.002006
%if %{with perl_Syntax_Keyword_Junction_enables_optional_test}
# Optional tests:
# CPAN::Meta not helpful
BuildRequires:  perl(Sub::Exporter) >= 0.986
BuildRequires:  perl(syntax)
%endif
Requires:       perl(if)
Requires:       perl(overload)
Requires:       perl(Sub::Exporter::Progressive) >= 0.001006

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Sub::Exporter::Progressive|Test::More|Test::Needs)\\)$

Provides:       perl(Syntax::Keyword::Junction)
Provides:       perl(Syntax::Keyword::Junction::All)
Provides:       perl(Syntax::Keyword::Junction::Any)
Provides:       perl(Syntax::Keyword::Junction::None)
Provides:       perl(Syntax::Keyword::Junction::One)
Provides:       perl(Syntax::Keyword::Junction::All)
Provides:       perl(Syntax::Keyword::Junction::Any)
Provides:       perl(Syntax::Keyword::Junction::None)
Provides:       perl(Syntax::Keyword::Junction::One)
%description
This is a lightweight module which provides 'Junction' operators, the most
commonly used being any and all. Inspired by the Perl6 design docs,
<http://dev.perl.org/perl6/doc/design/exe/E06.html>.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(blib)
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Test::Needs) >= 0.002006
%if %{with perl_Syntax_Keyword_Junction_enables_optional_test}
Requires:       perl(if)
Requires:       perl(Sub::Exporter) >= 0.986
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Syntax-Keyword-Junction-%{version}
for F in \
%if %{without perl_Syntax_Keyword_Junction_enables_optional_test}
    t/smartmatch.t t/syntax.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\E'"$F"'\Q}' MANIFEST
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
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Syntax
%dir %{perl_vendorlib}/Syntax/Feature
%{perl_vendorlib}/Syntax/Feature/Junction.pm
%dir %{perl_vendorlib}/Syntax/Keyword
%{perl_vendorlib}/Syntax/Keyword/Junction
%{perl_vendorlib}/Syntax/Keyword/Junction.pm
%{_mandir}/man3/Syntax::Feature::Junction.*
%{_mandir}/man3/Syntax::Keyword::Junction.*
%{_mandir}/man3/Syntax::Keyword::Junction::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
