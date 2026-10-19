%global source0_hash 3064e84967b4b4216f5c7e065cfec8c52019438a590e9ed81366af2770660944
%define gconf2_version 2.14
Summary:        Editor/admin tool for GConf
Name: gconf-editor
Version: 3.0.1
Release:        1%{?dist}
URL: http://www.gnome.org
Source0:        http://download.gnome.org/sources/gconf-editor/3.0/%{name}-%{version}.tar.xz
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
Requires(pre): GConf2 >= %{gconf2_version}
Requires(post): GConf2 >= %{gconf2_version}
Requires(preun): GConf2 >= %{gconf2_version}
# oreon:deps
BuildRequires:  GConf2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gnome-common
BuildRequires:  gnome-doc-utils
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  scrollkeeper
# /oreon:deps
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
rm -rf $RPM_BUILD_ROOT/var/scrollkeeper
%find_lang %{name} --with-gnome
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
