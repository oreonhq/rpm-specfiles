%global source0_hash e3fe66f2ba3a226a520070cd7dd6eb94457a045d00769fea2cd0a6d775cc0a69

%global snapdate 20161006

Name:           ufw-kde
Version:        0.5.0
Release:        0.31.%{snapdate}git%{?dist}
Summary:        UFW control module for KDE

# Some files GPLv3 only, some files GPLv2+
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://projects.kde.org/projects/playground/sysadmin/ufw-kde
Source0:        ufw-kde-%{version}-%{snapdate}.tar.xz
# releaseme (kdelibs4 branch) scripts used to generate the above source tarball:
Source1:        ufw-kde.rb
Source2:        ufw-kderc
# standalone .desktop file to invoke UFW-KDE outside of systemsettings 4
Source3:        ufw-kde.desktop

# do not use #!/usr/bin/env for the Python helper
Patch0:         ufw-kde-0.5.0-no-env.patch
# rename strings.* to i18nstrings.* to work around strings.h name conflict
# (#1556517, #1606605)
Patch1:         ufw-kde-0.5.0-rename-strings-h.patch

BuildRequires: make
BuildRequires:  cmake
BuildRequires:  kdelibs4-devel
BuildRequires:  gettext
BuildRequires:  python3-devel
# bytecompile with Python 3
%global __python %{__python3}
# for desktop-file-install
BuildRequires:  desktop-file-utils

Requires:       ufw
Requires:       python3
# for kcmshell4, used in the standalone .desktop file
Requires:       kde-runtime

%description
KDE KControl Module to configure and control the Uncomplicated Firewall (UFW).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .no-env
%patch -P1 -p1 -b .rename-strings-h

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}

%py_byte_compile %{__python3} %{buildroot}%{_libexecdir}/kde4/
%find_lang %{name} --all-name --with-kde

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_kde4_sysconfdir}/dbus-1/system.d/org.kde.ufw.conf
%{_kde4_libdir}/kde4/kcm_ufw.so
%{_kde4_libexecdir}/kcm_ufw_helper
%{_kde4_libexecdir}/kcm_ufw_helper.py
%{_kde4_libexecdir}/__pycache__/
%{_kde4_datadir}/dbus-1/services/org.kde.ufw.service
%{_kde4_datadir}/dbus-1/system-services/org.kde.ufw.service
%{_kde4_datadir}/kde4/services/ufw.desktop
%{_kde4_datadir}/polkit-1/actions/org.kde.ufw.policy
%{_kde4_appsdir}/kcm_ufw/
%{_datadir}/applications/ufw-kde.desktop

%changelog
%autochangelog
