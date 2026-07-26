%global source0_hash 6b567521be1c151323f2059c8feec85ded96b6f184ff80535837fea33798b40b

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%define	name	s3cmd
%define	version	2.4.0
%define	release	11

Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Tool for accessing Amazon Simple Storage Service

License:        GPL-2.0-or-later
URL:            https://s3tools.org/%{name}
Source0:        https://github.com/s3tools/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-dateutil
Requires:       ( python3-magic or python3-file-magic )

# Disable auto dependencies as sources match Python2
%{?python_disable_dependency_generator}
%else
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       python-dateutil
Requires:       python-magic
%else
Requires:       python2-dateutil
Requires:       python2-magic
%endif
%endif

%description
S3cmd lets you copy files from/to Amazon S3
(Simple Storage Service) using a simple to use
command line client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
rm -rf *.egg-info
%if %{without python3}
# Not needed on Py2, RPM fails to Bytecompile it
rm -f S3/Custom_httplib3x.py
%endif

%build
export S3CMD_PACKAGING=1
%if %{with python3}
%py3_build
%else
%py2_build
%endif

%install
export S3CMD_PACKAGING=1
%if %{with python3}
%py3_install
%else
%py2_install
%endif

mkdir -p %{buildroot}%{_mandir}/man1
install -D -p -m 0644 -t %{buildroot}%{_mandir}/man1 %{name}.1

%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%if %{with python3}
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/S3/
%else
%{python2_sitelib}/%{name}-*.egg-info/
%{python2_sitelib}/S3/
%endif

%changelog
%autochangelog
