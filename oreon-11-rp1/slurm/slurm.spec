%global source0_hash 035f4b193d4de979ba5381beca206a50b6b886b2793b06f68a1ce7e67022b06a
%global ups_rel 1
%if "%{ups_rel}" == "1"
%global name_version %{name}-%{version}
%else
%global name_version %{name}-%{version}-%{ups_rel}
%endif
%ifarch aarch64 ppc64le x86_64
%bcond_without ucx
%else
%bcond_with ucx
%endif
Name:           slurm
Version:        26.05.4
Release:        1%{?dist}
Summary:        Simple Linux Utility for Resource Management
License:        GPL-2.0-or-later AND BSD-2-Clause AND BSD-1-Clause
URL:            https://slurm.schedmd.com/
Source0:        https://download.schedmd.com/%{name}/%{name_version}.tar.bz2
Source1:        slurm.conf
Source2:        slurmdbd.conf
Source3:        slurm-sview.desktop
Source4:        slurm-128x128.png
Source5:        slurm-setuser.in
Patch0:         slurm_release_version.patch
Patch11:        slurm_html_doc_path.patch
Patch12:        slurm_perlapi_rpaths.patch
Patch13:        slurm-24.05.2-perlapi_vendor_installpath.patch
ExcludeArch:    armv7hl
ExcludeArch:    i686
Requires:       /bin/mailx
Requires:       munge
Requires:       pmix
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freeipmi-devel
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  hdf5-devel
BuildRequires:  http-parser-devel
BuildRequires:  hwloc-devel
BuildRequires:  json-c-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjwt-devel
BuildRequires:  libssh2-devel
BuildRequires:  libyaml-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  man2html
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  munge-devel
BuildRequires:  pam-devel
BuildRequires:  perl-ExtUtils-MakeMaker
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pmix-devel
BuildRequires:  python3
BuildRequires:  rdma-core-devel
BuildRequires:  readline-devel
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
Slurm is an open source, fault-tolerant, and highly scalable
cluster management and job scheduling system for Linux clusters.
Components include machine status, partition management,
job management, scheduling and accounting modules.

# -------------
# Base Packages
# -------------

%package devel
Summary: Development package for Slurm
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development package for Slurm.  This package includes the header files
and libraries for the Slurm API.

%package doc
Summary: Slurm documentation
%description doc
Documentation package for Slurm.  Includes documentation and
html-based configuration tools for Slurm.

%package gui
Summary: Slurm gui and visual tools
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gui
This package contains the Slurm visual tool sview and
its respective man pages.

%package libs
Summary: Slurm shared libraries
%description libs
Slurm shared libraries.

%package slurmctld
Summary: Slurm controller daemon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description slurmctld
Slurm controller daemon. Used to manage the job queue, schedule jobs,
and dispatch RPC messages to the slurmd processon the compute nodes
to launch jobs.

%package slurmd
Summary: Slurm compute node daemon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description slurmd
Slurm compute node daemon. Used to launch jobs on compute nodes

%package slurmdbd
Summary: Slurm database daemon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description slurmdbd
Slurm database daemon. Used to accept and process database RPCs and upload
database changes to slurmctld daemons on each cluster.

%package slurmrestd
Summary: Slurm REST API deamon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description slurmrestd
Slurm REST API daemon.  The slurmrestd daemon is designed to allow clients
to communicate with Slurm via a REST API.

%package sackd
Summary: Slurm Auth and Cred Kiosk daemon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description sackd
Slurm Auth and Cred Kiosk daemon. It can be used on login nodes that are not
running slurmd daemons to allow authentication to the cluster.

# -----------------
# Contribs Packages
# -----------------

%package contribs
Summary: Perl tools to print Slurm job state information
Requires: %{name}-perlapi%{?_isa} = %{version}-%{release}
%description contribs
Slurm contribution package which includes the programs seff,
sjobexitmod, sjstat and smail.  See their respective man pages
for more information.

%package nss_slurm
Summary: NSS plugin for slurm
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description nss_slurm
nss_slurm is an optional NSS plugin that can permit passwd and group resolution
for a job on the compute node to be serviced through the local slurmstepd
process, rather than through some alternate network-based service such as LDAP,
SSSD, or NSLCD.

%package openlava
Summary: Openlava/LSF wrappers for transition from OpenLava/LSF to Slurm
Requires: %{name}-perlapi%{?_isa} = %{version}-%{release}
%description openlava
OpenLava wrapper scripts used for helping migrate from OpenLava/LSF to Slurm.

%package pam_slurm
Summary: PAM module for restricting access to compute nodes via Slurm
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description pam_slurm
This module restricts access to compute nodes in a cluster where Slurm
is in use.  Access is granted to root, any user with a Slurm-launched job
currently running on the node, or any user who has allocated resources
on the node according to Slurm.

%package perlapi
Summary: Perl API to Slurm
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description perlapi
Perl API package for Slurm.  This package includes the perl API to provide a
helpful interface to Slurm through Perl.

%package torque
Summary: Torque/PBS wrappers for transition from Torque/PBS to Slurm
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-perlapi%{?_isa} = %{version}-%{release}
%description torque
Torque wrapper scripts used for helping migrate from Torque/PBS to Slurm.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name_version}
cp %SOURCE1 etc/slurm.conf
cp %SOURCE1 etc/slurm.conf.example
cp %SOURCE2 etc/slurmdbd.conf
cp %SOURCE2 etc/slurmdbd.conf.example
mkdir -p share/applications
mkdir -p share/icons/hicolor/128x128/apps
cp %SOURCE3 share/applications/%{name}-sview.desktop
cp %SOURCE4 share/icons/hicolor/128x128/apps/%{name}.png
mkdir -p extras
cp %SOURCE5 extras/%{name}-setuser.in

%build

aclocal -I auxdir
autoconf
automake --no-force
export CFLAGS="%{build_cflags} -fcommon"
export LDFLAGS="%{build_ldflags} -Wl,-z,lazy"
%configure \
  --sysconfdir=%{_sysconfdir}/%{name} \
  --with-pam_dir=%{_libdir}/security \
  --enable-pam \
  --enable-really-no-cray \
  --enable-shared \
  --enable-x11 \
  --disable-static \
  --disable-debug \
  --disable-salloc-background \
  --disable-partial_attach \
  --with-oneapi=no \
  --with-pmix=%{_prefix} \
  --with-shared-libslurm \
  --without-rpath
sed -i 's|^hardcode_into_libs=.*|hardcode_into_libs=no|g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -r '
s|^dir_conf=.*|dir_conf="%{_sysconfdir}/%{name}"|g;
s|^dir_log=.*|dir_log="%{_var}/log/%{name}"|g;
s|^dir_run=.*|dir_run="%{_rundir}/%{name}"|g;
s|^dir_spool=.*|dir_spool="%{_var}/spool/%{name}"|g;
s|^dir_tmpfiles_d=.*|dir_tmpfiles_d="%{_tmpfilesdir}"|g;' \
    extras/%{name}-setuser.in > extras/%{name}-setuser
sed -i 's|"PluginDir=" SLURM_PREFIX "/lib/slurm/\\n"|"PluginDir=%{buildroot}%{_libdir}/%{name}/\\n"|g' testsuite/slurm_unit/common/serializer-test.c
%make_build
%make_build contrib
%install
%make_install
%make_build DESTDIR=%{buildroot} install-contrib
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 -p etc/cgroup.conf.example \
    %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -p etc/cgroup.conf.example \
    %{buildroot}%{_sysconfdir}/%{name}/cgroup.conf
install -m 0644 -p etc/slurm.conf %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -p etc/slurm.conf.example %{buildroot}%{_sysconfdir}/%{name}
install -m 0600 -p etc/slurmdbd.conf %{buildroot}%{_sysconfdir}/%{name}
install -m 0600 -p etc/slurmdbd.conf.example %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -p etc/slurmctld.service %{buildroot}%{_unitdir}
install -m 0644 -p etc/slurmd.service %{buildroot}%{_unitdir}
install -m 0644 -p etc/slurmdbd.service %{buildroot}%{_unitdir}
install -m 0644 -p etc/slurmrestd.service %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
cat  >%{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
D %{_rundir}/%{name} 0755 root root -
EOF
install -d -m 0755 %{buildroot}%{_var}/log/%{name}
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
cat >%{buildroot}%{_sysconfdir}/logrotate.d/%{name} <<EOF
%{_var}/log/%{name}/*.log {
    missingok
    notifempty
    copytruncate
    rotate 5
}
EOF
install -d -m 0755 %{buildroot}%{_rundir}/%{name}
install -d -m 0755 %{buildroot}%{_var}/spool/%{name}/ctld
install -d -m 0755 %{buildroot}%{_var}/spool/%{name}/d
touch %{buildroot}%{_rundir}/%{name}/slurmctld.pid
touch %{buildroot}%{_rundir}/%{name}/slurmd.pid
touch %{buildroot}%{_rundir}/%{name}/slurmdbd.pid
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    share/applications/%{name}-sview.desktop
install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -m 0644 share/icons/hicolor/128x128/apps/%{name}.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -m 0755 extras/%{name}-setuser \
    %{buildroot}%{_bindir}/%{name}-setuser
install -m 0755 contribs/sjstat %{buildroot}%{_bindir}/sjstat
chmod 0755 %{buildroot}%{perl_vendorarch}/auto/Slurm/Slurm.so
chmod 0755 %{buildroot}%{perl_vendorarch}/auto/Slurmdb/Slurmdb.so
for prog in sjobexitmod sjstat mpiexec pbsnodes qalter qdel qhold qrerun qrls \
    qstat qsub bjobs bkill bsub lsid
do
    rm -f %{buildroot}%{_mandir}/man1/${prog}.1
    pod2man %{buildroot}%{_bindir}/${prog} > %{buildroot}%{_mandir}/man1/${prog}.1
done
install -d -m 0755 %{buildroot}%{_docdir}/%{name}/contribs/lua
install -m 0644 contribs/README %{buildroot}%{_docdir}/%{name}/contribs
install -m 0644 contribs/lua/*.lua %{buildroot}%{_docdir}/%{name}/contribs/lua
find %{buildroot} -name \*.a -o -name \*.la | xargs rm -f
rm -rf %{buildroot}%{_libdir}/libslurmfull.so
rm -rf %{buildroot}%{_libdir}/libslurm_pmi.so
rm -f %{buildroot}%{_libdir}/%{name}/auth_none.so
rm -f %{buildroot}%{_libdir}/%{name}/job_submit_defaults.so
rm -f %{buildroot}%{_libdir}/%{name}/job_submit_logging.so
rm -f %{buildroot}%{_libdir}/%{name}/job_submit_partition.so
rm -f %{buildroot}%{_libdir}/%{name}/*datawarp*.so
rm -f %{buildroot}%{_libdir}/%{name}/*cray*.so
rm -f %{buildroot}%{_mandir}/man5/cray*
rm -f %{buildroot}%{_sbindir}/capmc*
rm -f %{buildroot}%{_sbindir}/slurmsmwd*
rm -f %{buildroot}%{perl_vendorarch}/auto/Slurm*/.packlist
rm -f %{buildroot}%{perl_vendorarch}/auto/Slurm*/Slurm*.bs
rm -f %{buildroot}%{perl_archlib}/perllocal.pod
rm -f %{buildroot}%{_libdir}/%{name}/site_factor_example.so
%ldconfig_scriptlets devel
%ldconfig_scriptlets libs
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build LD_LIBRARY_PATH="%{buildroot}%{_libdir}" check
%post slurmctld

%systemd_post slurmctld.service
%preun slurmctld

%systemd_preun slurmctld.service
%postun slurmctld

%systemd_postun_with_restart slurmctld.service
%post slurmd

%systemd_post slurmd.service
%preun slurmd

%systemd_preun slurmd.service
%postun slurmd

%systemd_postun_with_restart slurmd.service
%post slurmdbd

%systemd_post slurmdbd.service
%preun slurmdbd

%systemd_preun slurmdbd.service
%postun slurmdbd

%systemd_postun_with_restart slurmdbd.service
%files -f %{oreon_filedir}/main.list
%files -n slurm-devel -f %{oreon_filedir}/slurm-devel.list
%files -n slurm-doc -f %{oreon_filedir}/slurm-doc.list
%files -n slurm-gui -f %{oreon_filedir}/slurm-gui.list
%files -n slurm-libs -f %{oreon_filedir}/slurm-libs.list
%files -n slurm-slurmctld -f %{oreon_filedir}/slurm-slurmctld.list
%files -n slurm-slurmd -f %{oreon_filedir}/slurm-slurmd.list
%files -n slurm-slurmdbd -f %{oreon_filedir}/slurm-slurmdbd.list
%files -n slurm-slurmrestd -f %{oreon_filedir}/slurm-slurmrestd.list
%files -n slurm-sackd -f %{oreon_filedir}/slurm-sackd.list
%files -n slurm-contribs -f %{oreon_filedir}/slurm-contribs.list
%files -n slurm-nss_slurm -f %{oreon_filedir}/slurm-nss_slurm.list
%files -n slurm-openlava -f %{oreon_filedir}/slurm-openlava.list
%files -n slurm-pam_slurm -f %{oreon_filedir}/slurm-pam_slurm.list
%files -n slurm-perlapi -f %{oreon_filedir}/slurm-perlapi.list
%files -n slurm-torque -f %{oreon_filedir}/slurm-torque.list

%changelog

%autochangelog
