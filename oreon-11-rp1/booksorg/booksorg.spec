%global source0_hash 796dc5f135d024d58b37e519bd2e9c6ec9f29a2ba0ff245c6461fa709ff9c88e
%global owner zakariakov
%global commit 93b03026cadd9946f02ba0cecb615714b822cdb5
Name: booksorg
Version: 0.3.1
Release:        16%{?dist}
License: GPL-3.0-only
Summary:        Books Organizer
URL: https://github.com/%{owner}/%{name}
Source0:        https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Requires: qt5-qtbase
# oreon:deps
BuildRequires:  dejavu-serif-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  poppler-qt5-devel
BuildRequires:  qt5-qtsvg-devel
# /oreon:deps
%description
 Books Organizer an organizer for PDF files based on SQLite
 and with a built-in reader.  Bring your favorite PDF pages
 all in one! Make your own extract pages from existing ones.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%if 0%{?flatpak}
sed -i -e 's|/usr|%{_prefix}|g' booksorganizer.pro
%endif

%build

%qmake_qt5
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/appdata
install -Dp -m 0644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
chmod 644 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
