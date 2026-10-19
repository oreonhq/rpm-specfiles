%global source1_hash 50b079839c4e5a631cf2cf58312b6d0a8cd3028946d57720b33879578721d48f
%global source0_hash 50b079839c4e5a631cf2cf58312b6d0a8cd3028946d57720b33879578721d48f
%global git_revision 9ae8768
%bcond_with	evolution
%bcond_without	bundled_gob2
Name:           mail-notification
Version:        5.4
Release:        1%{?dist}
Summary:        Status icon that informs you if you have new mail
License:        GPL-3.0-or-later
URL:            http://www.nongnu.org/mailnotify/
Source0:        %{name}-%{git_revision}.tar.gz
%if %{with bundled_gob2}
Source1:        http://ftp.5z.com/pub/gob/gob2-2.0.19.tar.gz
%endif
Patch0: mail-notification-jb-gcc-format.patch
Patch2:         mail-notification-evo3_11_2.patch
Patch3:         mail-notification-dont-link-against-bsd-compat.patch
Patch4:         mail-notification-eds3_23_2.patch
Patch5:		mail-notification-gstreamer1.patch
Patch6:		mail-notification-jb-c99.patch
Patch7:		mail-notification-incompatible-pointer-types.patch
Patch8:		mail-notification-maybe-uninitialized.patch
Patch9:		mail-notification-libxml2.patch
Patch10:	mail-notification-gint64.patch
%if %{without bundled_gob2}
%endif
%if %{with evolution}
%endif
%if %{with bundled_gob2}
%endif
Requires:         hicolor-icon-theme
Requires(pre):    GConf2
Requires(post):   GConf2, scrollkeeper
Requires(preun):  GConf2
Requires(postun): scrollkeeper
# oreon:deps
BuildRequires:  GConf2
BuildRequires:  GConf2-devel
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gmime-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libgnome-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libnotify-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  scrollkeeper
# /oreon:deps
%description
Mail Notification is a status icon (aka tray icon) that informs you if you
have new mail. It works with system trays implementing the freedesktop.org
System Tray Specification, such as the GNOME Panel Notification Area, the
Xfce Notification Area and the KDE System Tray.

%if %{with evolution}
%package        evolution-plugin
Summary:        Evolution plugin for Mail Notification
Requires:       %{name} = %{version}-%{release}
%description	evolution-plugin
Evolution support for Mail Notification.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n epienbroek-%{name}-%{git_revision} %{?with_bundled_gob2:-a 1}

%patch -P0 -p1
%patch -P2 -p1 -b .evo3_11_2
%patch -P3 -p0
%patch -P4 -p1 -b .eds3_23_2
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1 -b .incompatible-pointer-types
%patch -P8 -p1 -b .maybe-uninitialized
%patch -P9 -p1 -b .libxml2
%patch -P10 -p0 -b .gint64

# update config.{guess,sub} manually
cp -p /usr/lib/rpm/redhat/config.{guess,sub} jbsrc/tools/

%build

%if %{with bundled_gob2}
mkdir bin
pushd gob2-*
%configure
make
ln src/gob2 ../bin
popd
%endif
export jb_cflags=-Wno-discarded-qualifiers
./jb configure \
  cc="%{__cc}" \
  cflags="$RPM_OPT_FLAGS -Wno-deprecated-declarations" \
  cppflags="-D_GNU_SOURCE -Wno-deprecated-declarations" \
  ldflags="$RPM_LD_FLAGS" \
  destdir=$RPM_BUILD_ROOT \
  prefix=%{_prefix} \
  bindir=%{_bindir} \
  libdir=%{_libdir} \
  libexecdir=%{_libexecdir} \
  datadir=%{_datadir} \
  sysconfdir=%{_sysconfdir} \
  localstatedir=%{_localstatedir} \
  gtk3=yes \
%if %{with evolution}
  evolution=yes \
%else
  evolution=no \
%endif
%if %{with bundled_gob2}
  gob2=$PWD/bin/gob2 \
%endif
  install-gconf-schemas=no
./jb build
cat build/build.log
%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
./jb install
rm -rf $RPM_BUILD_ROOT%{_localstatedir}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
%if %{with evolution}
chmod +x $RPM_BUILD_ROOT%{_libdir}/evolution/plugins/*.so
%endif
desktop-file-install \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/gnome/autostart/  \
  --delete-original                                    \
  ${RPM_BUILD_ROOT}%{_sysconfdir}/xdg/autostart/mail-notification.desktop
desktop-file-install \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications      \
  --delete-original                                    \
  --add-category X-GNOME-NetworkSettings               \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/mail-notification-properties.desktop
%find_lang %{name}
%oreon_autofiles main

%pre

%gconf_schema_prepare %{name}
%post

%gconf_schema_upgrade %{name}
/usr/bin/scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :
%preun

%gconf_schema_remove %{name}
%postun

/usr/bin/scrollkeeper-update -q ||:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
