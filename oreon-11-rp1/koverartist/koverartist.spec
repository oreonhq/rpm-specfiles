%global source0_hash 8c7ce27f4b826c0830a5d5620ced9c721194c8b3614573072dd686509c7f8df4
Name:           koverartist
Version:        0.7.6
Release:        1%{?dist}
Summary:        Create CD/DVD covers
License:        GPL-2.0-or-later
URL:            http://www.kde-apps.org/content/show.php?content=38195
Source0:        http://kde-apps.org/CONTENT/content-files/38195-%{name}_%{version}.orig.tar.bz2
Patch0:         koverartist-0.7.6-gcc47.patch
# oreon:deps
BuildRequires:  /usr/bin/perl
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  make
BuildRequires:  perl(Getopt::Long)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
