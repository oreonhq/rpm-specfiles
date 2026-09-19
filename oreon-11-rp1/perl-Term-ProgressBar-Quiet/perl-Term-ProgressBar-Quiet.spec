%global source0_hash 25675292f588bc29d32e710cf3667da9a2a1751e139801770a9fdb18cd2184a6

# Perform optional tests
%bcond_without perl_Term_ProgressBar_Quiet_enables_optional_test

Name:           perl-Term-ProgressBar-Quiet
Version:        0.31
Release:        35%{?dist}
Summary:        Provide a progress meter if run interactively
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-ProgressBar-Quiet
Source0:        https://cpan.metacpan.org/authors/id/L/LB/LBROCARD/Term-ProgressBar-Quiet-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(IO::Interactive)
BuildRequires:  perl(Term::ProgressBar)
BuildRequires:  perl(Test::MockObject)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
%if %{with perl_Term_ProgressBar_Quiet_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
%endif

%description
Term::ProgressBar is a wonderful module for showing progress bars on the
terminal. This module acts very much like that module when it is run
interactively. However, when it is not run interactively (for example,
as a cron job) then it does not show the progress bar.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-ProgressBar-Quiet-%{version}
%if !%{with perl_Term_ProgressBar_Quiet_enables_optional_test}
rm t/pod.t
perl -i -ne 'print $_ unless m{^t/pod\.t\b}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Term_ProgressBar_Quiet_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
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
%doc CHANGES README
%dir %{perl_vendorlib}/Term
%dir %{perl_vendorlib}/Term/ProgressBar
%{perl_vendorlib}/Term/ProgressBar/Quiet.pm
%{_mandir}/man3/Term::ProgressBar::Quiet.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
