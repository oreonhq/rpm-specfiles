%global source0_hash 8c7ce27f4b826c0830a5d5620ced9c721194c8b3614573072dd686509c7f8df4

Name:           koverartist
Version:        0.7.6
Release:        34%{?dist}
Summary:        Create CD/DVD covers
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.kde-apps.org/content/show.php?content=38195
Source0:        http://kde-apps.org/CONTENT/content-files/38195-%{name}_%{version}.orig.tar.bz2
Patch0:         koverartist-0.7.6-gcc47.patch
BuildRequires:  kdelibs4-devel gettext desktop-file-utils cmake

# Required by configure
BuildRequires:  /usr/bin/perl perl(Getopt::Long)
BuildRequires: make

%description
KoverArtist is a program for the fast creation of covers for
cd/dvd cases and boxes. The main idea behind it is to be able
to create decent looking covers with some mouseclicks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gcc47

%build
%configure --disable-rpath
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/kde4/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/koverartist
%{_datadir}/icons/hicolor/*/apps/koverartist.png
%{_datadir}/applications/kde4/koverartist.desktop
%{_datadir}/kde4/apps/%{name}/
%{_datadir}/mime/packages/mime-types/x-koa*.xml

%changelog
%autochangelog
