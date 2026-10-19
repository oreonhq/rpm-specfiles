%global source0_hash 193db04f176795d0177665b3c62675742b6c73c10ccf193f657bb9d2d8242d16
%if 0%{!?_with_xfce:1} && 0%{!?_without_xfce:1}
%global _with_xfce 1
%endif
Name:		im-chooser
Version:	1.7.6
Release:        1%{?dist}
License:	GPL-2.0-or-later AND LGPL-2.0-or-later
URL:		http://pagure.io/im-chooser/
%{?_with_gtk2:BuildRequires:	gtk2-devel}
%{!?_with_gtk2:BuildRequires:	gtk3-devel}
%if 0%{?_with_xfce}
%endif
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2
Summary:        Desktop Input Method configuration tool
Obsoletes:	im-chooser-gnome3 < 1.4.2-2
Provides:	im-chooser-gnome3 = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  imsettings-devel
BuildRequires:  libSM-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  make
# /oreon:deps
%description
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

%package	common
Summary:	Common files for im-chooser subpackages
Requires:	imsettings >= 1.8.9
Obsoletes:	im-chooser < 1.5.0.1
Provides:	bundled(egglib)
%description	common
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

This package contains the common libraries/files to be used in
im-chooser subpackages.

%if 0%{?_with_xfce}
%package	xfce
Summary:	XFCE settings panel for im-chooser
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	im-chooser < 1.5.0.1
%description	xfce
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

This package contains the XFCE settings panel for im-chooser.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/im-chooser.desktop
%if 0%{?_with_xfce}
desktop-file-validate %{buildroot}%{_datadir}/applications/xfce4-im-chooser.desktop
%endif
rm -rf %{buildroot}%{_libdir}/libimchooseui.{so,la,a}
rm -rf %{buildroot}%{_libdir}/control-center-1/panels/libim-chooser.so
rm -rf %{buildroot}%{_datadir}/applications/im-chooser-panel.desktop
%find_lang %{name}
%ldconfig_scriptlets	common
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n im-chooser-common -f %{oreon_filedir}/im-chooser-common.list
%files -n im-chooser-xfce -f %{oreon_filedir}/im-chooser-xfce.list

%changelog

%autochangelog
