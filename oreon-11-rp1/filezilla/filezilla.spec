%global source0_hash fcbeac95571bdfa02a53fea81967c58cc0998006269fb6f1285aee230a5c2587

# Enable (1 = enabled/0 = disabled) if configure regeneration etc. is required.
%define run_autogen 1

# Needs not yet packaged storj/uplink-c
%bcond_with storj

Name: filezilla
Version: 3.69.5
Release: 3%{?dist}
Summary: FTP, FTPS and SFTP client
License: GPL-2.0-or-later
URL: https://filezilla-project.org/

Source0: https://download.filezilla-project.org/FileZilla_%{version}_src.tar.xz

%if 0%{?rhel} == 8
# libuv-devel not present on s390x on EL-8
ExcludeArch: s390x
%endif

%if 0%{?run_autogen}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
%endif
BuildRequires: boost-devel
BuildRequires: boost-regex
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: glib2-devel
BuildRequires: cppunit-devel >= 1.13.0
BuildRequires: dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gnutls-devel >= 2.8.3
BuildRequires: libappstream-glib
BuildRequires: libfilezilla-devel >= 0.35.0
BuildRequires: libidn-devel
%if %{with storj}
BuildRequires: golang-storj-uplink-c-devel
%endif
BuildRequires: nettle-devel
BuildRequires: pugixml-devel >= 1.7
BuildRequires: sqlite-devel
BuildRequires: wxGTK-devel
BuildRequires: xdg-utils
BuildRequires: make

Requires: xdg-utils

%description
FileZilla is a FTP, FTPS and SFTP client for Linux with a lot of features.
- Supports FTP, FTP over SSL/TLS (FTPS) and SSH File Transfer Protocol (SFTP)
- Cross-platform
- Available in many languages
- Supports resume and transfer of large files greater than 4GB
- Easy to use Site Manager and transfer queue
- Drag & drop support
- Speed limits
- Filename filters
- Network configuration wizard 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{version}
%if 0%{?run_autogen}
autoreconf -if
%endif

%build
# For wxGTK3 - needed to find wxrc
export WXRC=%{_bindir}/wxrc-3.2

# Do not use '--enable-buildtype=official' in configure. That option enables the
# "check for updates" dialog to download new binaries from the official website.
%configure \
  --disable-static \
  --enable-locales \
  --disable-manualupdatecheck \
  --with-pugixml=system \
  --with-wx-config=wx-config-3.2 \
  --with-dbus \
  --enable-gnutlssystemciphers \
%if %{with storj}
  --enable-storj \
%endif
  --disable-autoupdatecheck
%make_build

%install
%make_install

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/appdata/filezilla.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/filezilla/a.png 

for i in 16x16 32x32 48x48 ; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}/apps
  ln -sf ../../../../%{name}/resources/${i}/%{name}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}/apps/%{name}.png
done

rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps

desktop-file-install \
  --delete-original \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT/%{_datadir}/appdata/%{name}.appdata.xml

# Create directory for system wide settings.
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
# Ghost configuration file.
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/fzdefaults.xml
# This is not the usual docdir.
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%find_lang %{name}

%check
%make_build check

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%doc docs/fzdefaults.xml.example
%license COPYING
%dir %{_sysconfdir}/%{name}
%ghost %{_sysconfdir}/%{name}/fzdefaults.xml
%{_bindir}/%{name}
%{_bindir}/fzputtygen
%{_bindir}/fzsftp
%if %{with storj}
%{_bindir}/fzstorj
%endif
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_libdir}/libfzclient-private*
%{_libdir}/libfzclient-commonui*

%changelog
%autochangelog
