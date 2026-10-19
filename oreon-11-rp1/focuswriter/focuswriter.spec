%global source0_hash e6e2ac78c45f0331d8ebd33517910ae13a839b0288e4315a8429ba026900f211
Name:           focuswriter
Version:        1.9.1
Release:        1%{?dist}
Summary:        A full screen, distraction-free writing program
License:        GPL-3.0-or-later
URL:            http://gottcode.org/%{name}/
Source0:        http://gottcode.org/%{name}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  hunspell-devel
BuildRequires:  libappstream-glib
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
A full screen, distraction-free writing program. You can customize your
environment by changing the font, colors, and background image to add ambiance
as you type. FocusWriter features an on-the-fly updating word count, optional
auto-save, optional daily goals, and an interface that hides away to allow you
to focus more clearly; additionally, when you open the program your current
work-in-progress will automatically load and position you at the end of your
document, so that you can immediately jump back in.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
