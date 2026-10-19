%global source0_hash 250a86b79c231001c4ae71d2f66428092a4fbb2070971acafd471aa49739c9e4
Name:           perl-Sys-CPU
Version:        0.61
Release:        1%{?dist}
Summary:        Getting CPU information
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (LGPL-3.0-only OR Artistic-2.0)
URL:            https://metacpan.org/release/Sys-CPU
Source0:        https://cpan.metacpan.org/authors/id/M/MZ/MZSANFORD/Sys-CPU-%{version}.tar.gz
Patch0:         Sys-CPU-0.61-Add-support-for-cpu_type-on-ARM-and-AArch64-Linux-pl.patch
Patch1:         Sys-CPU-0.61-cpu_clock-can-be-undefined-on-an-ARM.patch
Patch2:         add-support-riscv64.patch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  sed
# /oreon:deps
%description
Perl extension for getting CPU information. 
Currently only number of CPU's supported.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.61-42
- Prepare for Oreon 11 (RP1)
