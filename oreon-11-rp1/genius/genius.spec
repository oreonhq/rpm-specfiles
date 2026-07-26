%global source0_hash 0243b7c36b5f9e930c62778acd52deb188deeca704a5e195337018435d9e7bb5

Name:           genius
Version:        1.0.27
Release:        3%{?dist}
Summary:        An arbitrary precision integer and multiple precision floatingpoint calculator

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://www.jirka.org/genius.html
Source0:        https://download.gnome.org/sources/genius/1.0/genius-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  vte291-devel
BuildRequires:  readline-devel
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  popt
BuildRequires:  pkgconfig
BuildRequires:  intltool
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires: make

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

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%exclude %{_datadir}/genius/gtksourceview
%{_bindir}/genius
%{_datadir}/genius

%files devel
%{_includedir}/genius

%files -n gnome-genius
%{_bindir}/gnome-genius
%{_libexecdir}/*
%{_datadir}/genius/gtksourceview
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/gnome-genius.svg
%{_datadir}/mime/packages/*
%{_datadir}/applications/*

%changelog
%autochangelog
