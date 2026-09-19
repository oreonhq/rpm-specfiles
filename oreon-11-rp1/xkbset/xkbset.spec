%global source0_hash 01c2579495b39e00d870f50225c441888dc88021e9ee3b693a842dd72554d172

Name:           xkbset
Version:        0.5
Release:        31%{?dist}
Summary:        Tool to configure XKB extensions

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.math.missouri.edu/~stephen/software/#xkbset
Source0:        http://www.math.missouri.edu/~stephen/software/xkbset/xkbset-%{version}.tar.gz
# 2012-10-03: Sent upstream via e-mail
Source3:        xkbset.desktop
# 2012-10-03: Sent upstream via e-mail
Patch0:         xkbset-0.5-install.patch

# for /usr/include/X11/Xlib.h
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: desktop-file-utils
BuildRequires: perl-generators
BuildRequires: gcc

%description
xkbset is a program rather like xset in that it allows you to set various
features of the X window interface.  It allows one to configure most of the
options connected with the XKB extensions.  They are described in Section 10 of
XKBlib.ps.

This includes customizing the following:
  MouseKeys:  using the numeric pad keys to move the mouse;
  StickyKeys: where modifiers like control and shift will lock until the
              next key press (good for one finger typing);
  SlowKeys:   The keys will not work unless they are pressed for a certain
              amount of time;
  BounceKeys: If a key is pressed more than once rapidly, only one key
              press will be registered.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .install

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
%make_install X11PREFIX=%{_prefix} INSTALL_PROGRAM=install INSTALL_MAN1=$RPM_BUILD_ROOT/%{_mandir}/man1
desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE3}

%files
%doc COPYRIGHT README TODO VERSIONS
%{_bindir}/xkbset
%{_bindir}/xkbset-gui
%{_mandir}/man1/xkbset.1*
%{_datadir}/applications/xkbset.desktop

%changelog
%autochangelog
