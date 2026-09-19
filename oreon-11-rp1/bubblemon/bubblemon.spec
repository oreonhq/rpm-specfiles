%global source0_hash f928073d3c69b2668e89b93cdcca5f390437831aab3eac3aa2129f8713e79dbf

Name:           bubblemon
Version:        1.46
Release:        42%{?dist}
Summary:        A system monitoring dockapp

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.ne.jp/asahi/linux/timecop/
Source0:        http://www.ne.jp/asahi/linux/timecop/software/bubblemon-dockapp-1.46.tar.gz

BuildRequires:  gcc
BuildRequires:  gtk+-devel
BuildRequires: make

%description
his is a system monitoring dockapp, visually based on the GNOME "BubbleMon"
applet (here). Basically, it displays CPU and memory load as bubbles in a jar
of water. But that's where similarity ends. New bubblemon-dockapp features
translucent CPU load meter (for accurate CPU load measurement), yellow duck
swimming back and forth on the water surface (just for fun), and fading load
average and memory usage screens. Either of the info screens can be locked to
stay on top of water/duck/cpu screen, so that you can see both statistics at
once. Pretty nifty toy for your desktop. Supports Linux, FreeBSD, OpenBSD, and
Solaris 2.6, 7 and 8. Code has been thoroughly optimized since version 1.0,
and even with all the features compiled in, BubbleMon still uses very little
CPU time. Load Average screen locked at about 20% looks particularly sexy. All
the extra "bloated" features can be compiled out or disabled on command-line,
if you prefer original "BubbleMon" look.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-dockapp-%{version}

%build
make CFLAGS="${RPM_OPT_FLAGS} `gtk-config --cflags` -DENABLE_DUCK -DENABLE_CPU -DENABLE_MEMSCREEN -DKERNEL_26" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

%files
%doc ChangeLog README doc/*
%{_bindir}/bubblemon

%changelog
%autochangelog
