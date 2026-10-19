%global source0_hash 7882c8e7c89c4a6d79809959b30c7978d2e2933ccb74be6d809488b0cc80d938
Name:           powerpc-utils
Version:        1.3.14
Release:        1%{?dist}
Summary:        PERL-based scripts for maintaining and servicing PowerPC systems
License:        GPL-2.0-only
URL:            https://github.com/ibm-power-utilities/powerpc-utils
Source0:        https://github.com/ibm-power-utilities/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        nx-gzip.udev
Patch0:         powerpc-utils-1.3.11-manpages.patch
ExclusiveArch:  ppc %{power64}
Requires:       perl(Data::Dumper)
Requires:       %{name}-core = %{version}-%{release}
# oreon:deps
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  librtas-devel
BuildRequires:  libservicelog-devel
BuildRequires:  make
BuildRequires:  numactl-devel
BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
PERL-based scripts for maintaining and servicing PowerPC systems.

%package core
Summary: Core utilities for maintaining and servicing PowerPC systems
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: kmod
Requires: which
Requires: /usr/bin/awk
Requires: /usr/bin/basename
Requires: /usr/bin/bc
Requires: /usr/bin/cat
Requires: /usr/bin/cut
Requires: /usr/bin/echo
Requires: /usr/bin/find
Requires: /bin/grep
Requires: /usr/bin/head
Requires: /usr/bin/ls
Requires: /usr/bin/sed
Requires: /usr/bin/tr
Requires: /usr/bin/udevadm
Conflicts: libnxz < 0.63-3
%description core
Core utilities for maintaining and servicing PowerPC systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
CFLAGS="$RPM_OPT_FLAGS -std=gnu17"
%configure --with-systemd=%{_unitdir} --disable-werror
make %{?_smp_mflags} V=1
%install
make install DESTDIR=$RPM_BUILD_ROOT FILES= RCSCRIPTS=
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}
install $RPM_BUILD_ROOT/usr/share/doc/packages/powerpc-utils/* -t $RPM_BUILD_ROOT%{_pkgdocdir}
rm -rf $RPM_BUILD_ROOT/usr/share/doc/packages/powerpc-utils
rm -f $RPM_BUILD_ROOT%{_pkgdocdir}/COPYING
install -pDm 644  %{SOURCE1}  %{buildroot}%{_udevrulesdir}/90-nx-gzip.rules
rm -rf $RPM_BUILD_ROOT/etc/init.d/ibmvscsis.sh $RPM_BUILD_ROOT/usr/sbin/vscsisadmin
ln -s serv_config %{buildroot}%{_sbindir}/uspchrp
ln -s serv_config.8 %{buildroot}%{_mandir}/man8/uspchrp.8
rm -f $RPM_BUILD_ROOT%{_sbindir}/snap $RPM_BUILD_ROOT%{_mandir}/man8/snap.8*
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/powerpc-utils
mv $RPM_BUILD_ROOT%{_unitdir}/hcn-init-NetworkManager.service $RPM_BUILD_ROOT%{_unitdir}/hcn-init.service
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post core

%systemd_post hcn-init.service
/usr/sbin/smtstate --save >/dev/null 2>&1 || :
%preun core

%systemd_preun smtstate.service
%systemd_preun hcn-init.service
%postun core

%systemd_postun_with_restart smtstate.service
%systemd_postun_with_restart hcn-init.service 
%posttrans core

systemctl enable hcn-init.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list
%files -n powerpc-utils-core -f %{oreon_filedir}/powerpc-utils-core.list

%changelog

%autochangelog
