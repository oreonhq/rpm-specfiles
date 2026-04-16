Name:           blivet-gui
Version:        2.6.0
Release:        1%{?dist}
Summary:        Graphical tool for storage configuration

License:        GPL-2.0-or-later
URL:            https://github.com/storaged-project/blivet-gui
Source0:        https://github.com/storaged-project/blivet-gui/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       %{name}-runtime = %{version}-%{release}

%description
blivet-gui is a GTK-based utility for inspecting and modifying storage layout,
including partitions, filesystems, LVM, RAID, and encrypted devices.

%package runtime
Summary:        Runtime files for blivet-gui
Requires:       python3-blivet >= 1:3.13.0
Requires:       python3-gobject-base
Requires:       python3-pid
Requires:       python3-pyparted
Requires:       gtk3
Requires:       polkit

%description runtime
Runtime files for blivet-gui, including Python modules, daemon, UI assets,
translations, policy files, and desktop integration data.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build
make -C po

%install
%py3_install
RPM_BUILD_ROOT=%{buildroot} make -C po install

%files
%{_bindir}/blivet-gui
%{_datadir}/applications/blivet-gui.desktop
%{_mandir}/man1/blivet-gui.1*

%files runtime
%license COPYING
%doc README.md
%{_bindir}/blivet-gui-daemon
%{python3_sitelib}/blivetgui/
%{python3_sitelib}/blivet_gui-*.egg-info/
%{_datadir}/blivet-gui/
%{_datadir}/appdata/*.xml
%{_datadir}/icons/hicolor/*/apps/blivet-gui.png
%{_datadir}/locale/*/LC_MESSAGES/blivet-gui.mo
%{_datadir}/polkit-1/actions/org.fedoraproject.pkexec.blivet-gui.policy
