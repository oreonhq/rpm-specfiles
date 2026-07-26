%global source0_hash 6314e030b2e18f9f8084eab239c7d694d2a457f63ddc87d5ed36f133e498843e

Name: 		utrac
Version:	0.3.0
Release:	43%{?dist}
Summary: 	Universal Text Recognizer and Converter
Summary(fr): 	Reconnaisseur et convertisseur universel de texte

License: 	GPL-2.0-or-later
Url: 		http://utrac.sourceforge.net
Source:		http://utrac.sourceforge.net/download/utrac-0.3.0.tar.gz
Patch0:		utrac-destdir.patch
Patch1:		utrac.h.utf8
Patch2:		utrac-prefix.patch

BuildRequires: make
BuildRequires:  gcc
%description
Utrac is a command line tool and a library that recognize the encoding
of an input file (ex: UTF-8, ISO-8859-1, CP437...) and its end-of-line
type (CR, LF, CRLF).
It has three main features:
- Automatic recognition (depending on the file and on the system's locale),
  reliable in most cases;
- Assistance for verification or manual recognition;
- Conversion to an other charset and/or end-of-line type.

%description -l fr
Utrac est un outil en ligne de commande et une bibliothèque qui reconnait
l'encodage d'un fichier d'entrée (par ex: UTF-8, ISO-8859-1, CP437...) et son
type de fin de ligne (CR, LF, CRLF).
Ses trois fonctionnalités principales sont :
- reconnaissance automatique (suivant le fichier et la localisation du
  système) fiable dans la plupart des cas ;
- assistance à la vérification ou à la reconnaissance manuelle ;
- conversion dans un autre jeu de caractères et/ou type de fin de ligne.

%package	devel
Summary:	Library and file header for utrac
Summary(fr):	Bibliothèque et fichier d'en-têtes pour utrac
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}

%description devel
The %{name}-devel package includes the static library and the header files
for compiling programs that use the utrac library.

%description -l fr devel
Le paquetage %{name}-devel contient la bibliothèque statique et le fichier
d'en-têtes nécessaires à la compilation des programmes qui utilisent la
bibliothèque utrac.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0
%patch -P1 -p1
%patch -P2
%{__sed} -i -e 's/^\(CFLAGS.*\)/\1 $(RPM_OPT_FLAGS)/' Makefile
%{__sed} -i -e '/^\s*strip /d' Makefile

%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -std=gnu17"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT \
             PREFIX_PATH=%{_prefix} \
             BIN_PATH=%{_bindir} \
             LIB_PATH=%{_libdir} \
             INC_PATH=%{_includedir} \
             MAN_PATH=%{_mandir}/man1 \
             SHARE_PATH=%{_datadir}/%{name}
make install-lib DESTDIR=$RPM_BUILD_ROOT \
             PREFIX_PATH=%{_prefix} \
             BIN_PATH=%{_bindir} \
             LIB_PATH=%{_libdir} \
             INC_PATH=%{_includedir} \
             MAN_PATH=%{_mandir}/man1 \
             SHARE_PATH=%{_datadir}/%{name}

%files
%doc CHANGES COPYING README TODO
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*

%files devel
%{_libdir}/*.a
%{_includedir}/*

%changelog
%autochangelog
