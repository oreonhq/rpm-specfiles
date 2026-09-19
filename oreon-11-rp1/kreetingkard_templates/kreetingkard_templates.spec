%global source0_hash 8ea0c55131904006c5d560d59f5a2c396e5530155fb569c74f428e734c857a87

%define		appname		kreetingkard

%define		mainver		0.2.0
%define		baserelease	11
%define		repoid		18013

Name:		kreetingkard_templates
Version:	%{mainver}
Release:	%{baserelease}%{?dist}
Summary:	Template files for KreetingKard

# SPDX confirmed
License:	GPL-1.0-or-later
URL:		http://linux-life.net/program/cc/kde/app/kreetingkard/
Source0:	http://downloads.sourceforge.jp/%{appname}/%{repoid}/%{name}-%{mainver}.tar.gz

BuildRequires:	make
# From Mandriva
Requires:	%{appname} >= 0.7.1

BuildArch:	noarch

%description
KreetingKard is a tool for making Japanese greeting cards. It allows you to 
make greeting cards easily by choosing a template and changing the words.

This package contains some template files for KreetingKard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

find templates/ -name CVS | sort -r | xargs %{__rm} -rf
find templates/ -name Makefile\* -or -name \*.rb | xargs %{__rm} -f

%build
# This package is noarch, however when we set BuildArch as
# noarch, %%configure fails strangefully. So we install the needed files
# manually.
echo "Nothing to do here"

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/apps/%{appname}/
%{__cp} -pr templates/ $RPM_BUILD_ROOT%{_datadir}/apps/%{appname}/

%files
%doc	AUTHORS
%license	COPYING
%doc	README

%{_datadir}/apps/%{appname}/templates/

%changelog
%autochangelog
