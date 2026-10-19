%global source0_hash 6e70590dfed324e6d6ac813e33d9f9dcfaa13b2f57fdec9e178e9dda05538cb0
Name:           milkytracker
Version:        1.06
Release:        1%{?dist}
Summary:        Module tracker software for creating music
License:        GPL-3.0-or-later
URL:            http://www.milkytracker.org/
Source0:        https://github.com/milkytracker/MilkyTracker/archive/v%{version}.tar.gz
Patch0:         milkytracker-1.03.00-c++11.patch
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  rtmidi-devel
BuildRequires:  zlib-devel
BuildRequires:  zziplib-devel
# /oreon:deps
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
mv -v %{buildroot}%{_docdir}/MilkyTracker %{buildroot}%{_pkgdocdir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p resources/pictures/carton.png %{buildroot}%{_datadir}/pixmaps/milkytracker.png
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ resources/milkytracker.desktop
install -v -D -m 644 resources/milkytracker.appdata %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
