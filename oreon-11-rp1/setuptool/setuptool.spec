%global source0_hash 09092a5955580e4aca3f83f48ff7f4395dd7dc69d0274e300f5393755d0e994b

Name: setuptool
Version: 1.19.11
Release: 33%{?dist}
Summary: A text mode system configuration tool
License: GPL-2.0-or-later
Url: http://git.fedorahosted.org/git/?p=setuptool.git
Source: setuptool-%{version}.tar.gz
BuildRequires: make
BuildRequires: newt-devel, gettext, perl-XML-Parser, glib2-devel, intltool, gcc
Requires: usermode

%description
Setuptool is a user-friendly text mode menu utility which allows you
to access all of the text mode configuration programs included in the
operating system distribution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang setup

%files -f setup.lang
%doc README COPYING
%{_bindir}/setup
%config(noreplace) %{_sysconfdir}/pam.d/setup
%config(noreplace) %{_sysconfdir}/security/console.apps/setup
%{_sbindir}/setup
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/setuptool.d
%dir %{_sysconfdir}/setuptool.d
%config(noreplace) %{_sysconfdir}/setuptool.d/*
%{_mandir}/man1/setup.1.gz

%changelog
%autochangelog
