# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash eb89e145a608ed1f8f141a57472ee5f69e67592a432dcd2e8b1dbb445f2b230b
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if ! (0%{?rhel} || 0%{?oreon})
%{bcond_without perl_HTML_Tagset_enables_optional_test}
%else
%{bcond_with perl_HTML_Tagset_enables_optional_test}
%endif

Name:           perl-HTML-Tagset
Version:        3.24
Release:        1%{?dist}
Summary:        HTML::Tagset - data tables useful in parsing HTML
License:        Artistic-2.0
URL:            https://metacpan.org/release/HTML-Tagset
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/HTML-Tagset-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
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
%oreon_sha256
%setup -q -n HTML-Tagset-%{version}

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

mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
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
%autochangelog
