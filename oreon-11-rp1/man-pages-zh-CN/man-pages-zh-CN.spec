%global source0_hash 04ec87e2ba0974da4cae772c502c99ab874a672b526be67e47aa5a36aa5366d0
%global origname manpages-zh
Summary:        Chinese Man Pages from Chinese Man Pages Project
Name: man-pages-zh-CN
Version: 1.6.4.5
Release:        1%{?dist}
License: GFDL-1.2-no-invariants-or-later
URL: https://github.com/man-pages-zh/
Source0:        https://github.com/man-pages-zh/%{origname}/archive/v%{version}.tar.gz
BuildArchitectures: noarch
Summary(zh_CN): 中文 man pages
Provides: man-pages-zh_CN = %{version}-%{release}
Requires: man-pages-reader
Supplements: (man-pages and langpacks-zh_CN)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnome-common
BuildRequires:  make
BuildRequires:  opencc-tools
BuildRequires:  python3
# /oreon:deps
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

gnome-autogen.sh
%configure --disable-zhtw
make %{?_smp_mflags}
%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/zh_CN
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm $RPM_BUILD_ROOT%{_datadir}/doc/manpages-zh/COPYRIGHT
%global manDest $RPM_BUILD_ROOT%{_mandir}/zh_CN
rm -f %{manDest}/man1/newgrp.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
