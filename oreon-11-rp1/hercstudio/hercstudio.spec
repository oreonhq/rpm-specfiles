%global source0_hash 532cf5cffc6a8d16a0862cb1c03cb54f0bd4d2d7f0ea334f88b2c7a34714e5d0

Name:           hercstudio
Version:        1.6.0
Release:        2%{?dist}
Summary:        GUI front-end to the Hercules mainframe Emulator

License:        GPL-3.0-or-later
URL:            https://hercstudio.sourceforge.io/
Source0:        %{url}/herculesstudio-%{version}-src.tar.gz
# borrowed from Debian
Source1:        HerculesStudio.1

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  sed

BuildRequires:  cmake(Qt6)

Requires:       (hercules or sdl-hercules)

%description
GUI front-end to the Hercules mainframe Emulator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n master -p1

# Do not clobber the compiler flags
sed -i '/CMAKE_CXX_FLAGS/d' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_prefix}/local
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 %{SOURCE1}
install -Dpm0644 -t %{buildroot}%{_metainfodir} %{name}.appdata.xml
install -Dpm0644 HercStudio/icons/tray.xpm \
  %{buildroot}%{_datadir}/pixmaps/HerculesStudio.xpm
desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
  hercules-studio.desktop

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license COPYING
%{_bindir}/HerculesStudio
%{_datadir}/applications/hercules-studio.desktop
%{_datadir}/pixmaps/HerculesStudio.xpm
%{_mandir}/man1/HerculesStudio.1*
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
