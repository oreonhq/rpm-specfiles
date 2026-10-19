%global source0_hash de466e4f245ac3fe9d1bdeba84f475fd9af2225d774e355723bdf7123c6759d8
Name:           bvi
Version:        1.5.0.src.src
Release:        1%{?dist}
Summary:        Display-oriented editor for binary files
Summary(fr):    Afficheur orienté editeur pour fichiers binaires
License:        GPL-3.0-or-later
URL:            http://bvi.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
The bvi is a display-oriented editor for binary files, based
on the vi text-editor. If you are familiar with vi, just start
the editor and begin to edit! A bmore program is also
included in the package.

%description -l fr
Le bvi est un afficheur orienté éditeur pour fichiers binaires, basé sur
l'éditeur de texte vi. Si vi vous est familié, démarrez juste l'éditeur
et commencez à éditer! Un logiciel bmore est également inclu dans le
paquet.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Fix the path of the bmore.help file specified in the man page :
sed -i "s@/usr/local/share/bmore.help@/usr/share/bvi/bmore.help@" ./bmore.1

%build

export CFLAGS="%{optflags} -std=gnu17"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
