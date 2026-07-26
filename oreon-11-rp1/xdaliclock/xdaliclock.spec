%global source0_hash 6b573a8bac23a72e87a1cd9966c28f1d653bdb0b28bb8fd11633a1a4c2fd9fa4

Summary: A clock for the X Window System
Name: xdaliclock
Version: 2.43
Release: 24%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://www.jwz.org/xdaliclock/
Source0: http://www.jwz.org/xdaliclock/xdaliclock-%{version}.tar.gz
Source1: xdaliclock.desktop
Patch0: xdaliclock-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: libICE-devel, libXmu-devel, libSM-devel, xorg-x11-proto-devel
BuildRequires: libXext-devel, libXaw-devel, libXt-devel
BuildRequires: redhat-rpm-config

%description
XDaliClock is a large digital clock for the X Window System, with digits
that "melt" into their new shapes when the time changes. XDaliClock
supports 12 and 24 hour modes, and displays the date when you hold a mouse
button down over it. It also can be configured to do colormap cycling, and
for window transparency.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# easier than patching configure to read those files from own directory
cp /usr/lib/rpm/redhat/config.{guess,sub} .

cd X11
%configure
make %{?_smp_mflags}

%install
cd X11

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults

install -p -m 0755 xdaliclock $RPM_BUILD_ROOT%{_bindir}
install -p -m 0644 xdaliclock.man \
	$RPM_BUILD_ROOT%{_mandir}/man1/xdaliclock.1
install -p -m 0644 XDaliClock.ad \
	$RPM_BUILD_ROOT%{_datadir}/X11/app-defaults/XDaliClock

desktop-file-install  \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--add-category "X-Fedora" \
	--add-category "Graphics" \
	%{SOURCE1}

%files
%doc README
%{_bindir}/xdaliclock
%{_mandir}/man1/xdaliclock.1*
%{_datadir}/X11/app-defaults/XDaliClock
%{_datadir}/applications/*

%changelog
%autochangelog
