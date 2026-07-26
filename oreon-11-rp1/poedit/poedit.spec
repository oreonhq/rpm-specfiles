%global source0_hash 1e86e56146a748fa94ce80e05a402b3e19fb70c89118b96628aceb1be9b6f7fb

Name:           poedit
Version:        3.9
Release:        1%{?dist}
Summary:        GUI editor for GNU gettext .po files
Summary(de):    Grafischer Editor für GNU Gettext-Dateien

License:        MIT
URL:            https://poedit.net/
Source0:        https://github.com/vslavik/%{name}/releases/download/v%{version}-oss/%{name}-%{version}.tar.gz
Source1:        https://src.fedoraproject.org/rpms/%{name}/raw/rawhide/f/%{name}.1.de.po

BuildRequires:  make
BuildRequires:  wxGTK-devel >= 3.2
BuildRequires:  gtkspell3-devel
BuildRequires:  libappstream-glib
BuildRequires:  lucene++-devel
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  po4a
BuildRequires:  libsecret-devel
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  cpprest-devel
# cld2 is not available for ppc64 s390x
%ifnarch ppc64 s390x
BuildRequires:  cld2-devel
%endif
# Use json.hpp from Fedora and not the version bundled with Poedit
BuildRequires:  json-devel
BuildRequires:  pkgconfig(pugixml) >= 1.9

Requires:       gettext

%description
This program is a GUI frontend to GNU Gettext utilities and a catalogs 
editor/source code parser. It helps with translating applications into 
other languages.

%description -l de
Dieses Programm stellt eine grafische Benutzeroberfläche für die
Dienstprogramme aus GNU Gettext bereit, sowie einen Katalogeditor und einen
Quellcode-Parser. Es hilft beim Übersetzen von Anwendungen in andere Sprachen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Remove bundled sources
rm -rf deps/

%build
%ifarch ppc64 s390x
# cld2 is not available for ppc64 s390x
%configure --with-wx-config=/usr/bin/wx-config-3.2 --with-cpprest
%else
%configure --with-wx-config=/usr/bin/wx-config-3.2 --with-cpprest --with-cld2
%endif
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

# Install the desktop file
desktop-file-install \
    --delete-original \
    --add-category=GTK \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/net.%{name}.Poedit.desktop

# Generate and install localized man pages
mkdir -p man/de
po4a-translate -M utf-8 -f man \
               --option groff_code=verbatim \
               -m docs/%{name}.1 -p %{SOURCE1} \
               -l man/de/%{name}.1

mkdir -p %{buildroot}%{_mandir}/de/man1
install -p -m 644 man/de/%{name}.1 %{buildroot}%{_mandir}/de/man1

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/net.%{name}.Poedit.appdata.xml ||:

%{find_lang} poedit --with-man

%files -f poedit.lang
%doc NEWS README.md AUTHORS docs/*.txt
%license COPYING
%{_bindir}/*
%{_datadir}/metainfo/net.%{name}.Poedit.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/poedit
%{_mandir}/man?/*

%changelog
%autochangelog
