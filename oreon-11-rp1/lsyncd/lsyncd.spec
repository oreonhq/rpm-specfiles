%global source0_hash 501f70368da8c43d3da81bf9bbb22f43dfcbc9f96b03c745842f326723c091c7

%global _hardened_build 1
%global gittag0 v2.3.1
%global commit0 6d59f16140468242fe157b4a5adf36d6a93cf6a4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:		lsyncd
Version:	2.3.1
Release:	10%{?dist}
Summary:	File change monitoring and synchronization daemon
License:	GPL-2.0-or-later AND CC-BY-3.0
URL:		https://axkibe.github.io/lsyncd/
Source0:	https://github.com/axkibe/%{name}/archive/%{gittag0}/%{name}-%{version}.tar.gz

Patch0:		cmake-DOCDIR.patch

Source1:	lsyncd.sysconfig
Source2:	lsyncd.logrotate
Source3:	lsyncd.conf
Source4:	lsyncd.service
Source5:	lsyncd.sysctl

BuildRequires:	asciidoc
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	lua
BuildRequires:	lua-devel >= 5.2
BuildRequires:	systemd-rpm-macros
Requires:	lua
Requires:	rsync

%description
Lsyncd watches a local directory trees event monitor interface (inotify).
It aggregates and combines events for a few seconds and then spawns one
(or more) process(es) to synchronize the changes. By default this is
rsync.

Lsyncd is thus a light-weight live mirror solution that is comparatively
easy to install not requiring new file systems or block devices and does
not hamper local file system performance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_MANDIR:PATH=%{_mandir} -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}
%cmake_build

%install
%cmake_install
install -p -d -m 0755 %{buildroot}%{_var}/log/%{name}
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/lsyncd
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/lsyncd
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/lsyncd.conf
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/lsyncd.service
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_sysctldir}/50-lsyncd.conf

%check
%ctest

%post
%sysctl_apply 50-lsyncd.conf
%systemd_post lsyncd.service

%preun
%systemd_preun lsyncd.service

%postun
%systemd_postun_with_restart lsyncd.service

%files
%license COPYING
%doc ChangeLog examples README.md
%doc %{_mandir}/man1/lsyncd.1.*
%config(noreplace) %{_sysconfdir}/lsyncd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/lsyncd
%config(noreplace) %{_sysconfdir}/logrotate.d/lsyncd
%{_sysctldir}/50-lsyncd.conf
%{_bindir}/lsyncd
%dir %{_var}/log/%{name}
%{_unitdir}/lsyncd.service

%changelog
%autochangelog
