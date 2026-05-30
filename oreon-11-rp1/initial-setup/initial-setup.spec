%global source0_hash a4b8217ac76039613329a1eecba0b2f7d4de4cb07cca03ff0f4dda9311f71d30

# Enable X11 for RHEL 9 and older only
%bcond x11 %[0%{?rhel} && 0%{?rhel} < 10]

Name: initial-setup
Summary: Initial system configuration utility
URL: https://fedoraproject.org/wiki/InitialSetup
License: GPL-2.0-or-later
Version: 0.3.101
Release: 7%{?dist}

# This is a Red Hat maintained package which is specific to
# our distribution.
#
# The source is thus available only from within this SRPM
# or via direct git checkout:
# git clone https://github.com/rhinstaller/initial-setup
Source0: %{name}-%{version}.tar.gz

%define debug_package %{nil}
%define anacondaver 37.8-1

BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: systemd-units
BuildRequires: gtk3-devel
BuildRequires: glade-devel
BuildRequires: intltool
BuildRequires: make

Requires: %{__python3}
Requires: anaconda-tui >= %{anacondaver}
Requires: libxkbcommon
Requires: python3-simpleline >= 1.4
Requires: systemd >= 235
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: util-linux
Conflicts: firstboot < 19.2

%description
The initial-setup utility runs after installation.  It guides the user through
a series of steps that allows for easier configuration of the machine.

%post
%systemd_post initial-setup.service

%preun
%systemd_preun initial-setup.service

%postun
%systemd_postun initial-setup.service

%files -f %{name}.lang
%doc README.rst ChangeLog
%license COPYING
%{python3_sitelib}/initial_setup*
%exclude %{python3_sitelib}/initial_setup/gui
%{_libexecdir}/%{name}/run-initial-setup
%{_libexecdir}/%{name}/initial-setup-text
%{_libexecdir}/%{name}/reconfiguration-mode-enabled
%{_unitdir}/initial-setup.service
%{_unitdir}/initial-setup-reconfiguration.service
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%config %{_sysconfdir}/%{name}/conf.d/*
%{_sysconfdir}/pam.d/initial-setup

%ifarch s390 s390x
%{_sysconfdir}/profile.d/initial-setup.sh
%{_sysconfdir}/profile.d/initial-setup.csh
%endif

# --------------------------------------------------------------------------

%package gui
Summary: Graphical user interface for the initial-setup utility
Requires: gtk3
Requires: anaconda-gui >= %{anacondaver}
Requires: firstboot(gui-backend)
Requires: %{name} = %{version}-%{release}
Suggests: %{name}-gui-wayland-generic

%description gui
The initial-setup-gui package contains a graphical user interface for the
initial-setup utility.

%files gui
%{_libexecdir}/%{name}/initial-setup-graphical
%{python3_sitelib}/initial_setup/gui/

# --------------------------------------------------------------------------

%package gui-wayland-generic
Summary: Run the initial-setup GUI in Wayland
Requires: %{name}-gui = %{version}-%{release}
Requires: weston
Requires: xorg-x11-server-Xwayland

Provides:  firstboot(gui-backend)
Conflicts: firstboot(gui-backend)
RemovePathPostfixes: .guiweston

%description gui-wayland-generic
%{summary}.

%files gui-wayland-generic
%{_libexecdir}/%{name}/run-gui-backend.guiweston

# --------------------------------------------------------------------------

%if %{with x11}
%package gui-xorg
Summary: Run the initial-setup GUI in Xorg
Requires: %{name}-gui = %{version}-%{release}
Requires: xorg-x11-xinit
Requires: xorg-x11-server-Xorg
Requires: firstboot(windowmanager)

Provides:  firstboot(gui-backend)
Conflicts: firstboot(gui-backend)
RemovePathPostfixes: .guixorg

%description gui-xorg
%{summary}.

%files gui-xorg
%{_libexecdir}/%{name}/run-gui-backend.guixorg
%{_libexecdir}/%{name}/firstboot-windowmanager
%endif

# --------------------------------------------------------------------------

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p 1

# remove upstream egg-info
rm -rf *.egg-info

%build
%make_build

%install
%make_install

# Remove the default link, provide subpackages for alternatives
rm %{buildroot}%{_libexecdir}/%{name}/run-gui-backend

%if ! %{with x11}
# We do not want to ship X11 support anymore
rm -v %{buildroot}%{_libexecdir}/%{name}/run-gui-backend.guixorg
rm -v %{buildroot}%{_libexecdir}/%{name}/firstboot-windowmanager
%endif

%find_lang %{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.101-7
- Import
