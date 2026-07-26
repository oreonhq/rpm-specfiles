%global source0_hash 0c4e737f9086042bde8b5aa9074191c15f1f72de92446b100ffccbe929d263c5

Name:           taxipilot
Version:        0.9.2
Release:        48%{?dist}
Summary:        Game where you pilot a taxi in space
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://taxipilot.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Patch1:         taxipilot-0.9.1-desktop.patch
Patch2:         taxipilot-0.9.1-weaksym.patch
Patch3:         taxipilot-0.9.2-arts-startup.patch
Patch4:         taxipilot-0.9.2-gcc45.patch
BuildRequires: make
BuildRequires:  gcc gcc-c++ kdelibs3-devel arts-devel
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
Game where you pilot a taxi in space, the objective is to pick up passengers
waiting on a number of platforms and to drop them where they want to go.
That's basically it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
. /etc/profile.d/qt.sh
%configure --disable-rpath
# Remove useless /usr/lib64 rpath on 64bit archs
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build taxipilot_LDADD="./EXT_wavpo/libEXT_wavpo.la -lartskde -lkdeui -lkdecore -lartsflow_idl -lmcop -lkio $(pkg-config --libs qt-mt)"

%install
. /etc/profile.d/qt.sh
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm $RPM_BUILD_ROOT%{_libdir}/libEXT_wavpo.so
%find_lang %{name}

# install .desktop file and appdata.
desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applnk/Games/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_bindir}/%{name}*
%{_libdir}/libEXT_wavpo.*
%{_libdir}/mcop/EXT_WavPlayObject.mcopclass
%{_datadir}/apps/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/??color/*/apps/%{name}.png
%{_datadir}/doc/HTML/en/%{name}

%changelog
%autochangelog
