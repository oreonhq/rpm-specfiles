%global source0_hash 86409f21a6a31148d2c1c17bf5f2d904eb5ef455f9dc67c49fbd0c10ab18fd5a

%global pkgname xinit

Summary:    X.Org X11 X Window System xinit startup scripts
Name:       xorg-x11-%{pkgname}
Version:    1.4.3
Release:    4%{?dist}
License:    X11-distribute-modifications-variant AND MIT-open-group
URL:        https://www.x.org

Source0:    https://xorg.freedesktop.org/archive/individual/app/%{pkgname}-%{version}.tar.xz
Source10:   xinitrc-common
Source11:   xinitrc
Source12:   Xclients
Source13:   Xmodmap
Source14:   Xresources
# NOTE: Xsession is used by xdm/kdm/gdm and possibly others, so we keep it
#       here instead of the xdm package.
Source16:   Xsession
Source17:   localuser.sh
Source18:   xinit-compat.desktop
Source19:   xinit-compat

# Fedora specific patches
Patch1: xinit-1.0.2-client-session.patch
Patch5: 0003-startx-Make-startx-auto-display-select-work-with-per.patch
# Fedora specific patch to match the similar patch in the xserver
Patch6: xinit-1.3.4-set-XORG_RUN_AS_USER_OK.patch

# The build process uses cpp (the C preprocessor) to do some text
# processing on several files that are not C or C++. However, these
# files have '.cpp' extensions, which causes cpp to preprocess them
# using cc1plus, which is part of gcc-c++. We could patch the build
# to pass '-xc' or '-xassembler-with-cpp' to cpp to avoid this, but
# doing so actually causes the processing to be done differently
# somehow, and a bunch of empty lines to show up at the top of
# startx (which is one of the files so processed). So it seems better
# to just BuildRequire gcc-c++ for now, so the processing is done as
# it was before. See https://bugs.freedesktop.org/show_bug.cgi?id=107368
# for more on this.
BuildRequires:  make
BuildRequires:  automake gcc gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  dbus-devel

# NOTE: startx needs xauth in order to run, but that is not picked up
#       automatically by rpm.  (Bug #173684)
Requires:   xorg-x11-xauth
# next two are for localuser.sh
Requires:   coreutils
Requires:   xhost xrdb setxkbmap xmodmap

Provides:   %{pkgname} = %{version}

%description
X.Org X11 X Window System xinit startup scripts.

%package session
Summary:    Display manager support for ~/.xsession and ~/.Xclients

%description session
Allows legacy ~/.xsession and ~/.Xclients files to be used from display
managers.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{pkgname}-%{version}
%patch -P1 -p1
%patch -P5 -p1
%patch -P6 -p1

%build
%configure
%make_build

%install
%make_install
install -p -m644 -D %{SOURCE18} $RPM_BUILD_ROOT%{_datadir}/xsessions/xinit-compat.desktop

# Install Red Hat custom xinitrc, etc.
{
    mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit

    install -p -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc-common

    for script in %{SOURCE11} %{SOURCE12} %{SOURCE16} ; do
        install -p -m 755 $script $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/${script##*/}
    done

    install -p -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/X11/Xmodmap
    install -p -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{_sysconfdir}/X11/Xresources

    mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d
    install -p -m 755 %{SOURCE17} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/localuser.sh

    mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/Xclients.d

    mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
    install -p -m 755 %{SOURCE19} $RPM_BUILD_ROOT%{_libexecdir}
}

%files
%doc COPYING README.md ChangeLog
%{_bindir}/startx
%{_bindir}/xinit
%dir %{_sysconfdir}/X11/xinit
%{_sysconfdir}/X11/xinit/xinitrc
%{_sysconfdir}/X11/xinit/xinitrc-common
%config(noreplace) %{_sysconfdir}/X11/Xmodmap
%config(noreplace) %{_sysconfdir}/X11/Xresources
%dir %{_sysconfdir}/X11/xinit/Xclients.d
%{_sysconfdir}/X11/xinit/Xclients
%{_sysconfdir}/X11/xinit/Xsession
%dir %{_sysconfdir}/X11/xinit/xinitrc.d
%{_sysconfdir}/X11/xinit/xinitrc.d/*
%{_mandir}/man1/startx.1*
%{_mandir}/man1/xinit.1*

%files session
%{_libexecdir}/xinit-compat
%{_datadir}/xsessions/xinit-compat.desktop

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.3-4
- Prepare for Oreon 11 (RP1)
