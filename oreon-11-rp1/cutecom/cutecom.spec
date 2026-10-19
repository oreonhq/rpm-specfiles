%global source0_hash 679ed0492fb9b36e48c7361e5c00dd0d3a264df431fb01b1c4181da86fcf2a16
%undefine __cmake_in_source_build
%global commit cce2e5ec01df09ca4b05f055f21942e0de7eb7dd
Name:    cutecom
Version: 0.51.0
Summary:        A graphical serial terminal, like minicom or Hyperterminal on Windows
Release:        1%{?dist}
License: GPL-3.0-only
URL:     http://gitlab.com/cutecom/cutecom
Source0:        https://gitlab.com/%{name}/%{name}/-/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:  3944c431-add-appdata.patch
Patch1:  cutecom-0.51.0-desktopfix.patch
Patch2:  cutecom-0.51.0-painterpath.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtserialport-devel
# /oreon:deps
%description
CuteCom is a graphical serial terminal, like minicom or Hyperterminal on 
Windows. It is aimed mainly at hardware developers or other people who need 
a terminal to talk to their devices. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}-%{commit}

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
install -p -D -m 644 $(pwd)/cutecom.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/cutecom.1
install -p -D -m 644 com.gitlab.cutecom.cutecom.appdata.xml %{buildroot}%{_metainfodir}/cutecom.appdata.xml
install -p -D -m 644 images/cutecom.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/cutecom.svg
desktop-file-install \
   --remove-key=Path --remove-key=Encoding \
   --remove-key=BinaryPattern --remove-key=TerminalOptions \
   --add-category=System \
   --dir ${RPM_BUILD_ROOT}%{_datadir}/applications/ \
   $(pwd)/cutecom.desktop
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
