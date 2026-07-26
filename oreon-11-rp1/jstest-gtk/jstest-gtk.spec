%global source0_hash ddb4b3c36cb298bb932bd029408f81d263503018776ede1e9e565aa7fef94d08

%global commit 92bdf8e945a6d14fdd0aa6fa961f6da34f5ac810
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20250403

Name:           jstest-gtk
Version:        0.1.0
Release:        %{date}git%{shortcommit}.%autorelease
Summary:        Simple joystick tester based on Gtk+

License:        GPL-3.0-only
URL:            https://github.com/Grumbel/jstest-gtk
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(sigc++-1.2)

Requires:       hicolor-icon-theme

%description
jstest-gtk is a simple joystick tester based on Gtk+. It provides you with a
list of attached joysticks, a way to display which buttons and axis are
pressed, a way to remap axis and buttons and a way to calibrate your joystick.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md 
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_libexecdir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
