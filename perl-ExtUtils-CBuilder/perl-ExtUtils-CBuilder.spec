%global base_version 0.280236

Name:           perl-ExtUtils-CBuilder
# Compete with perl.spec
Epoch:          1
# Mimic perl.spec
Version:        0.280242
Release:        521%{?dist}
Summary:        Compile and link C code for Perl modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-CBuilder
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/ExtUtils-CBuilder-%{base_version}.tar.gz
# Link XS modules to libperl.so with EU::CBuilder on Linux, bug #960048
Patch0:         ExtUtils-CBuilder-0.280230-Link-XS-modules-to-libperl.so-with-EU-CBuilder-on-Li.patch
# Unbundled from perl 5.37.11
Patch1:         ExtUtils-CBuilder-0.280236-Upgrade-to-0.280238.patch
# Unbundled from perl 5.40.0-RC1
Patch2:         ExtUtils-CBuilder-0.280238-Upgrade-to-0.280240.patch
# Unbundled from perl 5.42.0
Patch3:         ExtUtils-CBuilder-0.280240-Upgrade-to-0.280242.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
# ExtUtils::Mksymlists 6.30 not used at test time
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 3.13
# File::Spec::Functions not used at test time
BuildRequires:  perl(File::Temp)
# IO::File not used at test time
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Perl::OSType) >= 1
BuildRequires:  perl(Text::ParseWords)
# Optional run-time:
# C and C++ compilers are highly recommended because compiling code is the
# purpose of ExtUtils::CBuilder, bug #1547165
BuildRequires:  gcc
BuildRequires:  gcc-c++
# Tests:
BuildRequires:  perl(Test::More) >= 0.47
# vmsish not used
# C and C++ compilers are highly recommended because compiling code is the
# purpose of ExtUtils::CBuilder, bug #1547165
Requires:       gcc
Requires:       gcc-c++
Requires:       perl-devel
Requires:       perl(DynaLoader)
Requires:       perl(ExtUtils::Mksymlists) >= 6.30
Requires:       perl(File::Spec) >= 3.13
Requires:       perl(Perl::OSType) >= 1

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Perl::OSType)\\)$

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was motivated
by the Module::Build project, but may be useful for other purposes as well.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n ExtUtils-CBuilder-%{base_version}

# Normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Tests write into temporary files/directories. The solution is to copy the
# tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README README.mkdn
%dir %{perl_vendorlib}/ExtUtils
%{perl_vendorlib}/ExtUtils/CBuilder*
%{_mandir}/man3/ExtUtils::CBuilder*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.280242-521
- Prepare for Oreon 11 (RP1)
