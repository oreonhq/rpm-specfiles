%global source0_hash 4c6a2f7015977644dddfdbe9dc928c598f5ce25e14bb162b1900cf80b287b48a

%global selinux_variants mls targeted
%global modulename dist_git
%global installdir /var/lib/dist-git

Name:           dist-git
Version:        1.19
Release:        1%{?dist}
Summary:        Package source version control system

# upload.cgi uses GPLv1
License:        MIT AND GPL-1.0-only
URL:            https://github.com/release-engineering/dist-git
# Source is created by
# git clone https://github.com/release-engineering/dist-git.git
# cd dist-git
# tito build --tgz
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  systemd

Requires:       httpd
Requires:       perl(Sys::Syslog)
Requires:       (dist-git-selinux if selinux-policy-targeted)
Requires:       git
Requires:       git-daemon
Requires:       mod_ssl
Requires:       crudini
%if 0%{?rhel} && 0%{?rhel} < 10
Requires(pre):  shadow-utils
%endif

Requires:       python3-requests
Recommends:     python3-grokmirror
Suggests:       python3-fedmsg
Suggests:       fedora-messaging

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-requests

# this should be Requires but see https://bugzilla.redhat.com/show_bug.cgi?id=1833810
Recommends: moreutils

%if 0%{?fedora} && 0%{?fedora} >= 41
# The `cgi` module was removed from the Python 3.13 standard library
BuildRequires:  python3-legacy-cgi
Requires:       python3-legacy-cgi
%endif

%description
DistGit is a Git repository specifically designed to hold RPM
package sources.

%package selinux
Summary:        SELinux support for dist-git

BuildRequires:  checkpolicy
BuildRequires:  hardlink

Requires:       %name = %version-%release
BuildRequires:  selinux-policy-devel
%{?selinux_requires}

%description selinux
Dist Git is a remote Git repository specifically designed to hold RPM
package sources.

This package includes SELinux support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# ------------------------------------------------------------------------------
# SELinux
# ------------------------------------------------------------------------------
cd selinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv %{modulename}.pp %{modulename}.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -

%pre
%if 0%{?rhel} && 0%{?rhel} < 10
# ------------------------------------------------------------------------------
# Users and Groups
# ------------------------------------------------------------------------------
getent group packager > /dev/null || \
    groupadd -r packager
exit 0
%endif

%check
%pytest -vv .

%install
# ------------------------------------------------------------------------------
# /usr/share/ ........... scripts
# ------------------------------------------------------------------------------
install -d %{buildroot}%{_datadir}/dist-git/
cp -a scripts/dist-git/* %{buildroot}%{_datadir}/dist-git/

# ------------------------------------------------------------------------------
# /etc/ .......... config files
# ------------------------------------------------------------------------------
install -d %{buildroot}%{_sysconfdir}/dist-git
cp -a configs/dist-git/dist-git.conf %{buildroot}%{_sysconfdir}/dist-git/
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d/dist-git
mkdir -p   %{buildroot}%{_unitdir}

cp -a configs/httpd/dist-git.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/
cp -a configs/httpd/dist-git/* %{buildroot}%{_sysconfdir}/httpd/conf.d/dist-git/
cp -a configs/systemd/*        %{buildroot}%{_unitdir}/

install -m0644 -D configs/sysusers.d/dist-git.conf %{buildroot}%{_sysusersdir}/dist-git.conf

# ------------------------------------------------------------------------------
# /var/lib/ ...... dynamic persistent files
# ------------------------------------------------------------------------------
install -d %{buildroot}%{installdir}
install -d %{buildroot}%{installdir}/git
install -d %{buildroot}%{installdir}/cache
install -d %{buildroot}%{installdir}/cache/lookaside
install -d %{buildroot}%{installdir}/cache/lookaside/pkgs
install -d %{buildroot}%{installdir}/web

cp -a scripts/httpd/upload.cgi %{buildroot}%{installdir}/web/

%if 0%{?rhel} && 0%{?rhel} < 8
    sed -i '1 s|#.*|#!/usr/bin/python2|' %{buildroot}%{installdir}/web/upload.cgi
%endif

# ------------------------------------------------------------------------------
# /usr/bin/ ...... links to executable files
# ------------------------------------------------------------------------------
install -d %{buildroot}%{_bindir}
ln -s %{_datadir}/dist-git/setup_git_package %{buildroot}%{_bindir}/setup_git_package
ln -s %{_datadir}/dist-git/mkbranch %{buildroot}%{_bindir}/mkbranch
ln -s %{_datadir}/dist-git/mkbranch_branching %{buildroot}%{_bindir}/mkbranch_branching
ln -s %{_datadir}/dist-git/remove_unused_sources %{buildroot}%{_bindir}/remove_unused_sources
mv %{buildroot}%{_datadir}/dist-git/dist-git-gc %{buildroot}%{_bindir}/dist-git-gc

# ------------------------------------------------------------------------------
# SELinux
# ------------------------------------------------------------------------------
cd selinux
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 %{modulename}.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp
done
cd -

hardlink -cv %{buildroot}%{_datadir}/selinux

%post selinux
for selinuxvariant in %{selinux_variants}
do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp &> /dev/null || :
done
%{_sbindir}/restorecon -v %{installdir}/cache || :
%{_sbindir}/restorecon -v %{installdir}/cache/lookaside || :
%{_sbindir}/restorecon -v %{installdir}/cache/lookaside/pkgs || :
%{_sbindir}/restorecon -v %{installdir}/git || :
%{_sbindir}/restorecon -Rv %{installdir}/web/ || :

%systemd_post dist-git.socket

%preun
%systemd_preun dist-git.socket

%postun selinux
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
     /usr/sbin/semodule -s ${selinuxvariant} -r %{modulename} &> /dev/null || :
  done
fi

%systemd_postun dist-git.socket

%files
# ------------------------------------------------------------------------------
# Docs
# ------------------------------------------------------------------------------
%license LICENSE
%doc README.md

# ------------------------------------------------------------------------------
# /etc/ .......... config files
# ------------------------------------------------------------------------------
%dir                   %{_sysconfdir}/dist-git
%config(noreplace)     %{_sysconfdir}/dist-git/dist-git.conf
%dir                   %{_sysconfdir}/httpd/conf.d/dist-git
%config(noreplace)     %{_sysconfdir}/httpd/conf.d/dist-git/*
%config(noreplace)     %{_sysconfdir}/httpd/conf.d/dist-git.conf

%{_unitdir}/dist-git@.service
%{_unitdir}/dist-git.socket
%{_unitdir}/dist-git-gc.service
%{_unitdir}/dist-git-gc.timer

# ------------------------------------------------------------------------------
# /var/lib/ ...... dynamic persistent files
# ------------------------------------------------------------------------------

# non-standard-dir-perm:
# - git repositories and their contents must have w permission for their creators
%dir                              %{installdir}
%attr (2775, -, packager)         %{installdir}/git
%dir                              %{installdir}/web
%attr (755, apache, apache)       %{installdir}/web/upload.cgi
%dir                              %{installdir}/cache
%dir                              %{installdir}/cache/lookaside
%attr (2775, apache, apache)      %{installdir}/cache/lookaside/pkgs

# ------------------------------------------------------------------------------
# /usr/share ...... executable files
# ------------------------------------------------------------------------------

%dir              %{_datadir}/dist-git
%attr (775, -, -) %{_datadir}/dist-git/*
%{_bindir}/dist-git-gc
# TODO: move _datadir executables to _libexecdir, and drop these symlinks
%{_bindir}/mkbranch
%{_bindir}/mkbranch_branching
%{_bindir}/remove_unused_sources
%{_bindir}/setup_git_package

%{_sysusersdir}/dist-git.conf

%files selinux
%doc selinux/*
%{_datadir}/selinux/*/%{modulename}.pp

%changelog
%autochangelog
