%global source0_hash 61980551e46b2eaa9e17ad31cbc1a638074611fc33bff34163d10c7a67a9fdc6

%global _hardened_build 1

Summary:         Utilities for infrared communication between devices
Name:            irda-utils
Version:         0.9.18
Release:         53%{?dist}
Url:             http://irda.sourceforge.net
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:         GPL-2.0-or-later
ExcludeArch:     s390 s390x
Source0: http://downloads.sourceforge.net/irda/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1: irda.init
Source2: irda.service
Source3: irda.sysconfig
Patch1: irda-utils-0.9.17-rootonly.patch
Patch2: irda-utils-0.9.15-rh1.patch
Patch3: irda-utils-0.9.16-io.patch
Patch4: irda-utils-0.9.17-makefile.patch
Patch6: irda-utils-0.9.18-root.patch
Patch7: irda-utils-0.9.18-man.patch
Patch8: irda-utils-0.9.18-PIE.patch
Patch9: irda-utils-0.9.18-no-inline.patch
Patch10: irda-utils-0.9.18-run.patch
Patch11: irda-utils-0.9.18-sbin.patch
BuildRequires: gcc
BuildRequires: glib2-devel, pciutils-devel
BuildRequires: systemd-units
BuildRequires: make

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
IrDA(TM) (Infrared Data Association) is an industry standard for
wireless, infrared communication between devices. IrDA speeds range
from 9600 bps to 4 Mbps, and IrDA can be used by many modern devices
including laptops, LAN adapters, PDAs, printers, and mobile phones.

The Linux-IrDA project is a GPL'd implementation, written from
scratch, of the IrDA protocols. Supported IrDA protocols include
IrLAP, IrLMP, IrIAP, IrTTP, IrLPT, IrLAN, IrCOMM and IrOBEX.

The irda-utils package contains a collection of programs that enable
the use of IrDA protocols. Most IrDA features are implemented in the
kernel, so IrDA support must be enabled in the kernel before any IrDA
tools or programs can be used. Some configuration outside the kernel
is required, however, and some IrDA features, like IrOBEX, are
actually implemented outside the kernel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P6 -p1
gunzip man/irnet.4.gz man/irda.7.gz
%patch -P7 -p1
gzip -9 man/irnet.4 man/irda.7
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1

%build
export LDFLAGS="%{?__global_ldflags}"
make all RPM_OPT_FLAGS="$RPM_OPT_FLAGS -std=gnu89" ROOT="$RPM_BUILD_ROOT" \
   LDFLAGS="%{?__global_ldflags}" \
   CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

for dir in %{_bindir} %{_initrddir} %{_sysconfdir}/sysconfig
do
    install -d $RPM_BUILD_ROOT$dir
done

make install  ROOT="$RPM_BUILD_ROOT" MANDIR="$RPM_BUILD_ROOT/%{_mandir}"

#install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT/%{_initrddir}/irda
#chmod -x $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/irda
rm -f $RPM_BUILD_ROOT/%{_initrddir}/irda

install -d $RPM_BUILD_ROOT%{_unitdir}
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/irda.service
install -p -m644 %{SOURCE3} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/irda

rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts/ifcfg-irlan0

for i in irattach irdadump irdaping tekram
do
    [ -f $i/README ] && ln $i/README README.$i
done
iconv -f ISO8859-1 -t UTF-8 <README.irdadump >README.irdadump.new && \
	mv -f README.irdadump.new README.irdadump
mv etc/modules.conf.irda etc/modprobe.conf.irda
chmod -x etc/ifcfg-irlan0

%post
%systemd_post irda.service

%preun
%systemd_preun irda.service

%postun
%systemd_postun_with_restart irda.service

%files
%{_bindir}/*
%{_mandir}/*/*
%{_unitdir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/irda
%doc README* etc/ifcfg-irlan0 etc/modprobe.conf.irda

%changelog
%autochangelog
