%global source0_hash 10fbcf1e158d1c8d77e1dd934e379165b126a45c13645ad0be9dc07d151dd0cc
%bcond_without perl_Inline_C_enables_optional_tests
Name:           perl-Inline-C
Version:        0.82
Release:        1%{?dist}
Summary:        Write Perl subroutines in C
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Inline-C
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Inline-C-%{version}.tar.gz
Patch0:         Inline-C-0.82-Use-File-Path-for-creating-temporary-directories-in-.patch
BuildArch:      noarch
%if %{with perl_Inline_C_enables_optional_tests}
%endif
Requires:       gcc
Requires:       make
Requires:       perl-interpreter
Requires:       perl-devel
Requires:       perl(Fcntl)
Requires:       perl(FindBin)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Inline) >= 0.86
Requires:       perl(Parse::RecDescent) >= 1.967009
Requires:       perl(Time::HiRes)
Conflicts:      perl-Inline < 0.58
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Test::More|Test::Warn|version)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(TestInline
%global __provides_exclude %{?__provides_exclude:%{__requires_exclude}|}^perl\\(TestInline
Provides:       perl(Inline::C)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::MakeMaker)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Pegex::Base)
BuildRequires:  perl(Pegex::Parser)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Inline::C is a module that allows you to write Perl subroutines in C. Since
version 0.30 the Inline module supports multiple programming languages and
each language has its own support module.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(blib)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Inline::MakeMaker)
Requires:       perl(Test::More) >= 0.88
%if %{with perl_Inline_C_enables_optional_tests}
Requires:       perl(Test::Warn) >= 0.23
%endif
Requires:       perl(version) >= 0.77
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Inline-C-%{version}
%if !%{with perl_Inline_C_enables_optional_tests}
rm t/08taint.t
perl -i -ne 'print $_ unless m{^t/08taint\.t}' MANIFEST
%endif
# Remove author tests
rm t/author-pod-syntax.t
perl -i -ne 'print $_ unless m{^t/author-pod-syntax\.t}' MANIFEST
# Fix permissions
find example t -type f -exec chmod -x {} +
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a example t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/000-require-modules.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset ACTIVEPERL_CONFIG_SILENT AUTHOR_TESTING CPATH DEBUG INCLUDE MAKEFLAGS \
    PERL_INLINE_BUILD_NOISY PERL_INLINE_DEVELOPER_TEST PERL_INSTALL_ROOT \
    PERL_PEGEX_AUTO_COMPILE NO_INSANE_DIRNAMES
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset ACTIVEPERL_CONFIG_SILENT AUTHOR_TESTING CPATH DEBUG INCLUDE MAKEFLAGS \
    PERL_INLINE_BUILD_NOISY PERL_INLINE_DEVELOPER_TEST PERL_INSTALL_ROOT \
    PERL_PEGEX_AUTO_COMPILE NO_INSANE_DIRNAMES
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Inline-C-tests -f %{oreon_filedir}/perl-Inline-C-tests.list

%changelog

%autochangelog
