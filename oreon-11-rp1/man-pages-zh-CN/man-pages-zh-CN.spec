%global source0_hash 03ee010e177857ada2f11bb0af374513e742eebf0fb6f985b5de1964876f758e

%global origname manpages-zh

Summary: Chinese Man Pages from Chinese Man Pages Project
Name: man-pages-zh-CN
Version: 1.6.3.6
Release: 13%{?dist}
License: GFDL-1.2-no-invariants-or-later
#Vendor: From CMPP (Chinese Man Pages Project)
URL: https://github.com/man-pages-zh/
Source0: https://github.com/man-pages-zh/%{origname}/archive/v%{version}.tar.gz
BuildArchitectures: noarch
Summary(zh_CN): 中文 man pages

Provides: man-pages-zh_CN = %{version}-%{release}

BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gnome-common
BuildRequires: opencc-tools
BuildRequires: python3
Requires: man-pages-reader
Supplements: (man-pages and langpacks-zh_CN)

%description
manpages-zh is a sub-project from i18n-zh, from the Chinese Man Pages
Project (CMPP). However, the original CMPP seems inactive, nor can the
original home page (cmpp.linuxforum.net) be visited.

This project revives and maintains the remains of CMPP.

So far the simplified Chinese is packed.

%description -l zh_CN
本项目(manpages-zh)为 i18n-zh 的子项目，从 CMPP (中文 Man Pages 计划) 分支而来。
CMPP 项目现在可能已经死亡，原主页(cmpp.linuxforum.net)已不能访问。

本项目的目的是维护 CMPP 遗留下的成果，并对其错误/漏洞进行修改。

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{origname}-%{version}

%build 
# Disable zh_TW, as it requires dependencies only available in Debian.
gnome-autogen.sh
%configure --disable-zhtw
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/zh_CN
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
# Include the COPYRIGHT file in %doc macro
rm $RPM_BUILD_ROOT%{_datadir}/doc/manpages-zh/COPYRIGHT
# Remove file conflict
%global manDest $RPM_BUILD_ROOT%{_mandir}/zh_CN
rm -f %{manDest}/man1/newgrp.1

%files
%doc README NEWS COPYRIGHT
%license COPYING
%{_mandir}/zh_CN/man*/*

%changelog
%autochangelog
