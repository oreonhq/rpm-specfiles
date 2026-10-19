%global source0_hash 5d2e58483c2b23d33503d24c88f8b90a28cc0189d7e4001b3e273a604f6fe80e
%global branch 1.28
Name:          libmatekbd
Version:       %{branch}.0
Release:        1%{?dist}
Summary:        Libraries for mate kbd
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtk3-devel
BuildRequires:  libICE-devel
BuildRequires:  libxklavier-devel
BuildRequires:  make
BuildRequires:  mate-common
# /oreon:deps
%description
Libraries for matekbd

%package devel
Summary:  Development libraries for libmatekbd
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development libraries for libmatekbd

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

NOCONFIGURE=1 ./autogen.sh

%build

%configure                   \
   --disable-static          \
   --disable-schemas-compile \
   --with-x                  \
   --enable-introspection=yes
make %{?_smp_mflags} V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -fv {} ';'
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmatekbd-devel -f %{oreon_filedir}/libmatekbd-devel.list

%changelog

%autochangelog
