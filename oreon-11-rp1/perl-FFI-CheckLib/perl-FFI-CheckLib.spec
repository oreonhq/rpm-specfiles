%global source0_hash 04d885fc377d44896e5ea1c4ec310f979bb04f2f18658a7e7a4d509f7e80bb80

# Run optional test
%{bcond_without perl_FFI_Changes_enables_optional_test}

Name:           perl-FFI-CheckLib
Version:        0.31
Release:        10%{?dist}
Summary:        Check that a library is available for FFI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/FFI-CheckLib
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/FFI-CheckLib-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
# File::Which is used from private functions which are only called on Darwin.
BuildRequires:  perl(List::Util) >= 1.33
# Tests:
# File::Which is a run-time dependency on Darwin only. The code is exhibited by a test,
# but never on Linux in production.
BuildRequires:  perl(File::Which)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Require::EnvVar) >= 0.000121
BuildRequires:  perl(Test2::Require::Module) >= 0.000121
BuildRequires:  perl(Test2::V0) >= 0.000121
%if %{with perl_FFI_Changes_enables_optional_test}
# Optional tests:
# Test/More.pl is not helpful
# FFI::Platypus not used
BuildRequires:  perl(Test2::Tools::Process)
%endif
Requires:       perl(DynaLoader)
Requires:       perl(File::Basename)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test2::API|Test2::Require::EnvVar|Test2::Require::Module|Test2::V0)\\)$

# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\((Test2::Plugin::FauxOS|Test2::Tools::FauxDynaLoader|Test2::Tools::NoteStderr)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((Alien::libbar|Test2::Plugin::FauxOS|Test2::Tools::FauxDynaLoader|Test2::Tools::NoteStderr)\\)

%description
This Perl module checks whether a particular dynamic library is available for
Foreign Function Interface (FFI) to use. It is modeled heavily on
Devel::CheckLib, but will find dynamic libraries even when development
packages are not installed. It also provides a find_lib function that will
return the full path to the found dynamic library, which can be feed directly
into FFI::Platypus or FFI::Raw.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# Tests:
# File::Which is a run-time dependency on Darwin only. The code is exhibited by a test,
# but never on Linux in production.
Requires:       perl(File::Which)
Requires:       perl(Test2::API) >= 1.302015
Requires:       perl(Test2::Require::EnvVar) >= 0.000121
Requires:       perl(Test2::Require::Module) >= 0.000121
Requires:       perl(Test2::V0) >= 0.000121

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n FFI-CheckLib-%{version}
%if !%{with perl_FFI_Changes_enables_optional_test}
rm t/ffi_checklib__exit.t
perl -i -ne 'print $_ unless m{\A\Qt/ffi_checklib__exit.t\E\b}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset CIPSOMETHING FFI_CHECKLIB_PATH
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset CIPSOMETHING FFI_CHECKLIB_PATH
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/FFI
%{perl_vendorlib}/FFI/CheckLib.pm
%{_mandir}/man3/FFI::CheckLib.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
