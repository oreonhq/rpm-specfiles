%global source0_hash 859fb75ff4b5c87323d814b21809b25ccd8c671eef54d4c7e16d2c8f12930744
%bcond_without perl_Test2_Tools_Process_enables_extended_test
Name:           perl-Test2-Tools-Process
Version:        0.07
Release:        1%{?dist}
Summary:        Unit tests for code that calls exit, exec, system or qx()
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test2-Tools-Process
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Test2-Tools-Process-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Test2_Tools_Process_enables_extended_test}
%endif
Requires:       perl(Config)
Requires:       perl(Test2::API) >= 1.302015
Requires:       perl(Test2::Compare) >= 0.000121
Requires:       perl(Test2::Compare::Array) >= 0.000121
Requires:       perl(Test2::Compare::Custom) >= 0.000121
Requires:       perl(Test2::Compare::Number) >= 0.000121
Requires:       perl(Test2::Compare::String) >= 0.000121
Requires:       perl(Test2::Compare::Wildcard) >= 0.000121
Requires:       perl(Test2::Tools::Compare) >= 0.000121
Provides:       perl-Test-Exec = %{version}-%{release}
Obsoletes:      perl-Test-Exec < 0.04-12
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test::More|Test2::API|Test2::Compare(|::Array|::Custom|::Number|::String|::Wildcard)|Test2::Tools::Compare|Test2::V0)\\)$
# oreon:deps
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Return::MultiLevel)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Compare)
BuildRequires:  perl(Test2::Compare::Array)
BuildRequires:  perl(Test2::Compare::Custom)
BuildRequires:  perl(Test2::Compare::Number)
BuildRequires:  perl(Test2::Compare::String)
BuildRequires:  perl(Test2::Compare::Wildcard)
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This set of testing tools is intended for writing unit tests for code that
interacts with other processes without using real processes that might have
unwanted side effects. It also lets you test code that exits program flow
without actually terminating your test. So far it allows you to test and/or
mock exit, exec, system, readpipe and qx//. Other process related tests
will be added in the future.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.98
Requires:       perl(Test2::V0) >= 0.000121
%if %{with perl_Test2_Tools_Process_enables_extended_test}
Requires:       bash
Requires:       coreutils
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test2-Tools-Process-%{version}
%if !%{with perl_Test2_Tools_Process_enables_extended_test}
rm t/test2_tools_process__live.t
perl -i -ne 'print $_ unless m{\A\Qt/test2_tools_process__live.t\E\b}' MANIFEST
%endif
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
unset CIPSOMETHING RETURN_MULTILEVEL_DEBUG
%if %{with perl_Test2_Tools_Process_enables_extended_test}
export CIPSOMETHING=true
%endif
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset CIPSOMETHING RETURN_MULTILEVEL_DEBUG
%if %{with perl_Test2_Tools_Process_enables_extended_test}
export CIPSOMETHING=true
%endif
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test2-Tools-Process-tests -f %{oreon_filedir}/perl-Test2-Tools-Process-tests.list

%changelog

%autochangelog
