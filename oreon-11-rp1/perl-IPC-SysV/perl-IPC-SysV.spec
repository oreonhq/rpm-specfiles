%global source0_hash 1897541c74d548fd1007eb6c07f3419d3c7575d8056a62b5ba5270a2166d2dbd
%bcond_with perl_IPC_SysV_enables_optional_test
Name:           perl-IPC-SysV
Version:        2.09
Release:        1%{?dist}
Summary:        Object interface to System V IPC
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IPC-SysV
Source0:        https://cpan.metacpan.org/authors/id/M/MH/MHX/IPC-SysV-%{version}.tar.gz
%if !%{with perl_IPC_SysV_enables_optional_test} || %{defined perl_bootstrap}
%endif
%if %{with perl_IPC_SysV_enables_optional_test} && !%{defined perl_bootstrap}
%endif
Conflicts:      perl < 4:5.22.0-351
Provides:       perl(IPC::SysV)
Provides:       perl(IPC::Semaphore)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is an object interface for System V messages, semaphores, and
inter-process calls.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Config)
Requires:       perl(Test::More)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IPC-SysV-%{version}
%if !%{with perl_IPC_SysV_enables_optional_test} || %{defined perl_bootstrap}
rm t/pod*
perl -i -ne 'print $_ unless m{^t/pod}' MANIFEST
%endif

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_IPC_SysV_enables_optional_test} && !%{defined perl_bootstrap}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
unset PERL_CORE
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-IPC-SysV-tests -f %{oreon_filedir}/perl-IPC-SysV-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.09-522
- Prepare for Oreon 11 (RP1)
