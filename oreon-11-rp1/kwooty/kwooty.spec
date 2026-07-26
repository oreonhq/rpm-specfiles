%global source0_hash 578d0e976edd3ccbea6dabd486878a2b0b357d4b69884865eb4149b3a5564981

Name:    kwooty
Summary: A friendly nzb usenet binary download application
Version: 1.1.0
Release: 31%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://kwooty.sourceforge.net/
Source0: http://sourceforge.net/projects/kwooty/files/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: kde-workspace-devel
BuildRequires: kdelibs4-devel
BuildRequires: make

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kde-runtime%{?_kde4_version: >= %{_kde4_version}}
Requires: par2cmdline

# multilib upgrade path, when -libs subpkg was introduced
Obsoletes: kwooty < 1.1.0-4

%description
Kwooty is a NZB usenet binary download application for KDE 4.
It's main features are:
- Automatic file verification/repairing
- Automatic archive extraction (Rar, Zip and 7z archive formats supported)
- Multi-server support
- Built-in YEnc and UUEncode file decoders
- Watch Folder
- File queue and priority management
- System shutdown scheduler.
- Save/Restore pending downloads when application is closed/open.
- Built-in SSL connection support
- Pause/Resume downloads
- Suspends downloads if disk is full
- Display of Remaining Time or Estimated Time of Arrival (ETA)
- Display of available free disk space
- Automatic connection to host at start-up
- Automatic file downloading after opening Nzb file

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/kwooty.desktop

%find_lang kwooty --with-kde

## unpackaged files
# remove lib symlink
rm -f %{buildroot}%{_kde4_libdir}/libkwootycore.so

%files -f kwooty.lang
%doc README.txt TODO
%license COPYING
%{_kde4_bindir}/kwooty
%{_kde4_libdir}/kde4/kwooty_*
%{_kde4_datadir}/applications/kde4/kwooty.desktop
%{_kde4_datadir}/config.kcfg/kwooty_*.kcfg
%{_kde4_datadir}/config.kcfg/kwootysettings.kcfg
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_appsdir}/kwooty/
%{_kde4_datadir}/kde4/services/kwooty*
%{_kde4_datadir}/kde4/servicetypes/kwootyplugin.desktop

%ldconfig_scriptlets libs

%files libs
%{_kde4_libdir}/libkwootycore.so.*

%changelog
%autochangelog
