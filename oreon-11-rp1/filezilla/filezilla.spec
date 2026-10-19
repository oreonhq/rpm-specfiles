%global source0_hash fcbeac95571bdfa02a53fea81967c58cc0998006269fb6f1285aee230a5c2587
%define run_autogen 1
%bcond_with storj
Name: filezilla
Version: 3.69.5
Release:        1%{?dist}
Summary:        FTP, FTPS and SFTP client
License: GPL-2.0-or-later
URL: https://filezilla-project.org/
Source0:        https://download.filezilla-project.org/FileZilla_%{version}_src.tar.xz
%if 0%{?run_autogen}
%endif
%if %{with storj}
%endif
Requires: xdg-utils
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  boost-regex
BuildRequires:  cppunit-devel
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel
BuildRequires:  gnutls-devel
BuildRequires:  libappstream-glib
BuildRequires:  libfilezilla-devel
BuildRequires:  libidn-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nettle-devel
BuildRequires:  pugixml-devel
BuildRequires:  sqlite-devel
BuildRequires:  wxGTK-devel
BuildRequires:  xdg-utils
# /oreon:deps
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

export WXRC=%{_bindir}/wxrc-3.2
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
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/fzdefaults.xml
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs
%find_lang %{name}
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
