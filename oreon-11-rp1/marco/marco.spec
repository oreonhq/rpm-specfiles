%global source0_hash 2d20820ae9855feb6abc0650300e0c666127bdf0b8380416530703df7f1834ca
%global branch 1.28
Name:          marco
Version:       %{branch}.2
Release:        1%{?dist}
Summary:        MATE Desktop window manager
License:       LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Requires:      mate-desktop-libs
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Provides: firstboot(windowmanager) = marco
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libSM-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXpresent-devel
BuildRequires:  libXres-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libgtop2-devel
BuildRequires:  libsoup-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  startup-notification-devel
BuildRequires:  yelp-tools
BuildRequires:  zenity
# /oreon:deps
%description
MATE Desktop window manager

# to avoid that marco will install in other DE's by compiz-0.8.10
%package libs
Summary:       Libraries for marco
License:       LicenseRef-Callaway-LGPLv2+
%description libs
This package provides Libraries for marco.

%package devel
Summary:       Development files for marco
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development files for marco

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# weird tarball, no generated files
NOCONFIGURE=1 ./autogen.sh

%build

%configure --disable-static           \
           --disable-schemas-compile  \
           --with-x
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags} V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -vf {} ';'
desktop-file-install                                \
        --delete-original                           \
        --dir=%{buildroot}%{_datadir}/applications  \
%{buildroot}%{_datadir}/applications/marco.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n marco-libs -f %{oreon_filedir}/marco-libs.list
%files -n marco-devel -f %{oreon_filedir}/marco-devel.list

%changelog

%autochangelog
