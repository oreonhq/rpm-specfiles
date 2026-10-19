%global source0_hash 9c7d4f884fc21342814a186020e04aa1a5d436e9a13ea128d132e232d04b07e4
%global branch 1.28
Summary:        Terminal emulator for MATE
Name:          mate-terminal
Version:       %{branch}.3
Release:        1%{?dist}
License:       GPL-3.0-or-later
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Patch1:        mate-terminal_better_defaults-1.26.0.patch
Requires:      mate-desktop-libs
Requires:      gsettings-desktop-schemas
# oreon:deps
BuildRequires:  dconf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  vte291-devel
# /oreon:deps
%description
Mate-terminal is a terminal emulator for MATE. It supports translucent
backgrounds, opening multiple terminals in a single window (tabs) and
clickable URLs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static                \
           --disable-schemas-compile       
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                                                    \
        --delete-original                                               \
        --dir=%{buildroot}%{_datadir}/applications                      \
%{buildroot}%{_datadir}/applications/mate-terminal.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
