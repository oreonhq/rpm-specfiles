Name:           xwayland-run
Version:        0.0.5
Release:        1%{?dist}
Summary:        Set of utilities to run headless X/Wayland clients

License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/ofourdan/xwayland-run
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson >= 0.60.0
BuildRequires:  git-core
BuildRequires:  python3-devel
Requires:       (weston or cage or kwin-wayland or mutter or gnome-kiosk)
Requires:       xorg-x11-server-Xwayland
Requires:       dbus-daemon
Requires:       xorg-x11-xauth

# Handle preference for boolean dep on compositor
%if 0%{?rhel}
Suggests:       mutter
%else
Suggests:       weston
%endif

# Provide names of the other utilities included
Provides:       wlheadless-run = %{version}-%{release}
Provides:       xwfb-run = %{version}-%{release}

%description
xwayland-run contains a set of small utilities revolving around running
Xwayland and various Wayland compositor headless.


%prep
%autosetup -S git_am


%build
%meson %{?rhel:-Dcompositor=mutter}
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README.md
%{_bindir}/wlheadless-run
%{_bindir}/xwayland-run
%{_bindir}/xwfb-run
%{_datadir}/wlheadless/
%{_mandir}/man1/wlheadless-run.1*
%{_mandir}/man1/xwayland-run.1*
%{_mandir}/man1/xwfb-run.1*
%{python3_sitelib}/wlheadless/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.5-1
- Prepare for Oreon 11 (RP1)
