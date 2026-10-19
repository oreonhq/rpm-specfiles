%global source0_hash 46fdd7e750963dd3f90fbddb592b57096568ece31d93a5e77978d695a2eefa24
Name:       perl-Eval-Context
Version:    0.09.11
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Evaluate Perl code in context wrapper
Source0:        https://cpan.metacpan.org/authors/id/N/NK/NKH/Eval-Context-%{version}.tar.gz
Url:        https://metacpan.org/release/Eval-Context
Patch0:     Eval-Context-0.09.11-hash-randomization.patch
Patch1:     Eval-Context-0.09.11-adapt-test-for-Data-TreeDumper-0.41.patch
Patch2:     Eval-Context-0.09.11-Adapt-test-for-change-of-import.patch
Patch3:     Eval-Context-0.09.11-Adapt-tests-to-perl-5.40.0.patch
BuildArch:  noarch
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Data::TreeDumper\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::TreeDumper)
BuildRequires:  perl(Directory::Scratch::Structured)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Module::Build::Compat)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Block)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module defines a subroutine that let you evaluate Perl code in a
specific context. The code can be passed directly as a string or as a file
name to read from.  It also provides some subroutines to let you define and
optionally share variables and subroutines between your code and the code
you wish to evaluate. Finally there is some support for running your code
in a safe compartment.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Data::TreeDumper) >= 0.41
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Eval-Context-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Eval-Context-tests -f %{oreon_filedir}/perl-Eval-Context-tests.list

%changelog

%autochangelog
