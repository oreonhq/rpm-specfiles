%global source0_hash 4a756133c0eba27b1a8e236dae53ae17325605ba486fe6cb2eb2be9966683fa5

%if 0%{?rhel} >= 7 || 0%{?fedora} >= 44
%bcond_with gnome
%else
%bcond_without gnome
%endif
%bcond_with mate

Name:           verbiste
Version:        0.1.49
Release:        6%{?dist}
Summary:        French conjugation system
License:        GPL-2.0-or-later
URL:            http://sarrazip.com/dev/verbiste.html
Source:         http://perso.b2b2c.ca/~sarrazip/dev/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if %{with gnome}
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libgnomeui-devel
%endif
BuildRequires:  libxml2-devel
BuildRequires:  libtool
BuildRequires:  automake
%if %{with mate}
BuildRequires:  mate-panel-devel
%endif
BuildRequires:  perl(XML::Parser)

%description
This package contains a database of French conjugation templates
and a list of more than 7000 regular and irregular French verbs
with their corresponding template. It also comes with two command-line 
tools named french-conjugator and french-deconjugator.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libxml2-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%if %{with gnome}
%package        gnome
Summary:        GNOME Panel applet for Verbiste
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description    gnome
GNOME Panel applet and application based on Verbiste.
%endif

%if %{with mate}
%package        mate
Summary:        MATE Desktop Panel applet for Verbiste
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    mate
MATE Desktop Panel applet and application based on Verbiste.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# convert doc files to unicode
for DOCFILE in README NEWS HACKING LISEZMOI; do
    iconv -f ISO8859-15 -t UTF8 < $DOCFILE > $DOCFILE.tmp
    mv -f $DOCFILE.tmp $DOCFILE
done

%build
autoreconf -ivf
%configure \
%if %{with mate}
           --with-mate-applet \
%endif
%if %{with gnome}
           --with-gnome-app \
%endif
           --without-gtk-app \
           --disable-maintainer-mode \
           --without-examples \
           --disable-rpath
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete -print

%if %{with gnome}
# This file gets created on x86_64 for no apparent reason.
# It's owned by glibc-common.
#rm -f %%{buildroot}%%{_datadir}/locale/locale.alias
desktop-file-install \
  --delete-original                          \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

rm -frv %{buildroot}%{_docdir}

%find_lang %{name} --with-man
%find_lang french-conjugator --with-man
%find_lang french-deconjugator --with-man
%else
rm -rf %{buildroot}%{_mandir}/man3
rm -rf %{buildroot}%{_mandir}/*/man3
%endif

rm -frv %{buildroot}%{_docdir}
# This file gets created on x86_64 for no apparent reason.
# It's owned by glibc-common.
rm -f %{buildroot}%{_datadir}/locale/locale.alias

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING HACKING LISEZMOI NEWS README THANKS
%{_bindir}/french-*
%{_datadir}/verbiste*
%{_libdir}/*.so.*
%{_mandir}/man1/french-*.1*
%{_mandir}/*/man1/french-*.1*

%files devel
%{_includedir}/verbiste-0.1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%if %{with gnome}
%files gnome -f %{name}.lang -f french-conjugator.lang -f french-deconjugator.lang
%{_bindir}/verbiste
%{_bindir}/verbiste-gtk
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/texmf/tex/latex/verbiste
%{_mandir}/man3/verbiste.3*
%{_mandir}/*/man3/verbiste.3*
%endif

%changelog
%autochangelog
