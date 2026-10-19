%global source0_hash 02f09eb0314c2ac197b6f089950a571cdba39bfd03d6c3a0b8fd77252a968874
%global branch 1.28
Name:          mate-panel
Version:       %{branch}.4
Release:        1%{?dist}
Summary:        MATE Desktop panel and applets
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Source1:       mate-panel_fedora-30.layout
Source2:       mate-panel_rhel.layout
Source3:       mate-panel_fedora-40.layout
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:    fortune-mod
Requires:      caja-schemas
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  gtk3-devel
BuildRequires:  libSM-devel
BuildRequires:  libmateweather-devel
BuildRequires:  libwnck3-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-menus-devel
BuildRequires:  wayland-devel
BuildRequires:  yelp-tools
# /oreon:deps
%description
MATE Desktop panel applets

%package libs
Summary:     Shared libraries for mate-panel
License:     LGPLv2+
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description libs
Shared libraries for libmate-desktop

%package devel
Summary:     Development files for mate-panel
Requires:    %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development files for mate-panel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure                                        \
           --disable-static                       \
           --disable-schemas-compile              \
           --libexecdir=%{_libexecdir}/mate-panel \
           --enable-introspection                 \
           --disable-gtk-doc                      \
           --enable-x11                           \
           --enable-wayland                       \
           --with-in-process-applets=all
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
(
  cd po
  make mate-panel.pot-update
  make update-po
  for f in mate-panel.pot *.po
  do
    sed -i '/^#, /d' $f
  done
  make update-gmo
)
make %{?_smp_mflags} V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/mate-panel.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mate-panel-libs -f %{oreon_filedir}/mate-panel-libs.list
%files -n mate-panel-devel -f %{oreon_filedir}/mate-panel-devel.list

%changelog

%autochangelog
