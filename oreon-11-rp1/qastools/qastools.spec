%global source0_hash d18ee5e1045ec44a18d5f7b8613f3987f225b4ef96c63128bf5cc645b2e6dbbb

Name:           qastools
Version:        0.23.0
Release:        13%{?dist}
Summary:        Collection of desktop applications for ALSA
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only

URL:            https://gitlab.com/sebholt/qastools
Source0:        https://gitlab.com/sebholt/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  cmake gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtbase-devel qt5-qtsvg-devel qt5-linguist
BuildRequires:  pkgconfig(alsa)
# For libudev.h
BuildRequires:  systemd-devel

Requires:       qasconfig%{?_isa} = %{version}-%{release}
Requires:       qashctl%{?_isa} = %{version}-%{release}
Requires:       qasmixer%{?_isa} = %{version}-%{release}

%description
QasTools is a collection of desktop applications for the ALSA sound system.

%package -n qascommon
Summary:        Common part of QasTools

%description -n qascommon
Common part of QasTools.

%package -n qasconfig
Summary:	    ALSA configuration browser
Requires:	    qascommon%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n qasconfig
Browser for the ALSA configuration tree.

%package -n qashctl
Summary: 	    ALSA complex mixer
Requires:	    qascommon%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n qashctl
Mixer for ALSA's more complex "High level Control Interface".

%package -n qasmixer
Summary:        ALSA simple mixer
Requires:       qascommon%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n qasmixer
Desktop mixer for ALSA's "Simple Mixer Interface" (alsamixer).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}

%build
%cmake -DSKIP_LICENSE_INSTALL:BOOL=ON
%cmake_build

%install
%cmake_install
for file in %{buildroot}/%{_datadir}/applications/*.desktop; do
    desktop-file-validate $file
done
%find_lang %{name} --with-qt --without-mo
# hack
#rm -f %{buildroot}/%{_datadir}/%{name}/l10n/qastools_default.qm

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
# meta package

%files -n qascommon -f %{name}.lang
%license COPYING
%doc CHANGELOG README.md TODO
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/widgets/

%files -n qasconfig
%{_bindir}/qasconfig
%{_datadir}/applications/qasconfig.desktop
%{_datadir}/icons/hicolor/*/apps/qasconfig.*
%{_mandir}/man1/qasconfig.1.*
%{_metainfodir}/qasconfig.appdata.xml

%files -n qashctl
%{_bindir}/qashctl
%{_datadir}/applications/qashctl.desktop
%{_datadir}/icons/hicolor/*/apps/qashctl.*
%{_mandir}/man1/qashctl.1.*
%{_metainfodir}/qashctl.appdata.xml

%files -n qasmixer
%{_bindir}/qasmixer
%{_datadir}/%{name}/icons/
%{_datadir}/applications/qasmixer.desktop
%{_datadir}/icons/hicolor/*/apps/qasmixer.*
%{_mandir}/man1/qasmixer.1.*
%{_metainfodir}/qasmixer.appdata.xml

%changelog
%autochangelog
