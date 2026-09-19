%global source0_hash 10e57b6ca5b9a7fdec6d8ed344b26b501ce961436c310491134faa100ecc0261

Name:		srcpd
Version:	2.1.7
Release:	6%{?dist}
Summary:	Simple Railroad Command Protocol (SRCP) server

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://srcpd.sourceforge.net/
Source0:	http://sourceforge.net/projects/srcpd/files/srcpd/%{version}/srcpd-%{version}.tar.bz2
Source1:	srcpd.service

Patch0:		srcpd-2.1.6-io-conditional.patch

BuildRequires:		make
BuildRequires:		gcc
BuildRequires:		libxml2-devel

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd

%description
Simple Railroad Command Protocol (SRCP) is a communication protocol designed
to integrate various models of railroad systems. The srcpd acts a gateway
between any kind of model railway systems and user interface programs that
support SRCP. IANA assigned TCP port 4303 to it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install
%find_lang %{name} --with-man --all-name

install -Dpm 0644 %SOURCE1 %{buildroot}/%{_unitdir}/srcpd.service
rm -rf %{buildroot}/%{_sysconfdir}/udev
install -Dpm 0644 10-liusb.rules %{buildroot}/%{_udevrulesdir}/10-liusb.rules

%post
%systemd_post %{name}.service
exit 0

%preun
%systemd_preun %{name}.service
exit 0

%postun
%systemd_postun_with_restart %{name}.service
exit 0

%files -f %{name}.lang
%doc AUTHORS ChangeLog DESIGN NEWS PROGRAMMING-HOWTO TODO
%doc README README.loconet README.selectrix
%license COPYING
%config(noreplace) %{_sysconfdir}/srcpd.conf
%config(noreplace) %{_udevrulesdir}/10-liusb.rules
%{_unitdir}/%{name}.service
%{_sbindir}/srcpd
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

%changelog
%autochangelog
