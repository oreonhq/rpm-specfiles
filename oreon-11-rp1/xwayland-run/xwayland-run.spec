%global source0_hash dccd8e103ebf39b354537cd19a7601a996fd7591238be2ba68683e52aca96b66

Name:           xwayland-run
Version:        0.0.6
Release:        1%{?dist}
Summary:        Set of utilities to run headless X/Wayland clients

License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/ofourdan/xwayland-run
Source0:        https://gitlab.freedesktop.org/ofourdan/xwayland-run/-/archive/0.0.6/xwayland-run-0.0.5.tar.gz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git_am -n xwayland-run-%{version}-9cc35f59659dca42192c3c6f47a89b5f1bd1bb55


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
%autochangelog
