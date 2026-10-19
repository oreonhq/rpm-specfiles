%global source0_hash none
Name:           akmods
Version:        0.6.2
Release:        1%{?dist}
Summary:        Automatic kmods build and install tool
License:        MIT
URL:            http://rpmfusion.org/Packaging/KernelModules/Akmods
Source0:        95-akmods.preset
Source1:        akmods
Source2:        akmodsbuild
Source3:        akmods.h2m
Source6:        akmods.service
Source7:        akmods-shutdown
Source8:        akmods-shutdown.service
Source9:        README
Source10:       LICENSE
Source11:       akmods@.service
Source12:       akmods-ostree-post
Source13:       95-akmodsposttrans.install
Source14:       akmods.log
Source15:       README.secureboot
Source16:       cacert.config.in
Source17:       akmods-kmodgenca
Source18:       akmods-keygen.target
Source19:       akmods-keygen@.service
Source20:       %{name}-tmpfiles.conf
Source21:       akmods.sysusers.conf
BuildArch:      noarch
%{?sysusers_requires_compat}
Requires:       %{_bindir}/flock
Requires:       %{_bindir}/time
Requires:       %{_bindir}/rpmdev-vercmp
Requires:       kmodtool >= 1.1-1
Requires:       openssl
Requires:       bzip2 coreutils diffutils file findutils gawk gcc grep
Requires:       gzip make sed tar unzip util-linux rpm-build
Requires:       kernel-devel-uname-r
Suggests:       (kernel-debug-devel if kernel-debug-core)
Suggests:       (kernel-devel if kernel-core)
Suggests:       (kernel-rt-devel if kernel-rt)
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: pkgconfig(libelf)
# oreon:deps
BuildRequires:  help2man
BuildRequires:  systemd
# /oreon:deps
%description
Akmods startup script will rebuild akmod packages during system
boot, while its background daemon will build them for kernels right
after they were installed.

%prep

%setup -q -c -T
cp -p %{SOURCE9} %{SOURCE10} %{SOURCE15} .

%build

%install
mkdir -p %{buildroot}%{_usrsrc}/%{name} \
         %{buildroot}%{_sbindir} \
         %{buildroot}%{_sysconfdir}/rpm \
         %{buildroot}%{_sysconfdir}/pki/%{name}/certs \
         %{buildroot}%{_sysconfdir}/pki/%{name}/private \
         %{buildroot}%{_sysconfdir}/kernel/postinst.d \
         %{buildroot}%{_sysconfdir}/logrotate.d \
         %{buildroot}%{_localstatedir}/cache/%{name} \
         %{buildroot}%{_localstatedir}/log/%{name} \
         %{buildroot}%{_tmpfilesdir}
install -pm 0755 %{SOURCE1} %{buildroot}%{_sbindir}/
install -pm 0755 %{SOURCE2} %{buildroot}%{_sbindir}/
install -pm 0755 %{SOURCE12} %{buildroot}%{_sbindir}/
install -pm 0644 %{SOURCE14} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -pm 0640 %{SOURCE16} %{buildroot}%{_sysconfdir}/pki/%{name}/
install -pm 0755 %{SOURCE17} %{buildroot}%{_sbindir}/kmodgenca
install -pm 0644 %{SOURCE20} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -dpm 0770 %{buildroot}%{_rundir}/%{name}/
mkdir -p %{buildroot}%{_prefix}/lib/kernel/install.d
install -pm 0755 %{SOURCE13} %{buildroot}%{_prefix}/lib/kernel/install.d/
mkdir -p \
         %{buildroot}%{_unitdir} \
         %{buildroot}%{_presetdir}
install -pm 0644 %{SOURCE0} %{buildroot}%{_presetdir}/
install -pm 0644 %{SOURCE6} %{buildroot}%{_unitdir}/
install -pm 0755 %{SOURCE7} %{buildroot}%{_sbindir}/
install -pm 0644 %{SOURCE8} %{buildroot}%{_unitdir}/
install -pm 0644 %{SOURCE11} %{buildroot}%{_unitdir}/
install -pm 0644 %{SOURCE18} %{buildroot}%{_unitdir}/
install -pm 0644 %{SOURCE19} %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -i %{SOURCE3} -s 1 \
    -o %{buildroot}%{_mandir}/man1/akmods.1 \
       %{buildroot}%{_sbindir}/akmods
help2man -N -i %{SOURCE3} -s 1 \
    -o %{buildroot}%{_mandir}/man1/akmodsbuild.1 \
       %{buildroot}%{_sbindir}/akmodsbuild
install -m0644 -D %{SOURCE21} %{buildroot}%{_sysusersdir}/akmods.conf
%oreon_autofiles main

%pre

%sysusers_create_compat %{SOURCE21}
%post

%systemd_post akmods.service
%systemd_post akmods@.service
%systemd_post akmods-shutdown.service
%preun

%systemd_preun akmods.service
%systemd_preun akmods@.service
%systemd_preun akmods-shutdown.service
%postun

%systemd_postun akmods.service
%systemd_postun akmods@.service
%systemd_postun akmods-shutdown.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
