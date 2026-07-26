%global source0_hash 0dbb4e1cf6e61f1c5acaf4a5631aea7a16cae988e4876783c5e8ac3c5960d4de

%global htmldir /var/www/yawn
%global apacheconfdir /etc/httpd
%global svnrev 632
%global revdate 20140318
%global ver 0.1.7

Name:           yawn
Version:        0
Release:        0.55.%{revdate}svn%{svnrev}%{?dist}
Summary:        Yet Another WBEM Navigator

License:        LGPL-2.1-or-later
URL:            http://pywbem.github.io/yawn/index.html
# The source for this package was pulled from upstream svn repository.
# Use the following commands to get the archive:
#  svn export -r 632 https://svn.code.sf.net/p/pywbem/code/yawn/trunk/mod_wsgi yawn-20140318
#  tar -cJvf yawn-20140318.tar.xz yawn-20140318
Source0:        %{name}-%{revdate}.tar.xz

Patch0: fix-shebang-lines.patch
Patch1: python-3-support.patch
Patch2: fix-requires.patch

BuildRequires:  httpd, python3-devel
Requires:       python3-mod_wsgi, python3-pywbem, httpd, python3-werkzeug, python3-mako
BuildArch:      noarch

%description
Web-based CIM/WBEM browser

%package server
Summary: Standalone web server for yawn
Requires: %{name}

%description server
Script to run yawn without Apache web server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{revdate}
%autopatch -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
mkdir -p $RPM_BUILD_ROOT%{htmldir}
install ./scripts/yawn.wsgi $RPM_BUILD_ROOT%{htmldir}/index.wsgi
install -d $RPM_BUILD_ROOT%{apacheconfdir}/conf.d/
install -m 0644 ./apache/yawn.conf ${RPM_BUILD_ROOT}/%{apacheconfdir}/conf.d/yawn.conf

%post
/bin/systemctl try-restart httpd.service >/dev/null 2>&1 || :

%files
%{htmldir}
%{python3_sitelib}/pywbem_yawn/
%{python3_sitelib}/yawn-%{ver}.dist-info/
%config(noreplace) %{apacheconfdir}/conf.d/yawn.conf
%doc README Changelog

%files server
%{_bindir}/yawn.py

%changelog
%autochangelog
