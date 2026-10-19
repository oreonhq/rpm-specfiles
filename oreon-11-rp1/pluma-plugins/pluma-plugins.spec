%global source0_hash a47e8637366fffb1ba968d873f3965c988c3e620bb13362817b4be7d722a0baa
%global branch 1.28
%global __provides_exclude_from ^%{_libdir}/pluma/plugins
Summary:        Modules for the pluma text editor
Name:          pluma-plugins
Version:       %{branch}.0
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           https://mate-desktop.org
Source0:        https://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Requires:      %{name}-data = %{version}-%{release}
Requires:      pluma
Requires:      python3-dbus
Requires:      libpeas-loader-python3
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  libpeas-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  pluma-devel
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  vte291-devel
BuildRequires:  yelp-tools
# /oreon:deps
%description
Modules for the pluma text editor

%package data
Summary:   Data files for pluma-plugins
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}
%description data
This package contains shared data needed for pluma-plugins.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
        --enable-verify-all   \
        --enable-python       \
        --enable-deprecations
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pluma-plugins-data -f %{oreon_filedir}/pluma-plugins-data.list

%changelog

%autochangelog
