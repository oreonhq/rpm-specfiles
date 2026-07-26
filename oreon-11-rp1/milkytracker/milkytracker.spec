%global source0_hash 72d5357e303380b52383b66b51f944a77cd77e2b3bfeb227d87cc0e72ab292f7

Name:           milkytracker
Version:        1.03.00
Release:        14%{?dist}
Summary:        Module tracker software for creating music

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.milkytracker.org/
Source0:        https://github.com/milkytracker/MilkyTracker/archive/v%{version}.tar.gz
Patch0:         milkytracker-1.03.00-c++11.patch

BuildRequires: make
BuildRequires:  SDL2-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  rtmidi-devel
BuildRequires:  zlib-devel
BuildRequires:  zziplib-devel
BuildRequires:  jack-audio-connection-kit-devel

%description
MilkyTracker is an application for creating music in the .MOD and .XM formats.
Its goal is to be free replacement for the popular Fasttracker II software.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MilkyTracker-%{version}
%patch -P0 -p1

find . -regex '.*\.\(cpp\|h\|inl\)' -print0 | xargs -0 chmod 644

%build
%{cmake} -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
rm -rf %{buildroot}
cd %{_vpath_builddir}
make install DESTDIR=%{buildroot}
cd ..

# move the documentation directory (version 1.01.00 started installing
# it as MilkyTracker instead of milkytracker and we want to keep the
# name in sync with the package name)
mv -v %{buildroot}%{_docdir}/MilkyTracker %{buildroot}%{_pkgdocdir}

# copy the icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p resources/pictures/carton.png %{buildroot}%{_datadir}/pixmaps/milkytracker.png

# copy the desktop file
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ resources/milkytracker.desktop

# copy the appdata file
install -v -D -m 644 resources/milkytracker.appdata %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%{_bindir}/milkytracker
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/milkytracker.png
%{_datadir}/%{name}
%{_pkgdocdir}

%changelog
%autochangelog
