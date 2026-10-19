%global source0_hash 9c428f2fb55dac4ec511f69e37ceb5f367034e475b079f59cf6abb82114f5ca3
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without perl_Syntax_Keyword_Match_enables_optional_test
Name:           perl-Syntax-Keyword-Match
Version:        0.15
Release:        1%{?dist}
Summary:        Match/case syntax for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Keyword-Match
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Keyword-Match-%{version}.tar.gz
%define xs_parse_infix_minver 0
%define xs_parse_keyword_minver 0.36
%if %{with perl_Syntax_Keyword_Match_enables_optional_test}
%endif
Requires:       perl(XS::Parse::Infix) >= %{xs_parse_infix_minver}
%if %{defined perl_XS_Parse_Infix_ABI}
Requires:       %{perl_XS_Parse_Infix_ABI}
%endif
Requires:       perl(XS::Parse::Keyword) >= %{xs_parse_keyword_minver}
%if %{defined perl_XS_Parse_Keyword_ABI}
Requires:       %{perl_XS_Parse_Keyword_ABI}
%endif
Provides:       perl(Syntax::Keyword::Match)
Provides:       perl(Syntax::Keyword::Match)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::AsyncAwait)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Syntax::Operator::Divides)
BuildRequires:  perl(Syntax::Operator::Eqr)
BuildRequires:  perl(Syntax::Operator::Equ)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XS::Parse::Infix)
BuildRequires:  perl(XS::Parse::Infix::Builder)
BuildRequires:  perl(XS::Parse::Keyword)
BuildRequires:  perl(XS::Parse::Keyword::Builder)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a syntax plugin that implements a control-flow block
called match/case, which executes at most one of a choice of different
blocks depending on the value of its controlling expression.

%package Deparse
Summary:        B::Deparse support for Syntax::Keyword::Match
BuildArch:      noarch
%description Deparse
Loading this module will apply some hacks onto B::Deparse that attempts to
provide deparse support for code which uses the syntax provided by
Syntax::Keyword::Match.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Deparse = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Syntax_Keyword_Match_enables_optional_test}
Requires:       perl(Future)
Requires:       perl(Future::AsyncAwait) >= 0.10
Requires:       perl(Syntax::Operator::Divides)
Requires:       perl(Syntax::Operator::Eqr)
Requires:       perl(Syntax::Operator::Equ)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Syntax-Keyword-Match-%{version}
%if !%{with perl_Syntax_Keyword_Match_enables_optional_test}
for T in t/80await+matchcase.t t/80match-divides.t t/80match-equ.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done
%endif
chmod +x t/*.t

%build

perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{perl_vendorlib}/Syntax/Keyword/Match
mv %{buildroot}{%{perl_vendorarch},%{perl_vendorlib}}/Syntax/Keyword/Match/Deparse.pm
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Syntax-Keyword-Match-Deparse -f %{oreon_filedir}/perl-Syntax-Keyword-Match-Deparse.list
%files -n perl-Syntax-Keyword-Match-tests -f %{oreon_filedir}/perl-Syntax-Keyword-Match-tests.list

%changelog

%autochangelog
