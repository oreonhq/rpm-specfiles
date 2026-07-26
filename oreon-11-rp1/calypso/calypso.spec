%global source0_hash 0d1b667a8b3c87cb9ee0903ccd8e4f3b179f2e24a6f13e393e4a537bd1b48121

%global commit 7317d88263fb9658cd7f1174c6bbcfb0a7ae856a
%global shortcommit %%(c=%{commit}; echo ${c:0:7})
%global date 20190429

%bcond check 0

Name: calypso
Version: 2.0
Release: 0.26.%{date}git%{shortcommit}%{?dist}
Summary: Free and open-source CalDAV calendar server
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://keithp.com/blogs/calypso/
Source0: %{name}-%{commit}.tar.xz
Source1: %{name}-mktarball.sh
Source2: %{name}.config
Source3: %{name}.pam
Source4: %{name}.systemd
# fix python-daemon dependency name
Patch0: %{name}-daemon.patch
BuildRequires: python3-devel
BuildRequires: systemd-rpm-macros
%if %{with check}
BuildRequires: git-core
BuildRequires: python3-iniparse
BuildRequires: python3-pytest
%endif
Requires(post): git-core
Requires: git-core
Requires: python3-lockfile
Recommends: python3-kerberos
BuildArch: noarch

%description
Calypso is a python-based CalDAV/CardDAV server that started as a few small
patches to Radicale but was eventually split off as a separate project.

* Uses vObject for parsing and generating the data files
* Stores one event/contact per file
* Uses git to retain a history of the database

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

# Create a sysusers.d config file
cat >calypso.sysusers.conf <<EOF
u calypso - 'CalDAV/CardDAV server with git storage' %{_sharedstatedir}/calypso -
EOF

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l calypso
mkdir -p %{buildroot}%{_sharedstatedir}/calypso
install -Dpm644 calypso.1 %{buildroot}%{_mandir}/man1/calypso.1
install -Dpm644 %{S:2} %{buildroot}%{_sysconfdir}/calypso/config
install -Dpm644 %{S:3} %{buildroot}%{_sysconfdir}/pam.d/calypso
install -Dpm644 %{S:4} %{buildroot}%{_unitdir}/calypso.service

install -m0644 -D calypso.sysusers.conf %{buildroot}%{_sysusersdir}/calypso.conf

%if %{with check}
%check
%pyproject_check_import -t
%pytest
%endif

%preun
%systemd_preun calypso.service

%post
%systemd_post calypso.service
if [ $1 -eq 1 ] && ! [ -d %{_sharedstatedir}/calypso/default ]; then
    mkdir -p %{_sharedstatedir}/calypso/default
    pushd %{_sharedstatedir}/calypso/default
    cat > .calypso-collection << EOF
[collection]
is-calendar = 1
EOF
    git add .calypso-collection
    git commit -m'initialize new default calendar'
    popd
fi

%postun
%systemd_postun_with_restart calypso.service

%files -f %{pyproject_files}
%doc README collection-config config
%dir %attr(0750,root,calypso) %{_sysconfdir}/calypso
%config(noreplace) %{_sysconfdir}/calypso/config
%config(noreplace) %{_sysconfdir}/pam.d/calypso
%{_bindir}/calypso
%{_mandir}/man1/calypso.1*
%{_unitdir}/calypso.service
%dir %attr(0750,calypso,calypso) %{_sharedstatedir}/calypso
%{_sysusersdir}/calypso.conf

%changelog
%autochangelog
