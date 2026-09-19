%global source0_hash d71f79a799f2838c1f52a993ec51286665428720189e6c242442059be8b7c04d

Name:             backintime
Version:          1.6.1
Release:          1%{?dist}
Summary:          Simple backup tool inspired from the Flyback project and TimeVault
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              https://github.com/bit-team/backintime
Source0:          https://github.com/bit-team/backintime/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    cronie
BuildRequires:    desktop-file-utils
BuildRequires:    gettext
BuildRequires:    man-db
BuildRequires:    python-rpm-macros
BuildRequires:    python%{python3_pkgversion}-devel
BuildRequires:    rubygem-asciidoctor
BuildRequires:    systemd
Requires:         %{name}-common = %{version}-%{release}
# we place additional icons
Requires:         hicolor-icon-theme

# execution of tests
BuildRequires:    python%{python3_pkgversion}-keyring
BuildRequires:    python%{python3_pkgversion}-pyfakefs
BuildRequires:    python%{python3_pkgversion}-pytest
BuildRequires:    python%{python3_pkgversion}-dbus
BuildRequires:    python%{python3_pkgversion}-pyqt6-base
BuildRequires:    /usr/bin/ssh-agent
BuildRequires:    /usr/bin/ps
BuildRequires:    /usr/bin/rsync
BuildRequires:    make

%description
Back In Time is a simple backup system for Linux inspired from 
“flyback project” and “TimeVault”. The backup is done by taking 
snapshots of a specified set of directories.

%package          common
Summary:          Common files for %{name}
Requires:         cronie
Requires:         openssh-clients
Requires:         python%{python3_pkgversion}-keyring
Requires:         python%{python3_pkgversion}-dbus
Requires:         python%{python3_pkgversion}-packaging
Requires:         fuse-sshfs
Requires:         gocryptfs
Requires:         bindfs
Requires:         /usr/bin/ssh-agent
Requires:         /usr/bin/ps
Requires:         /usr/bin/rsync

%description      common
Back In Time is a simple backup system for Linux inspired from 
“flyback project” and “TimeVault”. The backup is done by taking 
snapshots of a specified set of directories.

This package contains non GUI files for %{name}.

%package          plugins
Summary:          Plugins for %{name}
Requires:         %{name}-common = %{version}-%{release}
Provides:         backintime-notify = %{version}-%{release}
Obsoletes:        backintime-notify < 1.1.12-1

%description      plugins
%summary}.

%package          qt
Summary:          Qt frontend for %{name}
Requires:         %{name}-common = %{version}-%{release}
Requires:         polkit
Requires:         python%{python3_pkgversion}-pyqt6
Requires:         python%{python3_pkgversion}-SecretStorage
Requires:         python%{python3_pkgversion}-keyring
Requires:         qt6-qttranslations
Requires:         xdpyinfo
Provides:         backintime-gnome = %{version}-%{release}
Obsoletes:        backintime-gnome < 1.1.12-1
Provides:         backintime-kde = %{version}-%{release}
Obsoletes:        backintime-kde < 1.1.12-1
Provides:         %{name}-qt4 = %{version}-%{release}
Obsoletes:        %{name}-qt4 < 1.1.24-8

Recommends:       %{name}-plugins

%description      qt
BackInTime is a simple backup system for Linux inspired from 
“flyback project” and “TimeVault”. The backup is done by taking 
snapshots of a specified set of directories.

This package contains the Qt frontend of BackInTime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
pushd common
%configure \
    --python=%{__python3} 
popd

pushd qt
%configure \
    --python=%{__python3} 
popd

%make_build -C common
%make_build -C qt

%install
#Force Python 3 to be used for byte compilation:
%global __python %{__python3}
%make_install -C common
%make_install -C qt

# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/qt

%find_lang %{name}

desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}-qt.desktop
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications/ \
        --add-category="Settings;" \
        %{buildroot}%{_datadir}/applications/%{name}-qt-root.desktop

ln -s consolehelper \
      %{buildroot}%{_bindir}/%{name}-qt-root

mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps/
cat << EOF > %{buildroot}%{_sysconfdir}/security/console.apps/%{name}-qt-root
USER=root
PROGRAM=%{_bindir}/%{name}-qt-root
SESSION=true
EOF

mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cat << EOF > %{buildroot}%{_sysconfdir}/pam.d/%{name}-qt-root
#%PAM-1.0
auth            include         config-util
account         include         config-util
session         include         config-util
EOF

rm %{buildroot}%{_mandir}/man5

%check
rm common/test/test_tools.py
rm common/test/test_sshtools.py
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
rm common/test/test_lint.py qt/test/test_lint.py
# remove test until PyFakeFS is not updated 
rm common/test/test_uniquenessset.py
rm common/test/test_backintime.py
rm common/test/test_snapshots.py
%pytest common 
%pytest qt

%files common -f %{name}.lang
%doc %{_datadir}/doc/%{name}-common/
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{_bindir}/%{name}-askpass
%{_datadir}/%{name}/common/
%{_datadir}/bash-completion/completions/backintime
%{_datadir}/dbus-1/system-services/net.launchpad.backintime.serviceHelper.service
%{_datadir}/polkit-1/actions/net.launchpad.backintime.policy
%{_datadir}/dbus-1/system.d/net.launchpad.backintime.serviceHelper.conf
%{_datadir}/metainfo/io.github.bit_team.back_in_time.gui.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/backintime.svg
%{_mandir}/man1/%{name}*

%files plugins
%{_datadir}/%{name}/plugins/

%files qt
%doc %{_docdir}/%{name}-qt/
%{_bindir}/%{name}-qt
%{_bindir}/%{name}-qt-root
%{_bindir}/%{name}-qt_polkit
%{_datadir}/applications/%{name}-qt.desktop
%{_datadir}/applications/%{name}-qt-root.desktop
%{_datadir}/backintime/qt/
%{_datadir}/icons/hicolor/*/actions/*.svg
%{_datadir}/bash-completion/completions/backintime-qt
%config(noreplace) %{_sysconfdir}/pam.d/%{name}-qt-root
%config %{_sysconfdir}/security/console.apps/%{name}-qt-root

%changelog
%autochangelog
