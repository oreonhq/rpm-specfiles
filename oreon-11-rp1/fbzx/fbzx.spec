%global source0_hash e379dc118a38cd1866219cbba8dddf1d50cacd041135f10d8aee5843234643ee
Name:           fbzx
Version:        4.8.0
Release:        1%{?dist}
Summary:        A ZX Spectrum emulator for FrameBuffer
License:        GPL-3.0-or-later
URL:            https://www.rastersoft.com/programas/fbzx.html
Source0:        %{name}-%{version}-noroms.tar.gz
Source1:        %{name}-generate-tarball.sh
Source2:        README_%{name}.Fedora
Source3:        %{name}.1
Patch0:         %{name}-4.8.0-gcc15.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
FBZX is a Sinclair Spectrum emulator, designed to work at full screen using 
the FrameBuffer or under X-Windows. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix Makefile
sed -i 's/$(CXX) -o/$(CXX) $(CXXFLAGS) -o/' src/Makefile

%build

%set_build_flags
%make_build
%install
%make_install PREFIX=%{_prefix} NOROMS=1
rm -rf %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 data/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
desktop-file-install \
  --delete-original \
  --add-category Emulator \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/*.appdata.xml
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE2} %{buildroot}%{_pkgdocdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
