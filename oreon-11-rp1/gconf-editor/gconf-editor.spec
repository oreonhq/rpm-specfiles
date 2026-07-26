%global source0_hash 3064e84967b4b4216f5c7e065cfec8c52019438a590e9ed81366af2770660944

%define gconf2_version 2.14

Summary: Editor/admin tool for GConf
Name: gconf-editor
Version: 3.0.1
Release: 34%{?dist}
URL: http://www.gnome.org
#VCS: git:git://git.gnome.org/gconf-editor
Source0: http://download.gnome.org/sources/gconf-editor/3.0/%{name}-%{version}.tar.xz
# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL

Requires(pre): GConf2 >= %{gconf2_version}
Requires(post): GConf2 >= %{gconf2_version}
Requires(preun): GConf2 >= %{gconf2_version}

BuildRequires: GConf2-devel
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils
BuildRequires: scrollkeeper
BuildRequires: gettext
BuildRequires: gnome-doc-utils
BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: autoconf automake libtool
BuildRequires: make

%description
gconf-editor allows you to browse and modify GConf configuration
sources.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-scrollkeeper
make %{?_smp_mflags}

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# stuff we don't want
rm -rf $RPM_BUILD_ROOT/var/scrollkeeper

%find_lang %{name} --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gconf-editor.desktop

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/gconf-editor.schemas > /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/gconf-editor.schemas > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/gconf-editor.schemas > /dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/gconf-editor
%{_datadir}/icons/hicolor/*/apps/gconf-editor.png
%{_datadir}/gconf-editor
%{_datadir}/applications/gconf-editor.desktop
%{_mandir}/man1/gconf-editor.1.gz
%{_sysconfdir}/gconf/schemas/gconf-editor.schemas
%dir %{_datadir}/omf/gconf-editor

%changelog
%autochangelog
