%global source0_hash 3580b72e0a0b5e72505117194dcdb11cecce95ea2dad6b4e11330181a75fdaa5

Name:          xlog
Version:       2.0.25
Release:       6%{?dist}
Summary:       Logging program for Hamradio Operators

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:       GPL-3.0-only
URL:           http://www.nongnu.org/xlog/
Source0:       http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:       org.nongnu.Xlog.metainfo.xml

Patch0:        %{name}-2.0.19-no-error.patch
Patch1:        xlog-%{version}-hamlib42.patch
Patch2:        %{name}-2.0.25-aclocal.patch

ExcludeArch:   i686

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gtk2-devel
BuildRequires: hamlib-devel
BuildRequires: shared-mime-info
BuildRequires: gettext-devel
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme

%description
xlog is a logging program for amateur radio operators. The log is stored
into a text file. QSO's are presented in a list. Items in the list can be
added, deleted or updated. For each contact, dxcc information is displayed
and bearings and distance is calculated, both short and long path.
xlog supports trlog, adif, cabrillo, edit, twlog and editest files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
#fix bogus .desktop file
sed -i -e "s/Utility;Database;HamRadio;GTK/Network;HamRadio;GTK/g" $RPM_BUILD_DIR/%{name}-%{version}/data/desktop/xlog.desktop
sed -i -e "s/.png//g" $RPM_BUILD_DIR/%{name}-%{version}/data/desktop/xlog.desktop

%build
autoreconf -vif
%configure CFLAGS="%{optflags} -lm" --enable-hamlib --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/mimeinfo.cache

%find_lang %{name}

# Install desktop file
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        $RPM_BUILD_ROOT%{_datadir}/applications/xlog.desktop
desktop-file-edit --set-key=Icon --set-value=%{name} $RPM_BUILD_ROOT%{_datadir}/applications/xlog.desktop

# Install svg icon
install -D -p -m644 data/pixmaps/xlog.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Install AppStream metainfo file
install -D -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/org.nongnu.Xlog.metainfo.xml

%files -f %{name}.lang
%doc AUTHORS data/doc/BUGS ChangeLog COPYING NEWS README data/doc/TODO data/doc/manual data/doc/KEYS data/glabels
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dxcc
%{_datadir}/%{name}/maps
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/*.desktop
%{_metainfodir}/org.nongnu.Xlog.metainfo.xml
%{_datadir}/mime/packages/*.xml
%{_mandir}/man?/*

%changelog
%autochangelog
