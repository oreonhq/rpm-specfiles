%global source0_hash 701271b9221eadec0f5f4c99a74a3ef4214123222b757d78d62ef73690f7d8e7
%global debug_package %{nil}
%global moduletype services
%global modulenames container
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %1+=" "; done;
%if %{defined copr_username} && "%{copr_username}" == "rhcontainerbot" && "%{copr_projectname}" == "podman-next"
%define next_build 1
%endif
Name: container-selinux
%if %{defined next_build}
Epoch: 102
%else
Epoch: 4
%endif
Version: 2.251.0
Release:        1%{?dist}
License: GPL-2.0-only
URL: https://github.com/containers/%{name}
Summary:        SELinux policies for container runtimes
Source0:        https://github.com/containers/container-selinux/archive/refs/tags/v2.251.0.tar.gz#/container-selinux-2.251.0.tar.gz
BuildArch: noarch
Requires: selinux-policy >= %_selinux_policy_version
Requires(post): selinux-policy-base >= %_selinux_policy_version
Requires(post): selinux-policy-any >= %_selinux_policy_version
Recommends: selinux-policy-targeted >= %_selinux_policy_version
Requires(post): policycoreutils
Requires(post): libselinux-utils
Requires(post): sed
Obsoletes: %{name} <= 2:1.12.5-13
Obsoletes: docker-selinux <= 2:1.12.4-28
Provides: docker-selinux = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts: udica < 0.2.6-1
Conflicts: k3s-selinux <= 0.4-1
# oreon:deps
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
# /oreon:deps
%description
SELinux policy modules for use with container runtimes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git %{name}-%{version}

sed -i 's/^man: install-policy/man:/' Makefile
sed -i 's/^install: man/install:/' Makefile

%if %{defined no_user_namespace}
sed -i '/user_namespace/d' container.te
%endif

%if %{defined legacy_var_run}
sed -i 's|^/run/|/var/run/|' container.fc
%endif

%build

make
%install
%_format MODULES $x.pp.bz2
%{__make} DATADIR=%{buildroot}%{_datadir} SYSCONFDIR=%{buildroot}%{_sysconfdir} install install.udica-templates install.selinux-user
%oreon_autofiles main

%pre

%selinux_relabel_pre
%post

if [ $1 -eq 1 ]; then
   %{_sbindir}/setsebool -P -N virt_use_nfs=1 virt_sandbox_use_all_caps=1
fi
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
. %{_sysconfdir}/selinux/config
%{_sbindir}/semodule -n -s ${SELINUXTYPE} -r container 2> /dev/null
%{_sbindir}/semodule -n -s ${SELINUXTYPE} -d docker 2> /dev/null
%{_sbindir}/semodule -n -s ${SELINUXTYPE} -d gear 2> /dev/null
%selinux_modules_install -s ${SELINUXTYPE} $MODULES
sed -e "\|container_file_t|h; \${x;s|container_file_t||;{g;t};a\\" -e "container_file_t" -e "}" -i /etc/selinux/${SELINUXTYPE}/contexts/customizable_types
matchpathcon -qV %{_sharedstatedir}/containers || restorecon -R %{_sharedstatedir}/containers &> /dev/null || :
%postun

if [ $1 -eq 0 ]; then
   %selinux_modules_uninstall %{modulenames} docker
fi
%posttrans

%selinux_relabel_post
%check

%{!?_licensedir:%global license %doc}
%triggerpostun -- container-selinux < 2:2.162.1-3

if %{_sbindir}/selinuxenabled ; then
    echo "Fixing Rootless SELinux labels in homedir"
    %{_sbindir}/restorecon -R /home/*/.local/share/containers/storage/overlay*  2> /dev/null
fi
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.247.0-1
- Prepare for Oreon 11 (RP1)
