%global source0_hash e98fa1f86774fe7ad10f6fbedfb5cbf7dfa1c54112ff80121b5cfc4e006e2bd6

# Perform optional tests
%bcond_without perl_Parse_DMIDecode_enables_optional_tests

Name:           perl-Parse-DMIDecode
Version:        0.03
Release:        42%{?dist}
Summary:        Interface to SMBIOS using dmidecode
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Parse-DMIDecode
Source0:        https://cpan.metacpan.org/modules/by-module/Parse/Parse-DMIDecode-%{version}.tar.gz
# Pod fixing patch from RT 52296 -> https://rt.cpan.org/Ticket/Attachment/699959/360879/fix-pod-urls.patch
Patch1:         fix-pod-urls.patch
# Fix a memory leak when destructing Parse::DMIDecode::Handle objects,
# CPAN RT#125088
Patch2:         Parse-DMIDecode-0.03-handle_leak.patch
# Fix supressing portability warnings, CPAN RT#143252, proposed to the upstream
Patch3:         Parse-DMIDecode-0.03-Disable-portability-warnings-lexically.patch
# Do not warn on SMBIOS version 3, bug #1661251, CPAN RT#54956, proposed to
# the upstream
Patch4:         Parse-DMIDecode-0.03-Emulate-number-of-structures-if-not-reported-by-dmid.patch
# This mirrors the ExclusiveArch in the dmidecode spec file
ExclusiveArch:  %{ix86} x86_64 ia64 aarch64 riscv64
# A debug package is not required as there are no binaries in this package. We
# are not noarch because of dmidecode
%global debug_package %{nil}
BuildRequires:  coreutils
BuildRequires:  dmidecode
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Config not used
# LWP::UserAgent not used
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Which) >= 0.05
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(Data::Dumper)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
%if %{with perl_Parse_DMIDecode_enables_optional_tests}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.2
BuildRequires:  perl(Test::Pod::Coverage) >= 1.06
%endif
Requires:       dmidecode
Suggests:       perl(Data::Dumper)
Requires:       perl(File::Which) >= 0.05

%description
This module provides an OO interface to SMBIOS information through the
dmidecode command which is known to work under a number of Linux, BSD and
BeOS variants.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Parse-DMIDecode-%{version}
%if !%{with perl_Parse_DMIDecode_enables_optional_tests}
rm t/10pod.t t/11pod_coverage.t
perl -i -ne 'print $_ unless m{^t/1[01]pod}' MANIFEST
%endif

%build
AUTOMATED_TESTING=1 %{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset DEBUG
./Build test

%files
%license LICENSE
%doc Changes NOTICE README TODO examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
