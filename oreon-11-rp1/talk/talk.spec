%global source0_hash d8f614e8d4d7981a0adf0f84d2d3954018d5fe0e57a8e5731256d66cbcf45e90
Summary:        Talk client for one-on-one Internet chatting
Name: talk
Version: 0.17
Release:        1%{?dist}
License: BSD-4-Clause-UC AND BSD-3-Clause
URL: http://web.archive.org/web/20070817165301/http://www.hcs.harvard.edu/~dholland/computers/netkit.html
Source0:        ftp://ftp.uk.linux.org/pub/linux/Networking/netkit/netkit-ntalk-%{version}.tar.gz
Source1: ntalk.socket
Source2: ntalk.service
Patch0: netkit-ntalk-0.17-pre20000412-time.patch
Patch1: netkit-ntalk-0.17-strip.patch
Patch2: netkit-ntalk-0.17-sockopt.patch
Patch3: netkit-ntalk-0.17-i18n.patch
Patch4: netkit-ntalk-0.17-resize.patch
Patch5: netkit-ntalk-0.17-person.patch
# oreon:deps
BuildRequires:  /usr/bin/perl
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  systemd
# /oreon:deps
%description
The talk package provides client programs for the Internet talk 
protocol, which allows you to chat with other users on different
systems.  Talk is a communication program which copies lines from one
terminal to the terminal of another user.

Install talk if you'd like to use talk for chatting with users on
different systems.

%package server
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Obsoletes: ntalk < %{version}-%{release}
Provides: ntalk = %{version}-%{release}
Summary: The talk server for one-on-one Internet chatting
%description server
The talk-server package provides daemon programs for the Internet talk
protocol, which allows you to chat with other users on different
machines.  Talk is a communication program which copies lines from one
terminal to the terminal of another user.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n netkit-ntalk-%{version}
%autopatch -p1

%build

./configure --with-c-compiler=cc
%{__perl} -pi -e '
    s,-O2,\$(RPM_OPT_FLAGS) -D_GNU_SOURCE -fpic -I/usr/include/ncursesw,;
    s,^LDFLAGS=,LDFLAGS=-pie,;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    s,^LIBCURSES=.*$,LIBCURSES=-lncursesw,;
    ' MCONFIG
%ifarch s390 s390x
%{__perl} -pi -e 's,-fpic,-fPIC,;' MCONFIG
%endif
make
%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,8}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
make INSTALLROOT=${RPM_BUILD_ROOT} install
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/ntalk.socket
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/ntalk.service
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%systemd_post ntalk.service
%systemd_post ntalk.socket
%preun server

%systemd_preun ntalk.service
%systemd_preun ntalk.socket
%postun server

%systemd_postun_with_restart ntalk.service
%systemd_postun_with_restart ntalk.socket
%files -f %{oreon_filedir}/main.list
%files -n talk-server -f %{oreon_filedir}/talk-server.list

%changelog

%autochangelog
