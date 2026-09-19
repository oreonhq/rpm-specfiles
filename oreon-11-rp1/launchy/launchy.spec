%global source0_hash 93ec471423b77973a2118eaec64c7a1c05ce37b5bff41760336ebd14fc819500

Name:           launchy
Version:        2.5
Release:        45%{?dist}
Summary:        Open Source Keystroke Launcher

License:        GPL-1.0-or-later
URL:            http://www.launchy.net
Source0:        http://www.launchy.net/downloads/src/launchy-2.5.tar.gz

Patch0:         %{name}-X11-lib.patch
Patch1:         %{name}-xdg-icon-path.patch

BuildRequires:  gcc-c++
BuildRequires:  qt-devel boost-devel
BuildRequires:  desktop-file-utils
BuildRequires: make

%description
Launchy is a free cross-platform utility designed to help you forget about your
start menu, the icons on your desktop, and even your file manager.
Launchy indexes the programs in your start menu and can launch your documents,
project files, folders, and bookmarks with just a few keystrokes!

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
# convert DOS to UNIX
%{__sed} -i 's/\r//' LICENSE.txt readme.txt

%build
%{_libdir}/qt4/bin/qmake "CONFIG+=debug" Launchy.pro
make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
# prefix is hardcoded in the makefile 
install -Dpm 0755 debug/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
install -Dpm 0755 debug/plugins/*so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/
install -Dpm 0755 release/plugins/*so $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/icons/
install -Dpm 0644 plugins/*/*png $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/icons/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -Dpm 0644 misc/Launchy_Icon/launchy_icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/
install -dpm 0755 skins $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/
install -dpm 0755 skins/Black_Glass $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Black_Glass
install -dpm 0755 skins/Spotlight_Wide $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Spotlight_Wide
install -dpm 0755 skins/Simple $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Simple
install -dpm 0755 skins/Note $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Note
install -dpm 0755 skins/Default $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Default
install -dpm 0755 skins/Mercury_Wide $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Mercury_Wide
install -dpm 0755 skins/Black_Glass_Wide $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Black_Glass_Wide
install -dpm 0755 skins/Mercury $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Mercury
install -dpm 0755 skins/QuickSilver2 $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/QuickSilver2
install -Dpm 0644 skins/Black_Glass/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Black_Glass
install -Dpm 0644 skins/Spotlight_Wide/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Spotlight_Wide
install -Dpm 0644 skins/Simple/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Simple
install -Dpm 0644 skins/Note/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Note
install -Dpm 0644 skins/Default/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Default
install -Dpm 0644 skins/Mercury_Wide/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Mercury_Wide
install -Dpm 0644 skins/Black_Glass_Wide/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Black_Glass_Wide
install -Dpm 0644 skins/Mercury/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/Mercury
install -Dpm 0644 skins/QuickSilver2/* $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/QuickSilver2
install -dm 0755 $RPM_BUILD_ROOT%{_includedir}/%{name}
install -Dpm 0644 "Plugin API"/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}
desktop-file-install    \
        --dir $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart       \
        --add-only-show-in=GNOME                                \
        linux/%{name}.desktop
desktop-file-install   \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        --remove-category Application \
        linux/%{name}.desktop

# autostart is disabled by default
echo "X-GNOME-Autostart-enabled=false" >> \
    $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/%{name}.desktop

%files
%doc LICENSE.txt readme.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/pixmaps/launchy_icon.png
%{_datadir}/applications/%{name}.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop

%files devel
%{_includedir}/%{name}/*.h

%changelog
%autochangelog
