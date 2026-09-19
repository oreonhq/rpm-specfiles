%global source0_hash fdb558b6fc90c17487867f80dc3fe038f7fc550f4bfd87afff3cfc3e5dc6bf93

# Perform optinal tests
%bcond_without perl_Test_NoBreakpoints_enables_optional_test

Name:           perl-Test-NoBreakpoints
Version:        0.17
Release:        15%{?dist}
Summary:        Test that files do not contain soft breakpoints
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-NoBreakpoints
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLAINEM/Test-NoBreakpoints-%{version}.tar.gz
# Ditch out t/02_pod.t if optional tests are disabled
Patch0:         Test-NoBreakpoints-0.17-Remove-t-02_pod.t.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  patch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(vars)
# Tests:
# FindBin not used
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Test::Tester) >= 0.09
BuildRequires:  perl(Test::UseAllModules)
BuildRequires:  perl(warnings)
%if %{with perl_Test_NoBreakpoints_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::NoWarnings)
%endif

# Filter unused dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(FindBin\\)
# Filter underspecified dependencies
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More\\)$

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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Test_NoBreakpoints_enables_optional_test}
patch --no-backup-if-mismatch -p1 -d %{buildroot}%{_libexecdir}/%{name} < %{PATCH0}
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset RELEASE_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
# Correct permissions
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
