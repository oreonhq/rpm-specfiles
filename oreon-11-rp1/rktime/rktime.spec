%global source0_hash e6a9936cbd4d8d4cd80fd09e11b8d951316a56c36ddda37b63c38b473293c83a
Name:		rktime
Version:	0.6
Release:        1%{?dist}
Summary:        Multi-zone time display utility
License:	GPL-2.0-only
URL:		http://people.redhat.com/rkeech/#rktime
Source0:        http://people.redhat.com/rkeech/%{name}-%{version}.tgz
BuildArch:	noarch
# oreon:deps

# /oreon:deps
%description
A command-line utility which displays the time
in multiple timezones in an easy-to-read way, using color
to help indicate which locations are currently in business
hours.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -Dp -m0755 rktime $RPM_BUILD_ROOT%{_bindir}/rktime
%{__install} -Dp -m0644 rktime.1 $RPM_BUILD_ROOT%{_mandir}/man1/rktime.1
%{__install} -Dp -m0644 rktime.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5/rktime.conf.5
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
