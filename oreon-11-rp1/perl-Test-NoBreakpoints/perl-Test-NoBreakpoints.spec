%global source0_hash fdb558b6fc90c17487867f80dc3fe038f7fc550f4bfd87afff3cfc3e5dc6bf93
%bcond_without perl_Test_NoBreakpoints_enables_optional_test
Name:           perl-Test-NoBreakpoints
Version:        0.17
Release:        15%{?dist}
Summary:        Test that files do not contain soft breakpoints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-NoBreakpoints
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLAINEM/Test-NoBreakpoints-%{version}.tar.gz
Patch0:         Test-NoBreakpoints-0.17-Remove-t-02_pod.t.patch
BuildArch:      noarch
%if %{with perl_Test_NoBreakpoints_enables_optional_test}
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(FindBin\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  patch
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(Test::UseAllModules)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::NoBreakpoints checks that files contain neither the string
"$DB::single = 1" nor "$DB::signal = 1". 

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.92
%if %{with perl_Test_NoBreakpoints_enables_optional_test}
Requires:       perl(Test::NoWarnings)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-NoBreakpoints-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done
# We cannot remove t/release-* tests here because they are used by t/04_all_perl_files.t
%if !%{with perl_Test_NoBreakpoints_enables_optional_test}
%patch -P0 -p1
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Test_NoBreakpoints_enables_optional_test}
patch --no-backup-if-mismatch -p1 -d %{buildroot}%{_libexecdir}/%{name} < %{PATCH0}
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset RELEASE_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset RELEASE_TESTING
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-NoBreakpoints-tests -f %{oreon_filedir}/perl-Test-NoBreakpoints-tests.list

%changelog

%autochangelog
