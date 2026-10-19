%global source0_hash 0a5aa5953ab65cf790681e6c0452e318ad57d80ac27f575f84918c603aa47406
%bcond_without perl_DBD_Mock_enabled_optional_test
Name:           perl-DBD-Mock
Version:        1.59
Release:        1%{?dist}
Summary:        Mock database driver for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBD-Mock
Source0:        https://cpan.metacpan.org/authors/id/J/JL/JLCOOPER/DBD-Mock-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_DBD_Mock_enabled_optional_test}
%endif
Requires:       perl(DBI) >= 1.3
Requires:       perl(List::Util) >= 1.27
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DBI|List::Util|Test::Exception|Test::More)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBI)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Testing with databases can be tricky. If you are developing a system married
to a single database then you can make some assumptions about your environment
and ask the user to provide relevant connection information.  But if you need
to test a framework that uses DBI, particularly a framework that uses
different types of persistence schemes, then it may be more useful to simply
verify what the framework is trying to do -- ensure the right SQL is generated
and that the correct parameters are bound. DBD::Mock makes it easy to just
modify your configuration (presumably held outside your code) and just use it
instead of DBD::Foo (like DBD::Pg or DBD::mysql) in your framework.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(DBI) >= 1.3
Requires:       perl(Test::Exception) >= 0.31
Requires:       perl(Test::More) >= 0.47
%if %{with perl_DBD_Mock_enabled_optional_test}
Requires:       perl(Test::Pod::Coverage) >= 1.04
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBD-Mock-%{version}
%if !%{with perl_DBD_Mock_enabled_optional_test}
rm 998_pod.t 999_pod_coverage.t
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor
./Build
%install
find blib/libdoc -type f -empty -delete
./Build install --destdir=%{buildroot} --create_packlist=0
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
%if %{with perl_DBD_Mock_enabled_optional_test}
rm %{buildroot}/%{_libexecdir}/%{name}/t/998_pod.t
%endif
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
set -e
unset REPORT_TEST_ENVIRONMENT
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset REPORT_TEST_ENVIRONMENT
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-DBD-Mock-tests -f %{oreon_filedir}/perl-DBD-Mock-tests.list

%changelog

%autochangelog
