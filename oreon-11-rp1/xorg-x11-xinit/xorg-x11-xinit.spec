%global source0_hash 40a47c7a164c7f981ce3787b4b37f7e411fb43231dcde543d70094075dacfef9
%global pkgname xinit
Summary:        X.Org X11 X Window System xinit startup scripts
Name:       xorg-x11-%{pkgname}
Version:    1.4.4
Release:        1%{?dist}
License:    X11-distribute-modifications-variant AND MIT-open-group
URL:        https://www.x.org
Source0:        https://www.x.org/archive/individual/app/%{pkgname}-%{version}.tar.xz
Source10:   xinitrc-common
Source11:   xinitrc
Source12:   Xclients
Source13:   Xmodmap
Source14:   Xresources
Source16:   Xsession
Source17:   localuser.sh
Source18:   xinit-compat.desktop
Source19:   xinit-compat
Patch1: xinit-1.0.2-client-session.patch
Patch5: 0003-startx-Make-startx-auto-display-select-work-with-per.patch
Patch6: xinit-1.3.4-set-XORG_RUN_AS_USER_OK.patch
Requires:   xorg-x11-xauth
Requires:   coreutils
Requires:   xhost xrdb setxkbmap xmodmap
Provides:   %{pkgname} = %{version}
# oreon:deps
BuildRequires:  automake
BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
X.Org X11 X Window System xinit startup scripts.

%package session
Summary:    Display manager support for ~/.xsession and ~/.Xclients
%description session
Allows legacy ~/.xsession and ~/.Xclients files to be used from display
managers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xorg-x11-xinit-session -f %{oreon_filedir}/xorg-x11-xinit-session.list

%changelog

%autochangelog
