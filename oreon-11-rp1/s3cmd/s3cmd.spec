%global source0_hash 6b567521be1c151323f2059c8feec85ded96b6f184ff80535837fea33798b40b
%bcond_without python3
%define	name	s3cmd
%define	version	2.4.0
%define	release	11
Name:           %{name}
Version:        %{version}
Release:        1%{?dist}
Summary:        Tool for accessing Amazon Simple Storage Service
License:        GPL-2.0-or-later
URL:            https://s3tools.org/%{name}
Source0:        https://github.com/s3tools/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%if %{with python3}
Requires:       python3-dateutil
Requires:       ( python3-magic or python3-file-magic )
%{?python_disable_dependency_generator}
%else
Requires:       python2-dateutil
Requires:       python2-magic
%endif
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
