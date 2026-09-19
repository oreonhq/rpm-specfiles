%global source0_hash 2921fc96d4ca676190d6ffd45fa80e107c1fe12291c0c4f64827c29639863332

Name:		openrdate
Version:	1.2
Release:	32%{?dist}
Summary:	Good-old rdate date and time-setting software
# Automatically converted from old format: BSD and BSD with advertising - review is highly recommended.
License:	LicenseRef-Callaway-BSD AND LicenseRef-Callaway-BSD-with-advertising
URL:		http://sourceforge.net/projects/openrdate
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# openrdate-1.2-1 replaces rdate-1.4-24, which does not have active upstream
Provides:	rdate = %{version}-%{release}
Obsoletes:	rdate < 1.4-25

BuildRequires: make
BuildRequires:  gcc

Patch0:openrdate_sysctl.patch
%description
Good-old date- and time-setting rdate software implementing RFC 868
(inetd time) and RFC 2030 (SNTP/NTP) protocols. An independent package
of OpenBSD's rdate program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/rdate
%{_mandir}/man8/rdate.8*

%changelog
%autochangelog
