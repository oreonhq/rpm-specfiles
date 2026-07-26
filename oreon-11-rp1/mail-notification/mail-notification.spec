%global source0_hash 50b079839c4e5a631cf2cf58312b6d0a8cd3028946d57720b33879578721d48f

%global git_revision 9ae8768

%bcond_with	evolution
%bcond_without	bundled_gob2

Name:           mail-notification
Version:        5.4
Release:        116.git.%{git_revision}%{?dist}
Summary:        Status icon that informs you if you have new mail

License:        GPL-3.0-or-later
URL:            http://www.nongnu.org/mailnotify/
#Source0:        http://savannah.nongnu.org/download/mailnotify/mail-notification-%{version}.tar.bz2
# Upstream isn't alive any more, use a github forked copy which contains all patches which
# have been collected over the past years: https://github.com/epienbroek/mail-notification
#
# To regenerate source tarball:
# wget https://github.com/epienbroek/mail-notification/tarball/$git_revision -O mail-notification-$git_revision.tar.gz
Source0:        mail-notification-%{git_revision}.tar.gz

%if %{with bundled_gob2}
Source1:        http://ftp.5z.com/pub/gob/gob2-2.0.19.tar.gz
%endif

# jb build system is turning on -Werror to build itself.  This patch fixes a
# warning with current gcc
Patch0: mail-notification-jb-gcc-format.patch

# build break when building with evolution 3.11.2
Patch2:         mail-notification-evo3_11_2.patch

# Fix FTBFS against latest glibc
Patch3:         mail-notification-dont-link-against-bsd-compat.patch

# Build against evolution-data-server 3.23.2
Patch4:         mail-notification-eds3_23_2.patch

# Use gstreamer-1.0 to play sound
Patch5:		mail-notification-gstreamer1.patch

Patch6:		mail-notification-jb-c99.patch
Patch7:		mail-notification-incompatible-pointer-types.patch
Patch8:		mail-notification-maybe-uninitialized.patch
Patch9:		mail-notification-libxml2.patch
Patch10:	mail-notification-gint64.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  desktop-file-utils, scrollkeeper
BuildRequires:  openssl-devel >= 0.9.6
BuildRequires:  cyrus-sasl-devel >= 2.0
BuildRequires:  glib2-devel >= 2.14
BuildRequires:  gtk3-devel
BuildRequires:  GConf2-devel, libgnome-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  libnotify-devel >= 0.4.1
BuildRequires:  gmime-devel >= 2.4
BuildRequires:  libgnome-keyring-devel
BuildRequires:  perl-XML-Parser
%if %{without bundled_gob2}
BuildRequires:  gob2 >= 2.0.17
%endif
%if %{with evolution}
BuildRequires:  evolution-devel >= 3.45.1
BuildRequires:  evolution-data-server-devel >= 3.45.1
%endif

# needed for the gtk-builder-convert tool
BuildRequires:  gtk2-devel

# needed for the GConf RPM macros
BuildRequires:  GConf2

%if %{with bundled_gob2}
BuildRequires: bison, flex, flex-static
%endif

Requires:         hicolor-icon-theme

Requires(pre):    GConf2
Requires(post):   GConf2, scrollkeeper
Requires(preun):  GConf2
Requires(postun): scrollkeeper

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

# The build command above hides away all gcc commands and their warnings
# As they can be interesting show the build log manually
cat build/build.log

%install
# For GConf apps: prevent schemas from being installed at this stage
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

./jb install

#  clear /var/lib/scrollkeeper stuff here
rm -rf $RPM_BUILD_ROOT%{_localstatedir}

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%if %{with evolution}
chmod +x $RPM_BUILD_ROOT%{_libdir}/evolution/plugins/*.so
%endif

desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
  --vendor fedora                   \
%endif
  --dir ${RPM_BUILD_ROOT}%{_datadir}/gnome/autostart/  \
  --delete-original                                    \
  ${RPM_BUILD_ROOT}%{_sysconfdir}/xdg/autostart/mail-notification.desktop

desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
  --vendor fedora                   \
%endif
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications      \
  --delete-original                                    \
  --add-category X-GNOME-NetworkSettings               \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/mail-notification-properties.desktop

%find_lang %{name}

%pre
%gconf_schema_prepare %{name}

%post
%gconf_schema_upgrade %{name}
/usr/bin/scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

%preun
%gconf_schema_remove %{name}

%postun
/usr/bin/scrollkeeper-update -q ||:

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README TODO
%{_sysconfdir}/gconf/schemas/mail-notification.schemas
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/gnome/autostart/*mail-notification.desktop
%{_datadir}/applications/*mail-notification-properties.desktop
%{_datadir}/gnome/help/mail-notification/
%dir %{_datadir}/omf/mail-notification/
%{_datadir}/omf/mail-notification/mail-notification-C.omf
%{_datadir}/icons/hicolor/*/apps/mail-notification.*

%if %{with evolution}
%files evolution-plugin
%{_libdir}/evolution/plugins/*
%endif

%changelog
%autochangelog
