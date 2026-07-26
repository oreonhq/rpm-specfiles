%global source0_hash e08c34dbac44794bd851f5336991cf932c7aff4827f2bb977268dfbbd7c143dc

Name:    kremotecontrol 
Summary: KDE frontend for your remote controls 
Version: 17.08.3
Release: 21%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://utils.kde.org/projects/%{name}
#URL:    https://cgit.kde.org/%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches
# lib namelink_skip
Patch50: kremotecontrol-4.7.90-namelink_skip.patch

BuildRequires: desktop-file-utils
BuildRequires: kdelibs4-devel >= 4.14.4
BuildRequires: pkgconfig(QtXmlPatterns)
BuildRequires: make

# when split occured
Conflicts: kdeutils-common < 6:4.7.80

Obsoletes: kdeutils-kremotecontrol < 6:4.7.80
Provides:  kdeutils-kremotecontrol = 6:%{version}-%{release}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%{?kde_runtime_requires}

%description
KRemoteControl (formerly known as KDELirc) is a KDE frontend for your
remote controls. It allows to configure actions for button presses on
remotes. All types of remotes supported by the Solid module in the KDE
platform are also supported by KRemoteControl (e.g. with the Linux
Infrared Remote Control system (LIRC) as backend).

%package libs
Summary: Runtime libraries for %{name} 
Requires: %{name} = %{version}-%{release}
Obsoletes: kdeutils-kremotecontrol-libs < 6:4.7.80
Provides:  kdeutils-kremotecontrol-libs = 6:%{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%check
desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/krcdnotifieritem.desktop

%files
%license COPYING
%doc AUTHORS README
%{_kde4_appsdir}/kremotecontrol/
%{_kde4_appsdir}/kremotecontroldaemon/
%{_kde4_datadir}/kde4/services/plasma-engine-kremotecontrol.desktop
%{_kde4_datadir}/kde4/services/kcm_remotecontrol.desktop
%{_kde4_datadir}/kde4/services/kded/kremotecontroldaemon.desktop
%{_kde4_iconsdir}/hicolor/*/devices/infrared-remote.*
%{_kde4_libdir}/kde4/kcm_remotecontrol.so
%{_kde4_libdir}/kde4/kded_kremotecontroldaemon.so
%{_kde4_libdir}/kde4/plasma_engine_kremoteconrol.so
%{_kde4_datadir}/kde4/services/kremotecontrolbackends/
%{_kde4_datadir}/kde4/servicetypes/kremotecontrolmanager.desktop
%{_kde4_libdir}/kde4/kremotecontrol_lirc.so
%{_kde4_bindir}/krcdnotifieritem
%{_kde4_datadir}/applications/kde4/krcdnotifieritem.desktop
%{_kde4_iconsdir}/hicolor/*/*/krcd*.*
%dir %{_kde4_docdir}/HTML/en/kcontrol/
%lang(en) %{_kde4_docdir}/HTML/en/kcontrol/kremotecontrol/

%ldconfig_scriptlets libs

%files libs
%{_kde4_libdir}/liblibkremotecontrol.so.1*

%changelog
%autochangelog
