%global source0_hash 2a658df42fa9f8be95bf6dafae2a53ab47962af8afb7043f78a018b7ca6b7310
%undefine _package_note_file
Name:        qelectrotech
Summary:        An electric diagrams editor
Summary(ar): مُحرّر مخططات كهربائية
Summary(be): Elektrische schema editor
Summary(ca): Editar esquemes elèctrics
Summary(cs): Editor výkresů elektrických obvodů
Summary(da): Elektrisk diagram redigering
Summary(de): Schaltpläne erstellen und bearbeiten
Summary(el): Επεξεργασία ηλεκτρικών διαγραμμάτων
Summary(es): Un editor de esquemas eléctricos
Summary(fr): Éditeur de schémas électriques
Summary(hr): Uredi elektro sheme
Summary(it): Un programma per disegnare schemi elettrici
Summary(nl): Elektrische schema editor
Summary(pl): Edytor schematów elektrycznych
Summary(pt): Um editor de esquemas eléctricos
Summary(ru): Редактор электрических схем
Epoch:       0
Version:     0.100
Release:        1%{?dist}
License:    GPL-2.0-or-later
Url:        http://qelectrotech.org/
Source0:        https://github.com/qelectrotech/qelectrotech-source-mirror/releases/download/%{version}/%{name}-%{version}.tar.gz
Requires:         qelectrotech-symbols = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(sqlite3)
# /oreon:deps
%description
QElectroTech is a Qt application to design electric diagrams. It uses XML
files for elements and diagrams, and includes both a diagram editor and an 
element editor.

%description -l be
QElectroTech is een QT toepassing voor het maken en beheren van elektrische
schema's. QET gebruikt XML voor de elementen en schema's en omvat een
schematische editor, itemeditor, en een titel sjabloon editor.

%description -l cs
QElectroTech je aplikací Qt určenou pro návrh nákresů elektrických obvodů.
Pro prvky a nákresy používá soubory XML, a zahrnuje v sobě jak editor nákresů,
tak editor prvků.

%description -l da
QElectroTech er et Qt5 program til at redigere elektriske diagrammer.
Det bruger XML filer for symboler og diagrammer og inkluderer diagram,
symbol og titelblok redigering.

%description -l el
Το QElectroTech είναι μια εφαρμογή Qt για σχεδίαση ηλεκτρικών διαγραμμάτων.
Χρησιμοποιεί αρχεία XML για στοιχεία και διαγράμματα, και περιλαμβάνει
επεξεργαστή διαγραμμάτων καθώς και επεξεργαστή στοιχείων.

%description -l es
QElectroTech es una aplicación Qt para diseñar esquemas eléctricos.
Utiliza archivos XML para los elementos y esquemas, e incluye un editor 
de esquemas y un editor de elemento.

%description -l fr
QElectroTech est une application Qt pour réaliser des schémas électriques.
QET utilise le format XML pour ses éléments et ses schémas et inclut un
éditeur de schémas ainsi qu'un éditeur d'élément.

%description -l it
QElectroTech è una applicazione fatta in Qt per disegnare schemi elettrici.
QET usa il formato XML per i suoi elementi e schemi, includendo anche un
editor per gli stessi.

%description -l nl
QElectroTech is een Qt applicatie om elektrische schema's te ontwerpen.
Het maakt gebruik van XML-bestanden voor elementen en diagrammen, en omvat
zowel een diagram bewerker, een element bewerker, en een bloksjabloon bewerker.

%description -l pl
QElectroTech to aplikacja napisana w Qt, przeznaczona do tworzenia schematów
elektrycznych. Wykorzystuje XML do zapisywania plików elementów i projektów.
Posiada edytor schematów i elementów.

%description -l pt
QElectroTech é uma aplicação baseada em Qt para desenhar esquemas eléctricos.
QET utiliza ficheiros XML para os elementos e para os esquemas e inclui um
editor de esquemas e um editor de elementos.

%description -l ru
QElectroTech - приложение написанное на Qt и предназначенное для разработки
электрических схем. Оно использует XML-файлы для элементов и схем, и включает,
как редактор схем, так и редактор элементов.

%package symbols
Summary:     Elements collection for QElectroTech
Summary(be): Elementen collectie voor QElectroTech
Summary(cs): Sbírka prvků pro QElectroTech
Summary(da): Symbol samling for QElectroTech
Summary(de): Bauteilsammlung für QElectroTech
Summary(el): Συλλογή στοιχείων του QElectroTech
Summary(es): Collección de elementos para QElectroTech
Summary(fr): Collection d'éléments pour QElectroTech
Summary(it): Collezione di elementi per QElectroTech
Summary(nl): Elementen collectie voor QElectroTech
Summary(pl): Kolekcja elementów QElectroTech
Summary(pt): Colecção de elementos para QElectroTech
Summary(ru): Коллекция элементов для QElectroTech
License:     CC-BY-3.0
BuildArch:   noarch
Requires:    qelectrotech = %{epoch}:%{version}-%{release}
%description symbols
Elements collection for QElectroTech.

%description -l be symbols
Elementen collectie voor QElectroTech.

%description -l cs symbols
Sbírka prvků pro QElectroTech.

%description -l da symbols
Symbol samling for QElectroTech.

%description -l de symbols
Bauteilsammlung für QElectroTech.

%description -l el symbols
Συλλογή στοιχείων του QElectroTech.

%description -l es symbols
Collección de elementos para QElectroTech.

%description -l fr symbols
Collection d'éléments pour QElectroTech.

%description -l it symbols
Collezione di elementi per QElectroTech.

%description -l nl symbols
Elementen collectie voor QElectroTech.

%description -l pl symbols
Kolekcja elementów QElectroTech.

%description -l pt symbols
Colecção de elementos para QElectroTech.

%description -l ru symbols
Коллекция элементов для QElectroTech.

%prep

%setup -q

sed -e s,/usr/local/,%{_prefix}/, \
    -e /QET_MAN_PATH/s,'man/','share/man', \
    -e /QET_MIME/s,../,, \
    -i %{name}.pro

%{qmake_qt5} \
  'QMAKE_COPY_DIR = cp -f -r --preserve=timestamps' \
  qelectrotech.pro

%build

make %{?_smp_mflags}
%install
rm -f *.lang
INSTALL_ROOT=%{buildroot} make install
rm -rf %{buildroot}/usr/doc/%{name} \
       %{buildroot}%{_datadir}/%{name}/examples \
       %{buildroot}%{_mandir}/fr.ISO8859-1 \
       %{buildroot}%{_mandir}/fr
mv %{buildroot}%{_mandir}/fr.UTF-8 %{buildroot}%{_mandir}/fr
desktop-file-install --vendor="" \
   --add-category=Electronics \
   --dir=%{buildroot}%{_datadir}/applications/ \
         %{buildroot}%{_datadir}/applications/*.desktop
rm -f %{buildroot}%{_datadir}/%{name}/lang/qt_*.qm
%find_lang qet          --with-qt
%find_lang qelectrotech --with-man
cat qet.lang >>qelectrotech.lang
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qelectrotech-symbols -f %{oreon_filedir}/qelectrotech-symbols.list

%changelog

%autochangelog
