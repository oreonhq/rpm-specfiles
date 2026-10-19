%global source0_hash 1df2549f25a84f9237620fbf0c9cba65080e49c76025bd50ce530cfd00f3eab5
Name:           genius
Version:        1.0.29
Release:        1%{?dist}
Summary:        An arbitrary precision integer and multiple precision floatingpoint calculator
License:        GPL-3.0-or-later
URL:            https://www.jirka.org/genius.html
Source0:        https://download.gnome.org/sources/genius/1.0/genius-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gmp-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  pkgconfig
BuildRequires:  popt
BuildRequires:  readline-devel
BuildRequires:  vte291-devel
# /oreon:deps
%description
Genius is a calculator program similar in some aspects to BC, Matlab
or Maple. GEL is the name of its extension language, in fact, a large
part of the standard genius functions are written in GEL itself.

%package devel
Summary:        Development files for Genius
Requires:       %{name} = %{version}-%{release}
%description devel
Development files for Genius.

%package -n gnome-genius
Summary:        GNOME frontend for Genius
Requires:       %{name} = %{version}-%{release}
%description -n gnome-genius
GNOME frontend for Genius.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#sed -i "s|Mime-Type|MimeType|" src/gnome-genius.desktop*
find -name \*.c | xargs chmod 0644

%build

%configure --disable-update-mimedb
%make_build
%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_libdir}
rm -f $RPM_BUILD_ROOT%{_datadir}/genius/plugins/test.plugin
rm -rf $RPM_BUILD_ROOT%{_datadir}/application-registry
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info
rm -rf $RPM_BUILD_ROOT/var
desktop-file-install \
    --add-category Utility \
    --remove-category Office \
    --remove-category Scientific \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    --delete-original \
    $RPM_BUILD_ROOT%{_datadir}/applications/gnome-genius.desktop
%find_lang %{name}
%oreon_autofiles gnome-genius usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n genius-devel -f %{oreon_filedir}/genius-devel.list
%files -n gnome-genius -f %{oreon_filedir}/gnome-genius.list

%changelog

%autochangelog
