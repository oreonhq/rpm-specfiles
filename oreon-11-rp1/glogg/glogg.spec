%global source0_hash 0c1ddc72ebfc255bbb246446fb7be5b0fd1bb1594c70045c3e537cb6d274965b
Name:          glogg
Version:       1.1.4
Release:        37%{?dist}
Summary:        Smart interactive log explorer
License:       GPL-3.0-or-later
URL:           http://glogg.bonnefon.org
Source0:        http://glogg.bonnefon.org/files/%{name}-%{version}.tar.gz
Patch0:        %{name}-python-markdown.patch
Patch1:        %{name}-qt5dbus.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  python3-markdown2
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
%{name} is a multi-platform GUI application to browse and search through
long or complex log files. It is designed with programmers and system
administrators in mind. %{name} can be seen as a graphical, interactive
combination of grep and less.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{qmake_qt5}
make %{?_smp_flags}
%install
make INSTALL_ROOT=%{buildroot}%{_prefix} install
rm -rf %{buildroot}%{_datadir}/doc
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
