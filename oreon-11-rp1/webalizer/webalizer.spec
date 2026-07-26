%global source0_hash edaddb5aa41cc4a081a1500e3fa96615d4b41bc12086bcedf9938018ce79ed8d

%define ver 2.23
%define patchlevel 08

%if 0%{?fedora} < 18 && 0%{?rhel} < 7
%global db_devel  db4-devel
%else
%global db_devel  libdb-devel
%endif

Name: webalizer
Summary: A flexible Web server log file analysis program
Version: 2.23_08
Release: 30%{?dist}
URL: http://www.mrunix.net/webalizer/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: ftp://ftp.mrunix.net/pub/webalizer/%{name}-%{ver}-%{patchlevel}-src.tgz
Source1: webalizer.conf
Source2: webalizer.cron
Source3: webalizer-httpd.conf
Source4: webalizer.sysconfig
Patch4: webalizer-2.21-02-underrun.patch
Patch6: webalizer-2.23-05-confuser.patch
Patch9: webalizer-2.23-05-groupvisit.patch
Patch10: webalizer-2.23-08-memmove.patch
# From Debian
Patch21: 02_fix_a_spelling_error.diff
Patch22: 04_Fix_cast_warnings_in_output.c.diff
Patch23: 14_add_search_engines.diff
Patch24: 17_fix_typo_supress_suppress_in_sample.conf.diff
Patch25: 27_fix_compilation_with_gcc-10.diff
BuildRequires: make
BuildRequires:  gcc
BuildRequires: gd-devel, %{db_devel}, bzip2-devel
BuildRequires: GeoIP-devel
Requires: httpd, crontabs

%description
The Webalizer is a Web server log analysis program. It is designed to
scan Web server log files in various formats and produce usage
statistics in HTML format for viewing through a browser. It produces
professional looking graphs which make analyzing when and where your
Web traffic is coming from easy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{ver}-%{patchlevel}
%patch -P4 -p1 -b .underrun
%patch -P6 -p1 -b .confuser
%patch -P9 -p1 -b .groupvisit
%patch -P10 -p1 -b .memmove
%patch -P21 -p1 -b .spelling_error
%patch -P22 -p1 -b .cast_warnings
%patch -P23 -p1 -b .sample_add_search_engines
%patch -P24 -p1 -b .sample_typo
%patch -P25 -p1 -b .gcc10_common_support

# Create a sysusers.d config file
cat >webalizer.sysusers.conf <<EOF
u webalizer - 'Webalizer' %{_localstatedir}/www/usage -
EOF

%build
#CPPFLAGS="-I%{_includedir}/db4" ; export CPPFLAGS
#CFLAGS="$RPM_OPT_FLAGS $CPPFLAGS -D_GNU_SOURCE" ; export CFLAGS
%configure --enable-dns --enable-bz2 --enable-geoip

%make_build

%install
mkdir -p %{buildroot}%{_localstatedir}/www/usage \
         %{buildroot}%{_sysconfdir}/cron.daily

mkdir -p %{buildroot}%{_localstatedir}/lib/webalizer

%make_install

install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}
install -p -m 644 *.png %{buildroot}%{_localstatedir}/www/usage
install -p -m 755 %{SOURCE2} \
         %{buildroot}%{_sysconfdir}/cron.daily/00webalizer
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -p -m 644 %{SOURCE3} \
        %{buildroot}%{_sysconfdir}/httpd/conf.d/webalizer.conf
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 644 %{SOURCE4} \
        %{buildroot}%{_sysconfdir}/sysconfig/webalizer

rm -f %{buildroot}%{_sysconfdir}/webalizer.conf.sample

install -m0644 -D webalizer.sysusers.conf %{buildroot}%{_sysusersdir}/webalizer.conf

%files
%doc README
%{_mandir}/man1/*.1*
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/webalizer.conf
%{_sysconfdir}/cron.daily/00webalizer
%config(noreplace) %{_sysconfdir}/httpd/conf.d/webalizer.conf
%config(noreplace) %{_sysconfdir}/sysconfig/webalizer
%attr(-, webalizer, root) %dir %{_localstatedir}/www/usage
%attr(-, webalizer, root) %dir %{_localstatedir}/lib/webalizer
%attr(-, webalizer, root) %{_localstatedir}/www/usage/*.png
%{_sysusersdir}/webalizer.conf

%changelog
%autochangelog
