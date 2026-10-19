%global source0_hash e98fa1f86774fe7ad10f6fbedfb5cbf7dfa1c54112ff80121b5cfc4e006e2bd6
%bcond_without perl_Parse_DMIDecode_enables_optional_tests
Name:           perl-Parse-DMIDecode
Version:        0.03
Release:        1%{?dist}
Summary:        Interface to SMBIOS using dmidecode
License:        Apache-2.0
URL:            https://metacpan.org/release/Parse-DMIDecode
Source0:        https://cpan.metacpan.org/modules/by-module/Parse/Parse-DMIDecode-%{version}.tar.gz
Patch1:         fix-pod-urls.patch
Patch2:         Parse-DMIDecode-0.03-handle_leak.patch
Patch3:         Parse-DMIDecode-0.03-Disable-portability-warnings-lexically.patch
Patch4:         Parse-DMIDecode-0.03-Emulate-number-of-structures-if-not-reported-by-dmid.patch
ExclusiveArch:  %{ix86} x86_64 ia64 aarch64 riscv64
%global debug_package %{nil}
%if %{with perl_Parse_DMIDecode_enables_optional_tests}
%endif
Requires:       dmidecode
Suggests:       perl(Data::Dumper)
Requires:       perl(File::Which) >= 0.05
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  dmidecode
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

unset DEBUG
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
