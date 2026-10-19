%global source0_hash 59d7dcd0022b3024a572b5f267df04e2cc940c1e6480e01682e9e775d8add851
Name:           qastools
Version:        1.5.0
Release:        1%{?dist}
Summary:        Collection of desktop applications for ALSA
License:        GPL-3.0-only
URL:            https://gitlab.com/sebholt/qastools
Source0:        https://gitlab.com/sebholt/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Requires:       qasconfig%{?_isa} = %{version}-%{release}
Requires:       qashctl%{?_isa} = %{version}-%{release}
Requires:       qasmixer%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(alsa)
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  systemd-devel
# /oreon:deps
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
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%cmake -DSKIP_LICENSE_INSTALL:BOOL=ON
%cmake_build
%install
%cmake_install
for file in %{buildroot}/%{_datadir}/applications/*.desktop; do
    desktop-file-validate $file
done
%find_lang %{name} --with-qt --without-mo
%oreon_autofiles qascommon usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qasconfig usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qashctl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qasmixer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n qascommon -f %{oreon_filedir}/qascommon.list
%files -n qasconfig -f %{oreon_filedir}/qasconfig.list
%files -n qashctl -f %{oreon_filedir}/qashctl.list
%files -n qasmixer -f %{oreon_filedir}/qasmixer.list

%changelog

%autochangelog
