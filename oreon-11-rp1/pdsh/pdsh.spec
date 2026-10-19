%global source0_hash a661095ce51dd5fb05e398cf5d0e1d63157123958441f6d3512bcf1a7d25c517
Name: pdsh
Version: 2.36
Release:        1%{?dist}
Summary:        Parallel remote shell program
License: GPL-2.0-or-later
Url: https://github.com/chaos/pdsh/
Source0:        https://github.com/chaos/pdsh/releases/download/pdsh-%{version}/pdsh-%{version}.tar.gz
Requires: pdsh-rcmd
%{!?_with_readline: %{!?_without_readline: %global _with_readline --with-readline}}
%{!?_with_rsh: %{!?_without_rsh: %global _with_rsh --with-rsh}}
%{!?_with_ssh: %{!?_without_ssh: %global _with_ssh --with-ssh}}
%{!?_with_dshgroups: %{!?_without_dshgroups: %global _with_dshgroups --with-dshgroups}}
%{!?_with_netgroup: %{!?_without_netgroup: %global _with_netgroup --with-netgroup}}
%{!?_with_debug: %{!?_without_debug: %global _with_debug --with-debug}}
%{!?_with_nodeupdown: %{!?_without_nodeupdown: %global _with_nodeupdown --with-nodeupdown}}
%{!?_with_genders: %{!?_without_genders: %global _with_genders --with-genders}}
%{!?_with_rms: %{!?_without_rms: %global _without_rms --without-rms}}
%{!?_with_mrsh: %{!?_without_mrsh: %global _without_mrsh --without-mrsh}}
%{!?_with_qshell: %{!?_without_qshell: %global _without_qshell --without-qshell}}
%{!?_with_mqshell: %{!?_without_mqshell: %global _without_mqshell --without-mqshell}}
%{!?_with_xcpu: %{!?_without_xcpu: %global _without_xcpu --without-xcpu}}
%{!?_with_nodeattr: %{!?_without_nodeattr: %global _without_nodeattr --without-nodeattr}}
%{!?_with_machines: %{!?_without_machines: %global _without_machines --without-machines}}
%{!?_with_slurm: %{!?_without_slurm: %global _without_slurm --without-slurm}}
%{!?_with_torque: %{!?_without_torque: %global _without_torque --without-torque}}
%if %{?_with_debug:1}%{!?_with_debug:0}
  %global _enable_debug --enable-debug
%endif
%{?_with_qshell:BuildRequires: qsnetlibs}
%{?_with_mqshell:BuildRequires: qsnetlibs}
%{?_with_nodeupdown:BuildRequires: libnodeupdown-devel}
%{?_with_genders:BuildRequires: libgenders-devel > 1.0}
%{?_with_torque:BuildRequires: torque-devel}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libgenders-devel
BuildRequires:  libnodeupdown-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  readline-devel
# /oreon:deps
%description
Pdsh is a multithreaded remote shell client which executes commands
on multiple remote hosts in parallel.  Pdsh can use several different
remote shell services, including standard "rsh", Kerberos IV, and ssh.

%package qshd
Summary: Remote shell daemon for pdsh/qshell/Elan3
Requires(post):  xinetd
%description qshd
Remote shell service for running Quadrics Elan3 jobs under pdsh.
Sets up Elan capabilities and environment variables needed by Quadrics
MPICH executables.

%package mqshd
Summary: Remote shell daemon for pdsh/mqshell/Elan3
Requires(post):  xinetd
%description mqshd
Remote shell service for running Quadrics Elan3 jobs under pdsh with
mrsh authentication.  Sets up Elan capabilities and environment variables 
needed by Quadrics MPICH executables.

%package   rcmd-rsh
Summary:   Provides bsd rcmd capability to pdsh
Provides:  pdsh-rcmd
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description rcmd-rsh
Pdsh module for bsd rcmd functionality. Note: This module
requires that the pdsh binary be installed setuid root.

%package   rcmd-ssh
Summary:   Provides ssh rcmd capability to pdsh
Provides:  pdsh-rcmd
Requires:  openssh-clients
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description rcmd-ssh
Pdsh module for ssh rcmd functionality.

%package   rcmd-qshell
Summary:   Provides qshell rcmd capability to pdsh
Provides:  pdsh-rcmd
Conflicts: pdsh-rcmd-mqshell
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description rcmd-qshell
Pdsh module for running QsNet MPI jobs. Note: This module
requires that the pdsh binary be installed setuid root.

%package   rcmd-mrsh
Summary:   Provides mrsh rcmd capability to pdsh
Provides:  pdsh-rcmd
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description rcmd-mrsh
Pdsh module for mrsh rcmd functionality.

%package   rcmd-mqshell
Summary:   Provides mqshell rcmd capability to pdsh
Provides:  pdsh-rcmd
Conflicts: pdsh-rcmd-qshell
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description rcmd-mqshell
Pdsh module for mqshell rcmd functionality.

%package   rcmd-xcpu
Summary:   Provides xcpu rcmd capability to pdsh
Provides:  pdsh-xcpu
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description rcmd-xcpu
Pdsh module for xcpu rcmd functionality.

%package   mod-genders
Summary:   Provides libgenders support for pdsh
Requires:  genders >= 1.1
Conflicts: pdsh-mod-nodeattr
Conflicts: pdsh-mod-machines
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description mod-genders
Pdsh module for libgenders functionality.

%package   mod-nodeattr
Summary:   Provides genders support for pdsh using the nodeattr program
Requires:  genders
Conflicts: pdsh-mod-genders
Conflicts: pdsh-mod-machines
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description mod-nodeattr
Pdsh module for genders functionality using the nodeattr program.

%package   mod-nodeupdown
Summary:   Provides libnodeupdown support for pdsh
Requires:  whatsup
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description mod-nodeupdown
Pdsh module providing -v functionality using libnodeupdown.

%package   mod-rms
Summary:   Provides RMS support for pdsh
Requires:  qsrmslibs
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description mod-rms
Pdsh module providing support for gathering the list of target nodes
from an allocated RMS resource.

%package   mod-machines
Summary:   Pdsh module for gathering list of target nodes from a machines file
Conflicts: pdsh-mod-genders
Conflicts: pdsh-mod-nodeattr
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description mod-machines
Pdsh module for gathering list of all target nodes from a machines file.

%package   mod-dshgroup
Summary:   Provides dsh-style group file support for pdsh
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description mod-dshgroup
Pdsh module providing dsh (Dancer's shell) style "group" file support.
Provides -g groupname and -X groupname options to pdsh.

%package   mod-netgroup
Summary:   Provides netgroup support for pdsh
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description mod-netgroup
Pdsh module providing support for targeting hosts based on netgroup.
Provides -g groupname and -X groupname options to pdsh.

%package   mod-slurm
Summary:   Provides support for running pdsh under SLURM allocations
Requires:  slurm
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description mod-slurm
Pdsh module providing support for gathering the list of target nodes
from an allocated SLURM job.

%package   mod-torque
Summary:   Provides support for running pdsh under Torque jobid
Requires:  torque
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description mod-torque
Pdsh module providing support for running pdsh on Torque nodes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
chmod +x configure

%build

%configure \
    %{?_enable_debug}       \
    %{?_with_rsh}           \
    %{?_without_rsh}        \
    %{?_with_ssh}           \
    %{?_without_ssh}        \
    %{?_with_qshell}        \
    %{?_without_qshell}     \
    %{?_with_readline}      \
    %{?_without_readline}   \
    %{?_with_machines}      \
    %{?_without_machines}   \
    %{?_with_genders}       \
    %{?_without_genders}    \
    %{?_with_rms}           \
    %{?_without_rms}        \
    %{?_with_nodeupdown}    \
    %{?_without_nodeupdown} \
    %{?_with_nodeattr}      \
    %{?_without_nodeattr}   \
    %{?_with_mrsh}          \
    %{?_without_mrsh}       \
    %{?_with_mqshell}       \
    %{?_without_mqshell}    \
    %{?_with_xcpu}          \
    %{?_without_xcpu}       \
    %{?_with_slurm}         \
    %{?_without_slurm}      \
    %{?_with_dshgroups}     \
    %{?_without_dshgroups}  \
    %{?_with_netgroup}      \
    %{?_without_netgroup}   \
    %{?_with_torque}        \
    %{?_without_torque}
make CFLAGS="$RPM_OPT_FLAGS"
%install
mkdir -p $RPM_BUILD_ROOT
DESTDIR="$RPM_BUILD_ROOT" make install
if [ -x $RPM_BUILD_ROOT/%{_sbindir}/in.qshd ]; then
   install -D -m644 etc/qshell.xinetd $RPM_BUILD_ROOT/%{_sysconfdir}/xinetd.d/qshell
fi
if [ -x $RPM_BUILD_ROOT/%{_sbindir}/in.mqshd ]; then
   install -D -m644 etc/mqshell.xinetd $RPM_BUILD_ROOT/%{_sysconfdir}/xinetd.d/mqshell
fi
rm $RPM_BUILD_ROOT/%{_libdir}/pdsh/*a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post qshd

if ! grep "^qshell" /etc/services >/dev/null; then
  echo "qshell            523/tcp                  # pdsh/qshell/elan3" >>/etc/services
fi
%{_initrddir}/xinetd reload
%endif
%if %{?_with_mqshell:1}%{!?_with_mqshell:0}
%post mqshd

if ! grep "^mqshell" /etc/services >/dev/null; then
  echo "mqshell         21234/tcp                  # pdsh/mqshell/elan3" >>/etc/services
fi
%{_initrddir}/xinetd reload
%endif
%files -f %{oreon_filedir}/main.list
%files -n pdsh-qshd -f %{oreon_filedir}/pdsh-qshd.list
%files -n pdsh-mqshd -f %{oreon_filedir}/pdsh-mqshd.list
%files -n pdsh-rcmd-rsh -f %{oreon_filedir}/pdsh-rcmd-rsh.list
%files -n pdsh-rcmd-ssh -f %{oreon_filedir}/pdsh-rcmd-ssh.list
%files -n pdsh-rcmd-qshell -f %{oreon_filedir}/pdsh-rcmd-qshell.list
%files -n pdsh-rcmd-mrsh -f %{oreon_filedir}/pdsh-rcmd-mrsh.list
%files -n pdsh-rcmd-mqshell -f %{oreon_filedir}/pdsh-rcmd-mqshell.list
%files -n pdsh-rcmd-xcpu -f %{oreon_filedir}/pdsh-rcmd-xcpu.list
%files -n pdsh-mod-genders -f %{oreon_filedir}/pdsh-mod-genders.list
%files -n pdsh-mod-nodeattr -f %{oreon_filedir}/pdsh-mod-nodeattr.list
%files -n pdsh-mod-nodeupdown -f %{oreon_filedir}/pdsh-mod-nodeupdown.list
%files -n pdsh-mod-rms -f %{oreon_filedir}/pdsh-mod-rms.list
%files -n pdsh-mod-machines -f %{oreon_filedir}/pdsh-mod-machines.list
%files -n pdsh-mod-dshgroup -f %{oreon_filedir}/pdsh-mod-dshgroup.list
%files -n pdsh-mod-netgroup -f %{oreon_filedir}/pdsh-mod-netgroup.list
%files -n pdsh-mod-slurm -f %{oreon_filedir}/pdsh-mod-slurm.list
%files -n pdsh-mod-torque -f %{oreon_filedir}/pdsh-mod-torque.list

%changelog

%autochangelog
