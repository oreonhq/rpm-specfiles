%global source0_hash 2c10f6bb9f72b0d49e0abfde6867a825e620bdd8561bf115758713201cdd80a7
%undefine __cmake_in_source_build
Name:           xiphos
Version:        4.3.2
Release:        5%{?dist}
Summary:        Bible study and research tool
License:        GPL-2.0-or-later
URL:            http://xiphos.org/
Source0:        https://github.com/crosswire/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Requires:       yelp
Obsoletes:      xiphos-gtk2 < 4.1
Obsoletes:      xiphos-gtk3 < 4.1
Obsoletes:      xiphos-common < 4.1
# oreon:deps
BuildRequires:  biblesync-devel
BuildRequires:  cmake
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  libuuid-devel
BuildRequires:  libzip-devel
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  rarian-compat
BuildRequires:  sword-devel
BuildRequires:  util-linux
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  yelp-tools
# /oreon:deps
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
rm -frv %{buildroot}%{_docdir}/%{name}
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
