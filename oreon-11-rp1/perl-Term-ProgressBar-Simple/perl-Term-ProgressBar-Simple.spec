%global source0_hash a20db3c67d5bdfd0c1fab392c6d1c26880a7ee843af602af4f9b53a7043579a6
%bcond_without perl_Term_ProgressBar_Simple_enables_optional_test
Name:           perl-Term-ProgressBar-Simple
Version:        0.03
Release:        1%{?dist}
Summary:        Simpler progress bars
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-ProgressBar-Simple
Source0:        https://cpan.metacpan.org/authors/id/E/EV/EVDB/Term-ProgressBar-Simple-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Term_ProgressBar_Simple_enables_optional_test}
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Term::ProgressBar::Quiet)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Term_ProgressBar_Simple_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Term-ProgressBar-Simple-tests -f %{oreon_filedir}/perl-Term-ProgressBar-Simple-tests.list

%changelog

%autochangelog
