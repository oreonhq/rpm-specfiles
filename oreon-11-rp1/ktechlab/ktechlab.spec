%global source0_hash 046b9ce1f2c2a93e1da734a416674a5bb5da3203ac773d49ed693b8492f6d212

Name:           ktechlab
Version:        0.51.0
Release:        %autorelease
Summary:        Development and simulation of micro-controllers and electronic circuits
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://invent.kde.org/sdk/ktechlab
Source:         https://download.kde.org/unstable/ktechlab/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gpsim-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-khtml-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-ktexteditor-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qtserialport

# Ktechlab requires gputils for PIC simulation.
Requires:       electronics-menu
Requires:       gputils
Requires:       sdcc

%description
KTechlab is a development and simulation environment for micro-controllers
and electronic circuits. KTechlab consists of several well-integrated
components: A circuit simulator, capable of simulating logic, linear devices
and some nonlinear devices. Integration with gpsim, allowing PICs to be
simulated in circuit. A schematic editor, which provides a rich real-time
feedback of the simulation. A flowchart editor, allowing PIC programs to be
constructed visually. MicroBASIC; a BASIC-like compiler for PICs, written as
a companion program to KTechlab. An embedded Kate part, which provides a
powerful editor for PIC programs. Integrated assembler and disassembler via
gpasm and gpdasm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# TODO: Please submit an issue to upstream (rhbz#2380694)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -Wno-dev
%cmake_build

%install
%cmake_install

#fedora-specific : setting default path for sdcc
%{__mkdir} -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh << EOF
# setting default path for sdcc - fedora
export PATH=\$PATH:%{_libexecdir}/sdcc
EOF

# Fix absolute symlink
%{__rm} -f %{buildroot}%{_docdir}/HTML/en/%{name}/common

%find_lang %{name}

%post
source %{_sysconfdir}/profile.d/%{name}.sh

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%doc %{_datadir}/doc/HTML/*/%{name}
%license COPYING
%{_bindir}/%{name}
%{_bindir}/microbe
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/applications/org.kde.ktechlab.desktop
%{_datadir}/katepart5/syntax/microbe.xml
%{_datadir}/%{name}/*
%{_datadir}/kxmlgui5/%{name}/*
%{_datadir}/metainfo/org.kde.ktechlab.appdata.xml
%{_datadir}/mime/packages/ktechlab_mime.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_sysconfdir}/profile.d/%{name}.sh

%changelog
%autochangelog
