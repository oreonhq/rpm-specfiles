%global source0_hash none

%undefine __cmake_in_source_build

Name:           xiphos
Version:        4.3.2
Release:        5%{?dist}
Summary:        Bible study and research tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://xiphos.org/
Source0:        https://github.com/crosswire/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  biblesync-devel >= 2.0.1-3
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dbus-glib-devel
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  libuuid-devel
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  rarian-compat
BuildRequires:  sword-devel >= 1.8
BuildRequires:  util-linux
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  yelp-tools
BuildRequires:  libzip-devel
Requires:       yelp
Obsoletes:      xiphos-gtk2 < 4.1
Obsoletes:      xiphos-gtk3 < 4.1
Obsoletes:      xiphos-common < 4.1

%if 0%{?rhel} > 0 && 0%{?rhel} <= 7
ExcludeArch: ppc64
%endif

%description
Xiphos is a Bible study tool written for Linux,
UNIX, and Windows under the GNOME toolkit, offering a rich and featureful
environment for reading, study, and research using modules from The SWORD
Project and elsewhere.

%prep
%setup -q
rm -rf src/biblesync

%build
export CFLAGS="$CFLAGS -fPIC"
export CXXFLAGS="$CXXFLAGS -fPIC"
%ifarch %{power64}
 CFLAGS="$CFLAGS -D__SANE_USERSPACE_TYPES__"
 CXXFLAGS="$CXXFLAGS -D__SANE_USERSPACE_TYPES__"
%endif
export CXXFLAGS
export CFLAGS

LDFLAGS='%{?__global_ldflags}' \
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    %{nil}
%cmake_build

%install
%cmake_install

desktop-file-install --delete-original         \
    --add-category=X-Bible                     \
    --add-category=X-Religion                  \
    --dir=%{buildroot}%{_datadir}/applications \
    --copy-name-to-generic-name                \
    %{buildroot}%{_datadir}/applications/xiphos.desktop

# package docs with macro
rm -frv %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md RELEASE-NOTES TODO
%license COPYING
%{_bindir}/xiphos
%{_bindir}/xiphos-nav
%{_datadir}/metainfo/xiphos.appdata.xml
%{_datadir}/applications/xiphos.desktop
%{_datadir}/icons/hicolor/scalable/apps/xiphos.svg
%{_datadir}/xiphos/
%{_datadir}/help/C/xiphos
%{_datadir}/help/fa/xiphos
%{_datadir}/help/fr/xiphos
%{_datadir}/help/it/xiphos
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/%{name}-nav.1.gz

%changelog
%autochangelog
