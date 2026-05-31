%global source0_hash 01576fa58598ccdd3d366febfaef61e3d1de93eb60a93f9ac6ba5faf84144c6f

%global catalogue /etc/X11/fontpath.d

%global majorver 4.5
Summary: An X Window System based IBM 3278/3279 terminal emulator
Name: x3270
Version: 4.5ga5
Release: 1%{?dist}
License: BSD-3-Clause AND HPND-sell-variant AND MIT AND Apache-2.0
URL: https://x3270.miraheze.org/wiki/Main_Page
Source0:        http://downloads.sourceforge.net/%{name}/suite3270-%{version}-src.tgz
Source1: x3270.png
Source2: x3270.desktop
Patch0: x3270-3.5-paths.patch
# workaround C23 related issues
Patch1: c23.patch
Patch2: mkversion.patch

BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: readline-devel
BuildRequires: openssl-devel
BuildRequires: libtool
BuildRequires: desktop-file-utils
BuildRequires: fonts-rpm-macros

%package x11
Summary: IBM 3278/3279 terminal emulator for the X Window System
BuildRequires: mkfontdir bdftopcf
BuildRequires: libXaw-devel
Requires: %{name} = %{version}
Requires: xrdb

%package text
Summary: IBM 3278/3279 terminal emulator for text mode
Requires: %{name} = %{version}


%description
The x3270 package contains files needed for emulating the IBM 3278/3279
terminals, commonly used with mainframe applications.

You will also need to install a frontend for %{name}. Available frontends
are %{name}-x11 (for the X Window System) and %{name}-text (for text mode).

%description x11
The x3270 program opens a window in the X Window System which emulates
the actual look of an IBM 3278/3279 terminal, commonly used with
mainframe applications.  x3270 also allows you to telnet to an IBM
host from the x3270 window.

Install the %{name}-x11 package if you need to access IBM hosts using an IBM
3278/3279 terminal emulator from X11.

%description text
The c3270 program opens a 3270 terminal which emulates the actual look of an
IBM 3278/3279 terminal, commonly used with mainframe applications.
x3270 also allows you to telnet to an IBM host from the x3270 window.

Install the %{name}-text package if you need to access IBM hosts using an IBM
3278/3279 terminal emulator without running X.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n suite3270-%{majorver}


%build
%configure --enable-x3270 --enable-c3270 --enable-s3270 --enable-pr3287 --disable-tcl3270 --disable-b3270 --enable-playback
make %{?_smp_mflags} CCOPTIONS="$RPM_OPT_FLAGS" LIBX3270DIR=%{_sysconfdir}


%install
make install DESTDIR=$RPM_BUILD_ROOT CIFONTDIR=%{_fontdir} LIBX3270DIR=%{_sysconfdir}
make install.man DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{catalogue}
ln -sf %{_fontdir} $RPM_BUILD_ROOT%{catalogue}/x3270

install -p -m755 "$(find ./obj -type f -name playback -print -quit)" $RPM_BUILD_ROOT%{_bindir}
install -p -m644 playback/playback.man $RPM_BUILD_ROOT%{_mandir}/man1/playback.1

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/48x48/apps

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
desktop-file-install \
        --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
        %{SOURCE2}


%files
%doc README.md
%{_bindir}/s3270
%{_bindir}/pr3287
%{_bindir}/prtodir
%{_bindir}/x3270if
%{_bindir}/playback
%{_mandir}/man1/s3270.1*
%{_mandir}/man1/pr3287.1*
%{_mandir}/man1/x3270if.1*
%{_mandir}/man1/playback.1*
%{_mandir}/man5/ibm_hosts.5*
%config(noreplace) %{_sysconfdir}/ibm_hosts

%files x11
%{_bindir}/x3270
%{_bindir}/x3270a
%{_fontdir}/
%{catalogue}/x3270
%{_mandir}/man1/x3270.1*
%{_datadir}/icons/hicolor/48x48/apps/x3270.png
%{_datadir}/applications/x3270.desktop

%files text
%{_bindir}/c3270
%{_mandir}/man1/c3270.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.5ga5-1
- Prepare for Oreon 11 (RP1)
