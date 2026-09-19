%global source0_hash 931c34b43bbbec8c58972d5149daa6cccb31d4254034c470b7eb740b6f51bd6e

Name:       imvirt
Summary:    Detects several virtualizations
Version:    0.9.6
Release:    39%{?dist}
URL:        http://micky.ibh.net/~liske/imvirt.html
Source0:    http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
License:    GPL-2.0-only
Requires:   dmidecode
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: gcc
BuildRequires: make
ExclusiveArch: %{ix86} x86_64 ia64

%description
This little Perl script tries to detect if it is called from within 
a virtualization container. This is detected by looking for well known boot 
messages, directories and reading DMI (Desktop Management Interface) data.

The following containers are detected:

    * Virtual PC/Virtual Server
    * VirtualBox
    * VMware
    * QEMU/KVM (experimental)
    * Xen (para and non-para virtualized)
    * OpenVZ/Virtuozzo
    * UML
    * any HVM providing CPUID 0x40000000 detection
    * lguest
    * ARAnyM
    * LXC

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --prefix=%{_prefix} --libexec=%{_libexecdir}/imvirt
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{perl_vendorarch}/auto/ImVirt/.packlist
rm $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%check
#make check

%clean
make clean

%files
%{_sbindir}/imvirt-report
%{_bindir}/*
%dir %{_libexecdir}/imvirt
%{_libexecdir}/imvirt/*
%doc AUTHORS COPYING ChangeLog README
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{perl_vendorlib}/*

%changelog
%autochangelog
