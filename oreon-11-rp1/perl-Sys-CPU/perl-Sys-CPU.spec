Name:           perl-Sys-CPU
Version:        0.61
Release:        42%{?dist}
Summary:        Getting CPU information

# Some code was copied from Unix::Processors, which is LGPL-3.0-only OR Artistic-2.0
# The rest of the code is under the standard Perl license (GPL-1.0-or-later OR Artistic-1.0-Perl).
# See <https://bugzilla.redhat.com/show_bug.cgi?id=585336>.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (LGPL-3.0-only OR Artistic-2.0)
URL:            https://metacpan.org/release/Sys-CPU
Source0:        https://cpan.metacpan.org/authors/id/M/MZ/MZSANFORD/Sys-CPU-%{version}.tar.gz
# Support cpu_type on ARM and AArch64, bug #1093266, CPAN RT#95400
Patch0:         Sys-CPU-0.61-Add-support-for-cpu_type-on-ARM-and-AArch64-Linux-pl.patch
# Accept undefined cpu_clock on ARM and AArch64, bug #1093266, CPAN RT#95400
Patch1:         Sys-CPU-0.61-cpu_clock-can-be-undefined-on-an-ARM.patch
# Add support for RISC-V 64-bit (RV64GC) aka riscv64
Patch2:         add-support-riscv64.patch
# oreon url source checksums begin
%global source0_sha256 250a86b79c231001c4ae71d2f66428092a4fbb2070971acafd471aa49739c9e4
%global source0_file Sys-CPU-0.61.tar.gz
# oreon url source checksums end
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)

%{?perl_default_filter}

%description
Perl extension for getting CPU information. 
Currently only number of CPU's supported.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Sys-CPU-0.61.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "250a86b79c231001c4ae71d2f66428092a4fbb2070971acafd471aa49739c9e4" || { echo "oreon: Source0 SHA256 mismatch for Sys-CPU-0.61.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Sys-CPU-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
sed -i 's/\r//' Changes README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test TEST_VERBOSE=1

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name CPU.bs -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys/*
%{_mandir}/man3/*.3*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.61-42
- Prepare for Oreon 11 (RP1)
