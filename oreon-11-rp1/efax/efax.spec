%global source0_hash 46abddf13f7565ea0c9d85b92845cdb32fb265c47cfc84c972e11a0219cda8ea

Summary: A program for faxing using a Class 1, 2 or 2.0 fax modem
Name: efax
Version: 0.9a
Release: 47.001114%{?dist}
License: GPL-2.0-or-later
Url: http://www.cce.com/efax/
Source: http://www.cce.com/efax/download/%{name}-%{version}-001114.tar.gz
Source1: logrotate-efax
Patch0: efax-0.9-config.patch
Patch1: efax-0.9-numlines.patch
Patch2: efax08a-time.patch
Patch3: efax-0.9-manpage.patch
Patch5: efax-0.9-nullptr.patch
Patch6: efax-0.9-misc.patch
Patch7: efax-0.9-viewcmd.patch
Patch8: efax-0.9-quote.patch
Patch9: efax-0.9-msg-va_list.patch
Patch10: efax-0.9a-001114-crash.patch
Patch11: efax-0.9-pdf.patch
Patch12: efax-0.9a-001114-format-security.patch
Patch13: efax-0.9a-001114-multiple-definition.patch

ExcludeArch: s390 s390x

BuildRequires: make
BuildRequires: gcc

Requires: netpbm-progs

%description
Efax is a small ANSI C/POSIX program that sends and receives faxes
using any Class 1, 2 or 2.0 fax modem.

You need to install efax if you want to send faxes and you have a
Class 1, 2 or 2.0 fax modem.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-001114

%patch -P0 -p1 -b .config
%patch -P1 -p1 -b .numlines
%patch -P2 -p1 -b .time
%patch -P3 -p0 -b .manpage
%patch -P5 -p1 -b .nullptr
%patch -P6 -p1 -b .misc
%patch -P7 -p1 -b .viewcmd
%patch -P8 -p1 -b .quote
%patch -P9 -p1 -b .msg-va_list
%patch -P10 -p1 -b .crash
%patch -P11 -p0 -b .pdf
%patch -P12 -p1 -b .format-security
%patch -P13 -p1 -b .multiple-definition

%build
make %{?_smp_mflags} RPM_OPT_FLAGS="-ansi $RPM_OPT_FLAGS -fno-strict-aliasing"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_localstatedir}/spool/fax
mkdir -p %{buildroot}%{_localstatedir}/log/fax

make BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir} install
mkdir -p %{buildroot}/etc/logrotate.d/
install -c -m 644 %{SOURCE1} %{buildroot}/etc/logrotate.d/efax

%files
%doc README COPYING
%config(noreplace) /etc/logrotate.d/efax
%{_bindir}/*
%{_mandir}/*/*
%dir %{_localstatedir}/spool/fax
%dir %{_localstatedir}/log/fax

%changelog
%autochangelog
