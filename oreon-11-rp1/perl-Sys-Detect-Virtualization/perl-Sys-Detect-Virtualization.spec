%global source0_hash 0927993d24b90ce8ceac66fecad250492c83e51ff62cfe8458b8071d82a9a107
%bcond_without perl_Sys_Detect_Virtualization_enables_optional_test
Name:           perl-Sys-Detect-Virtualization
Version:        0.107
Release:        1%{?dist}
Summary:        Library to detect if a UNIX system is running as a virtual machine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-Detect-Virtualization
Source0:        https://cpan.metacpan.org/modules/by-module/Sys/Sys-Detect-Virtualization-%{version}.tar.gz
Patch1:         sys_detect_virt_dmidecode.patch
Patch2:         sys_detect_virt_perldoc.patch
%ifarch %{ix86} x86_64 ia64
%endif
%if %{with perl_Sys_Detect_Virtualization_enables_optional_test}
%endif
%ifarch %{ix86} x86_64 ia64
Requires:       perl(Parse::DMIDecode) >= 0.03
%endif
%global debug_package %{nil}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module attempts to detect whether or not a system is running as a
guest under virtualization, using various heuristics.

%package -n virtdetect
Summary:        Detect if a UNIX system is running as a virtual machine
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
%oreon_autofiles virtdetect usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset RELEASE_TESTING
make test
%files -f %{oreon_filedir}/main.list
%files -n virtdetect -f %{oreon_filedir}/virtdetect.list

%changelog

%autochangelog
