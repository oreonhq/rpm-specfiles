%global source0_hash 6540716a1a3b2b9711635108da14b26baea488881d4a682121c0bddbba6b74cb

Name:           bvi
Version:        1.5.0
Release:        3%{?dist}
Summary:        Display-oriented editor for binary files
Summary(fr):    Afficheur orienté editeur pour fichiers binaires

License:        GPL-3.0-or-later
URL:            http://bvi.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz

BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  make

ExcludeArch:    %{ix86}

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

%files
%doc README COPYING CREDITS CHANGES
%{_bindir}/%{name}
%{_bindir}/bmore
%{_bindir}/bvedit
%{_bindir}/bview
%{_datadir}/%{name}/
%{_mandir}/man1/*.1.*

%changelog
%autochangelog
