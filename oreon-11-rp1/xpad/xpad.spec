%global source0_hash f26052308850c406b15adb8d86acd3962ef10af22b427bb1a5cff4eec96f82e9

Name:           xpad
Version:        5.8.0
Release:        12%{?dist}
Summary:        Sticky notepad for GTK

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://launchpad.net/xpad
Source0:        https://launchpad.net/xpad/trunk/%{version}/+download/%{name}-%{version}.tar.bz2

Patch1:         xpad-5.8.0-gettext-version.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libSM-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  gtksourceview4-devel
BuildRequires:  libayatana-appindicator-gtk3-devel
BuildRequires:  autoconf
BuildRequires:  libappstream-glib

%description
Xpad is a sticky note application that strives to be simple, fault-tolerant, 
and customizable. It consists of independent pad windows; each is basically a 
text box in which notes can be written. Despite being called xpad, all that is
needed to run or compile it is the GTK+ 2.0 libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh
%configure

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

# desktop file stuff
desktop-file-install  \
        --delete-original \
        --dir=%{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/xpad
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/xpad.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
