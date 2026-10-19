%global source0_hash d71f79a799f2838c1f52a993ec51286665428720189e6c242442059be8b7c04d
Name:             backintime
Version:          1.6.1
Release:        1%{?dist}
Summary:        Simple backup tool inspired from the Flyback project and TimeVault
License:          GPL-2.0-or-later
URL:              https://github.com/bit-team/backintime
Source0:        https://github.com/bit-team/backintime/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:        noarch
Requires:         %{name}-common = %{version}-%{release}
Requires:         hicolor-icon-theme
# oreon:deps
BuildRequires:  /usr/bin/ps
BuildRequires:  /usr/bin/rsync
BuildRequires:  /usr/bin/ssh-agent
BuildRequires:  cronie
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  python-rpm-macros
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-keyring
BuildRequires:  python3-pyfakefs
BuildRequires:  python3-pyqt6-base
BuildRequires:  python3-pytest
BuildRequires:  rubygem-asciidoctor
BuildRequires:  systemd
# /oreon:deps
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
%global __python %{__python3}
%make_install -C common
%make_install -C qt
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
auth            include         config-util
account         include         config-util
session         include         config-util
EOF
rm %{buildroot}%{_mandir}/man5
%oreon_autofiles backintime-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles backintime-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles backintime-qt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm common/test/test_tools.py
rm common/test/test_sshtools.py
rm common/test/test_lint.py qt/test/test_lint.py
rm common/test/test_uniquenessset.py
rm common/test/test_backintime.py
rm common/test/test_snapshots.py
%pytest common 
%pytest qt
%files -f %{oreon_filedir}/main.list
%files -n backintime-common -f %{oreon_filedir}/backintime-common.list
%files -n backintime-plugins -f %{oreon_filedir}/backintime-plugins.list
%files -n backintime-qt -f %{oreon_filedir}/backintime-qt.list

%changelog

%autochangelog
