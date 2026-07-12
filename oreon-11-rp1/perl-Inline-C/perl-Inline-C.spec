%global source0_hash 10fbcf1e158d1c8d77e1dd934e379165b126a45c13645ad0be9dc07d151dd0cc

# Perform optional tests
%bcond_without perl_Inline_C_enables_optional_tests

Name:           perl-Inline-C
Version:        0.82
Release:        14%{?dist}
Summary:        Write Perl subroutines in C
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Inline-C
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Inline-C-%{version}.tar.gz
# Fix tests to work from a read-only location, proposed to an upstream,
# <https://github.com/ingydotnet/inline-c-pm/pull/102>
Patch0:         Inline-C-0.82-Use-File-Path-for-creating-temporary-directories-in-.patch
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.00
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime:
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(FindBin)
BuildRequires:  perl(if)
BuildRequires:  perl(Inline) >= 0.86
# Inline::Filters and Inline::Struct are optional and introduce circular deps
BuildRequires:  perl(Parse::RecDescent) >= 1.967009
BuildRequires:  perl(Pegex::Base)
BuildRequires:  perl(Pegex::Parser)
BuildRequires:  perl(Time::HiRes)
# Tests only:
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
# t/27inline_maker.t uses example/modules/Boo-2.01 that uses Inline::MakeMaker
# that generated Makefile.PL with "perl -Mblib".
BuildRequires:  perl(blib)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Inline::MakeMaker)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(YAML::XS)
%if %{with perl_Inline_C_enables_optional_tests}
# Optional tests only:
BuildRequires:  perl(Test::Warn) >= 0.23
%endif
# It executes C compiler to build generated XS code
Requires:       gcc
# It executes make
Requires:       make
# It executes "perl Makefile.PL"
Requires:       perl-interpreter
# It requires Perl header files in the generated and compiled XS code
Requires:       perl-devel
Requires:       perl(Fcntl)
Requires:       perl(FindBin)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Inline) >= 0.86
Requires:       perl(Parse::RecDescent) >= 1.967009
Requires:       perl(Time::HiRes)
# Split from Inline in 0.58
Conflicts:      perl-Inline < 0.58

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Test::More|Test::Warn|version)\\)$

# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(TestInline
%global __provides_exclude %{?__provides_exclude:%{__requires_exclude}|}^perl\\(TestInline

Provides:       perl(Inline::C)
%description
Inline::C is a module that allows you to write Perl subroutines in C. Since
version 0.30 the Inline module supports multiple programming languages and
each language has its own support module.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# t/27inline_maker.t uses example/modules/Boo-2.01 that uses Inline::MakeMaker
# that generated Makefile.PL with "perl -Mblib".
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a example t %{buildroot}%{_libexecdir}/%{name}
# t/000-require-modules.t operates on modules in ./lib, do not symlink the tree
# to prevent from generating RPM dependencies on them. Remove the test inestead.
rm %{buildroot}%{_libexecdir}/%{name}/t/000-require-modules.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset ACTIVEPERL_CONFIG_SILENT AUTHOR_TESTING CPATH DEBUG INCLUDE MAKEFLAGS \
    PERL_INLINE_BUILD_NOISY PERL_INLINE_DEVELOPER_TEST PERL_INSTALL_ROOT \
    PERL_PEGEX_AUTO_COMPILE NO_INSANE_DIRNAMES
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset ACTIVEPERL_CONFIG_SILENT AUTHOR_TESTING CPATH DEBUG INCLUDE MAKEFLAGS \
    PERL_INLINE_BUILD_NOISY PERL_INLINE_DEVELOPER_TEST PERL_INSTALL_ROOT \
    PERL_PEGEX_AUTO_COMPILE NO_INSANE_DIRNAMES
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/auto/share
%dir %{perl_vendorlib}/auto/share/dist
%{perl_vendorlib}/auto/share/dist/Inline-C
%dir %{perl_vendorlib}/Inline
%{perl_vendorlib}/Inline/C
%{perl_vendorlib}/Inline/C.pod
%{perl_vendorlib}/Inline/C.pm
%{_mandir}/man3/Inline::C::*
%{_mandir}/man3/Inline::C.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
