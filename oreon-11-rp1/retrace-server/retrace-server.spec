%global source0_hash 1e4d4264f910886d51071839f3f433770f33349beabd4932ac1e45b0f698615b
%define retrace_gid_uid 174
%define retrace_home %{_sharedstatedir}/retrace
Summary:        Application for remote coredump analysis
Name: retrace-server
Version: 1.24.2
Release:        15%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/abrt/retrace-server
Source0:        https://github.com/abrt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: coreutils
Requires: rsync
Requires: mock >= 1.4.7
Requires: xz
Requires: gzip
Requires: bzip2
Requires: tar
Requires: p7zip
Requires: unzip
Requires: lzop
Requires: lsof
Requires: elfutils
Requires: createrepo_c
Requires: procps-ng
Requires: python3-createrepo_c
Requires: python3-mod_wsgi
Requires: python3-webob
Requires: python3-magic
Requires: python3-requests
Requires: python3-requests-gssapi
Requires: python3-bugzilla
Requires: python3-dnf
Requires: python3-hawkey
Requires: mod_ssl
Requires: sqlite
Requires: crash >= 5.1.7
Requires: wget
Requires: kexec-tools
Requires: distribution-gpg-keys
Requires(post): /usr/bin/crontab
Requires(post): /usr/bin/systemctl
Recommends: httpd
Recommends: logrotate
Recommends: rpm
Suggests: podman
Suggests: unar
Obsoletes: abrt-retrace-server < 2.0.3
Provides: abrt-retrace-server = 2.0.3
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  coreutils
BuildRequires:  createrepo_c
BuildRequires:  gettext
BuildRequires:  gzip
BuildRequires:  lsof
BuildRequires:  meson
BuildRequires:  podman
BuildRequires:  procps-ng
BuildRequires:  python3-bugzilla
BuildRequires:  python3-devel
BuildRequires:  python3-dnf
BuildRequires:  python3-magic
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-requests-gssapi
BuildRequires:  tar
BuildRequires:  texinfo
BuildRequires:  xmlto
BuildRequires:  xz
# /oreon:deps
%description
The retrace server provides a coredump analysis and backtrace
generation service over a network using HTTP protocol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Create a sysusers.d config file
cat >retrace-server.sysusers.conf <<EOF
u retrace %{retrace_gid_uid} - %{retrace_home} -
EOF

%build

%meson \
    -Ddocs=enabled \
    %{nil}
%meson_build
%check

%meson_test
%install
%meson_install
find %{buildroot} -name "*.py[co]" -delete
mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}
mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}/kernel
mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}/download
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/retrace
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/pre_start
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/start
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/pre_prepare_debuginfo
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/post_prepare_debuginfo
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/pre_prepare_environment
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/post_prepare_environment
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/pre_retrace
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/post_retrace
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/success
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/fail
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/pre_remove_task
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/post_remove_task
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/pre_clean_task
mkdir -p %{buildroot}%{_libexecdir}/%{name}/hooks/post_clean_task
rm -f %{buildroot}%{_infodir}/dir
%{find_lang} %{name}
install -m0644 -D retrace-server.sysusers.conf %{buildroot}%{_sysusersdir}/retrace-server.conf
%oreon_autofiles main

%post

/usr/sbin/usermod -a -G mock retrace 2> /dev/null || :
if [ "$1" = 2 -a "$(getent passwd retrace | cut -d: -f6)" = "%{_datadir}/%{name}" ]
then
    /usr/bin/systemctl is-active --quiet httpd.service ; httpd_active=$?
    [ "$httpd_active" = 0 ] && /usr/bin/systemctl stop httpd.service
    /usr/sbin/usermod --home %{retrace_home} retrace 2> /dev/null || :
    [ "$httpd_active" = 0 ] && /usr/bin/systemctl start httpd.service
fi
if [ "$1" = 1 ]
then
    %define retrace_crontab_entry0 "# 0 * * * * /usr/bin/retrace-server-cleanup >> /var/log/retrace-server/cleanup_error.log 2>&1"
    %define retrace_crontab_entry1 "# 0 0,12 * * * /usr/bin/retrace-server-reposync fedora 15 i386 >> /var/log/retrace-server/reposync_error.log 2>&1"
    %define retrace_crontab_entry2 "# 0 2,14 * * * /usr/bin/retrace-server-reposync fedora 15 x86_64 >> /var/log/retrace-server/reposync_error.log 2>&1"
    %define retrace_crontab_entry3 "# 0 4,16 * * * /usr/bin/retrace-server-reposync fedora 16 i386 >> /var/log/retrace-server/reposync_error.log 2>&1"
    %define retrace_crontab_entry4 "# 0 6,18 * * * /usr/bin/retrace-server-reposync fedora 16 x86_64 >> /var/log/retrace-server/reposync_error.log 2>&1"
    %define retrace_crontab_entry5 "# 0 8,20 * * * /usr/bin/retrace-server-reposync fedora rawhide i386 >> /var/log/retrace-server/reposync_error.log 2>&1"
    %define retrace_crontab_entry6 "# 0 10,22 * * * /usr/bin/retrace-server-reposync fedora rawhide x86_64 >> /var/log/retrace-server/reposync_error.log 2>&1"
    (crontab -u retrace -l 2> /dev/null; echo %{retrace_crontab_entry0}; \
     echo %{retrace_crontab_entry1}; echo %{retrace_crontab_entry2}; \
     echo %{retrace_crontab_entry3}; echo %{retrace_crontab_entry4}; \
     echo %{retrace_crontab_entry5}; echo %{retrace_crontab_entry6};) | crontab -u retrace - 2> /dev/null
fi
exit 0
%preun

if [ "$1" = 0 ]
then
    (crontab -u retrace -l 2> /dev/null | sed "s,^\([^#].*\)$,#\1,g") | crontab -u retrace - 2> /dev/null
fi
exit 0
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
