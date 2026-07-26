%global source0_hash 28f9a4f973731c9fc731277f9fc029b5710baafbc682fd288073baa02189644a

%if 0%{?fedora} > 27 || 0%{?rhel} > 7
# Build python3
%global with_python3 1
%global PYTHONDIR %{python3_sitelib}
%else
%global with_python3 0
%global PYTHONDIR %{python2_sitelib}
%endif

Summary: Web page with summary of ABRT services
Name: abrt-server-info-page
Version: 1.8
Release: 25%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://github.com/marusak/abrt-server-info-page
# source is created by:
# git clone
# cd abrt-server-info-page; tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

%if 0%{?with_python3}
BuildRequires: python3-devel
%else
BuildRequires: python2-devel
%endif

%if 0%{?with_python3}
Requires: python3-flask >= 0.10
Requires: python3-mod_wsgi
%else
Requires: python-flask >= 0.10
Requires: mod_wsgi
%endif
Requires: httpd
Requires(post): systemd

%description
Web page for use as front page of ABRT servers. Contains information about
ABRT's products.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%install
sed -i "s|@PYTHONDIR@|%{PYTHONDIR}|g" config/abrt-server-info-page.conf
mkdir -p %{buildroot}
mkdir -p %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/static
mkdir -p %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/static/js
mkdir -p %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/static/css
mkdir -p %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/static/fonts
mkdir -p %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/templates
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
cp -a abrt_server_info_page.py %{buildroot}/%{PYTHONDIR}/abrt-server-info-page
cp -a abrt_server_info_page.wsgi %{buildroot}/%{PYTHONDIR}/abrt-server-info-page
cp -a config.py %{buildroot}/%{PYTHONDIR}/abrt-server-info-page
cp -a config/abrt-server-info-page.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/
cp -a templates/index.html %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/templates
cp -a static/* %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/static

%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/abrt-server-info-page.conf
%{PYTHONDIR}/abrt-server-info-page

%license LICENSE

%post
systemctl condrestart httpd

%changelog
%autochangelog
