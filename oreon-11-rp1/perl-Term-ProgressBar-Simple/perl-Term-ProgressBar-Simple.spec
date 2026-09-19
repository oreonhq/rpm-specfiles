%global source0_hash a20db3c67d5bdfd0c1fab392c6d1c26880a7ee843af602af4f9b53a7043579a6

# Perform optional tests
%bcond_without perl_Term_ProgressBar_Simple_enables_optional_test

Name:           perl-Term-ProgressBar-Simple
Version:        0.03
Release:        35%{?dist}
Summary:        Simpler progress bars
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-ProgressBar-Simple
Source0:        https://cpan.metacpan.org/authors/id/E/EV/EVDB/Term-ProgressBar-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(overload)
BuildRequires:  perl(Term::ProgressBar::Quiet)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
%if %{with perl_Term_ProgressBar_Simple_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(Pod::Coverage) >= 0.19
%endif

%description
Progress bars are handy - they tell you how much work has been done, how
much is left to do and estimate how long it will take. This module does the
right thing in almost all cases in a really convenient way.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-ProgressBar-Simple-%{version}
%if %{without perl_Term_ProgressBar_Simple_enables_optional_test}
rm t/pod*
perl -i -ne 'print $_ unless m{^t/pod}' MANIFEST
%endif
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Term_ProgressBar_Simple_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc CHANGES
%dir %{perl_vendorlib}/Term
%dir %{perl_vendorlib}/Term/ProgressBar
%{perl_vendorlib}/Term/ProgressBar/Simple.pm
%{_mandir}/man3/Term::ProgressBar::Simple.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
