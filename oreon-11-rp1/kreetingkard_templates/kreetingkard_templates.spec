%global source0_hash 8ea0c55131904006c5d560d59f5a2c396e5530155fb569c74f428e734c857a87
%define		appname		kreetingkard
%define		mainver		0.2.0
%define		baserelease	11
%define		repoid		18013
Name:		kreetingkard_templates
Version:	%{mainver}
Release:        1%{?dist}
Summary:        Template files for KreetingKard
License:	GPL-1.0-or-later
URL:		http://linux-life.net/program/cc/kde/app/kreetingkard/
Source0:        http://downloads.sourceforge.jp/%{appname}/%{repoid}/%{name}-%{version}.tar.gz
Requires:	%{appname} >= 0.7.1
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
# /oreon:deps
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

echo "Nothing to do here"
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/apps/%{appname}/
%{__cp} -pr templates/ $RPM_BUILD_ROOT%{_datadir}/apps/%{appname}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
