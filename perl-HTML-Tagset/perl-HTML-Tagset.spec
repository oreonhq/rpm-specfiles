%if ! (0%{?rhel})
%{bcond_without perl_HTML_Tagset_enables_optional_test}
%else
%{bcond_with perl_HTML_Tagset_enables_optional_test}
%endif

Name:           perl-HTML-Tagset
Version:        3.24
Release:        5%{?dist}
Summary:        HTML::Tagset - data tables useful in parsing HTML
License:        Artistic-2.0
URL:            https://metacpan.org/release/HTML-Tagset
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/HTML-Tagset-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Optional tests
# Test::Pod -> Pod::Simple -> HTML::Entities (HTML::Parser) -> HTML::Tagset
%if 0%{!?perl_bootstrap:1}
%if %{with perl_HTML_Tagset_enables_optional_test}
BuildRequires:  perl(Test::Pod) >= 1.14
%endif
%endif

%description
This module contains several data tables useful in various kinds of
HTML parsing operations, such as tag and entity names.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n HTML-Tagset-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/HTML/
%{_mandir}/man3/HTML::Tagset.3pm*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.24-5
- Prepare for Oreon 11 (RP1)
