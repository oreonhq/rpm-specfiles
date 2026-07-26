%global source0_hash d6e4a332f5e87365b5f5c14807f66f328ba6c7330ea21a0c8bef7c1268347314

Name:           focuswriter
Version:        1.9.0
Release:        %autorelease
Summary:        A full screen, distraction-free writing program
License:        GPL-3.0-or-later
URL:            http://gottcode.org/%{name}/
Source0:        http://gottcode.org/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  zlib-devel
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  hunspell-devel
BuildRequires:  gettext-devel

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

%autosetup -n %{name}-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
