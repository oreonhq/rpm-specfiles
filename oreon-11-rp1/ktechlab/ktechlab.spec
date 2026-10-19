%global source0_hash 046b9ce1f2c2a93e1da734a416674a5bb5da3203ac773d49ed693b8492f6d212
Name:           ktechlab
Version:        0.51.0
Release:        1%{?dist}
Summary:        Development and simulation of micro-controllers and electronic circuits
License:        GPL-2.0-only
URL:            https://invent.kde.org/sdk/ktechlab
Source0:        https://download.kde.org/unstable/ktechlab/%{name}-%{version}.tar.xz
Requires:       electronics-menu
Requires:       gputils
Requires:       sdcc
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gpsim-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-khtml-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-ktexteditor-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  qt5-qtserialport
BuildRequires:  qt5-qtserialport-devel
# /oreon:deps
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
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -Wno-dev
%cmake_build
%install
%cmake_install
%{__mkdir} -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh << EOF
export PATH=\$PATH:%{_libexecdir}/sdcc
EOF
%{__rm} -f %{buildroot}%{_docdir}/HTML/en/%{name}/common
%find_lang %{name}
%oreon_autofiles main

%post

source %{_sysconfdir}/profile.d/%{name}.sh
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
