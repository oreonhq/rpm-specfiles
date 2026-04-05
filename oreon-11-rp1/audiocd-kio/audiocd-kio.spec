
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    audiocd-kio
Summary: KF6 Audiocd kio slave
Version: 25.12.3
Release:	2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND LGPL-3.0-or-later
URL:     https://invent.kde.org/multimedia/audiocd-kio
	
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# cdparanoia-devel not on all arches for RHEL8.
%if 0%{?rhel} == 8
ExclusiveArch: x86_64 ppc64le aarch64 %{arm}
%endif

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: cdparanoia-devel cdparanoia
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6KIO)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: cmake(KCddb6)
BuildRequires: cmake(KCompactDisc6)

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(phonon4qt6)

# See: https://docs.kde.org/trunk5/en/audiocd-kio/kcontrol/kcmaudiocd/index.html
# Those are explicitely required at build time
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(theora)
BuildRequires: pkgconfig(vorbis)
# The MP3 and Opus Encoder tabs are only available if the tools are installed
Recommends: lame
Recommends: opus-tools

Requires:  %{name}-doc = %{version}-%{release}


# when split occurred (kdemultimedia to audiocd-kio rpm)
# when split occurred
# for the former audiocd-kio-libs rpm
Conflicts: kdemultimedia-libs < 6:4.8.80
# for the former audiocd-kio rpm
Obsoletes: kdemultimedia-kio_audiocd < 6:4.8.80
Provides:  kdemultimedia-kio_audiocd = 6:%{version}-%{release}
Provides:  kio_audiocd = %{version}-%{release}
# conflicts from later history of kf5-audiocd-kio
# when conflicting /usr/share/config.kcfg/audiocd_vorbis_encoder.kcfg was dropped
Conflicts: kf5-audiocd-kio < 24.01.85
Obsoletes: kf5-audiocd-kio < 24.01.85
Conflicts: audiocd-kio-libs < 24.01.85
Obsoletes: audiocd-kio-libs < 24.01.85
# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package devel
Summary:  Development files for %{name}
# from the former kdemultimedia - audiocd-kio split
Conflicts: kdemultimedia-devel < 6:4.8.80
# libaudiocdplugins.so symlink conflict (now against kf5-audiocd-kio-devel)
Conflicts: kf5-audiocd-kio-devel < 24.01.85
Obsoletes: kf5-audiocd-kio-devel < 24.01.85
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package doc
Summary: Documentation for %{name}
License: GFDL-1.2-only
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
# now ahead of kf5-libkcddb
Conflicts: kf5-audiocd-kio-doc < 24.01.85
Obsoletes: kf5-audiocd-kio-doc < 24.01.85
%description doc
Documentation for %{name}.


%prep
%autosetup -p1


%build
%cmake_kf6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-man
%find_lang %{name}-doc --all-name --with-html --without-mo


%files -f %{name}.lang
%license COPYING*
%{_kf6_datadir}/qlogging-categories6/*
%{_kf6_metainfodir}/org.kde.kio_audiocd.*.xml
%{_kf6_libdir}/libaudiocdplugins.so.5*
%{_qt6_plugindir}/libaudiocd_encoder_flac.so
%{_qt6_plugindir}/libaudiocd_encoder_lame.so
%{_qt6_plugindir}/libaudiocd_encoder_opus.so
%{_qt6_plugindir}/libaudiocd_encoder_vorbis.so
%{_qt6_plugindir}/libaudiocd_encoder_wav.so
%{_kf6_plugindir}/kio/audiocd.so
%{_kf6_datadir}/config.kcfg/audiocd_*_encoder.kcfg
%dir %{_kf6_datadir}/konqsidebartng/
%dir %{_kf6_datadir}/konqsidebartng/virtual_folders
%dir %{_kf6_datadir}/konqsidebartng/virtual_folders/services/
%{_kf6_datadir}/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_kf6_datadir}/solid/actions/solid_audiocd.desktop
%{_kf6_datadir}/applications/kcm_audiocd.desktop
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_audiocd.so

%files devel
%{_kf6_libdir}/libaudiocdplugins.so
%{_includedir}/audiocdplugins/

%files doc -f %{name}-doc.lang
%license COPYING.DOC


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
