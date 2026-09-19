%global source0_hash 0c1ddc72ebfc255bbb246446fb7be5b0fd1bb1594c70045c3e537cb6d274965b

Name:          glogg
Version:       1.1.4
Release:       37%{?dist}
Summary:       Smart interactive log explorer
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://glogg.bonnefon.org
Source:        http://glogg.bonnefon.org/files/%{name}-%{version}.tar.gz
# We're using python-markdown2
# thus we need to rename markdown -> markdown2
Patch0:        %{name}-python-markdown.patch
# Look for Qt5DBus rather than QtDBus
Patch1:        %{name}-qt5dbus.patch

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-markdown2
BuildRequires:  qt5-qtbase-devel
BuildRequires: make

%description
%{name} is a multi-platform GUI application to browse and search through
long or complex log files. It is designed with programmers and system
administrators in mind. %{name} can be seen as a graphical, interactive
combination of grep and less.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{qmake_qt5}
make %{?_smp_flags}

%install
make INSTALL_ROOT=%{buildroot}%{_prefix} install
rm -rf %{buildroot}%{_datadir}/doc
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING README.md TODO doc/documentation.html
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
