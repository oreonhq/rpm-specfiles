Name:           xwayland-run
Version:        0.0.5
Release:        1%{?dist}
Summary:        Set of utilities to run headless X/Wayland clients

License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/ofourdan/xwayland-run
Source0:        https://gitlab.freedesktop.org/ofourdan/xwayland-run/-/archive/0.0.5/xwayland-run-0.0.5.tar.gz
# oreon url source checksums begin
%global source0_sha256 b000386a0f0270cf49d5207b60215de7a09423d8afe3a45fe3e315791667fbb5
%global source0_file xwayland-run-0.0.5.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xwayland-run-0.0.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b000386a0f0270cf49d5207b60215de7a09423d8afe3a45fe3e315791667fbb5" || { echo "oreon: Source0 SHA256 mismatch for xwayland-run-0.0.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
