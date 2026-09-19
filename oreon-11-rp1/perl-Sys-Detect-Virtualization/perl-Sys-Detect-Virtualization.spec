%global source0_hash 0927993d24b90ce8ceac66fecad250492c83e51ff62cfe8458b8071d82a9a107

# Perform optional tests
%bcond_without perl_Sys_Detect_Virtualization_enables_optional_test

Name:           perl-Sys-Detect-Virtualization
Version:        0.107
Release:        37%{?dist}
Summary:        Library to detect if a UNIX system is running as a virtual machine
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-Detect-Virtualization
Source0:        https://cpan.metacpan.org/modules/by-module/Sys/Sys-Detect-Virtualization-%{version}.tar.gz
# Included from https://rt.cpan.org/Public/Bug/Display.html?id=86673 to allow building on archs that do not have Parse::DMIDecode
Patch1:         sys_detect_virt_dmidecode.patch
# Included from https://rt.cpan.org/Public/Bug/Display.html?id=95536 to pass POD tests
Patch2:         sys_detect_virt_perldoc.patch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
# Getopt::Long not used at tests
# The dmidecode package (and perl-Parse-DMIDecode) are only available on the
# following architectures
%ifarch %{ix86} x86_64 ia64
BuildRequires:  perl(Parse::DMIDecode) >= 0.03
%endif
# Pod::Usage not used at tests
# POSIX not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.82
%if %{with perl_Sys_Detect_Virtualization_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
# Test::CheckManifest not used
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
%ifarch %{ix86} x86_64 ia64
Requires:       perl(Parse::DMIDecode) >= 0.03
%endif

# There is no need for a debug package. The only reason an arch is important
# is because of the BuildRequires not available everywhere.
%global debug_package %{nil}

%description
This module attempts to detect whether or not a system is running as a
guest under virtualization, using various heuristics.

%package -n virtdetect
Summary:        Detect if a UNIX system is running as a virtual machine
# The BuildArch is now irrelevant, Sys::Detect::Virtualization hides the dependency on dmidecode
BuildArch:      noarch

%description -n virtdetect
This script attempts to detect whether or not a system is running as a
guest under virtualization, using various heuristics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sys-Detect-Virtualization-%{version}
%patch -P1 -p1
%patch -P2 -p1
# Remove bundled modules
rm -rf ./inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%if !%{with perl_Sys_Detect_Virtualization_enables_optional_test}
rm t/pod.t t/pod-coverage.t
perl -i -ne 'print $_ unless m{^t/pod.*\.t}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset RELEASE_TESTING
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files -n virtdetect
%doc README
%{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
