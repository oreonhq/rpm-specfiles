%global source0_hash 4a756133c0eba27b1a8e236dae53ae17325605ba486fe6cb2eb2be9966683fa5
%bcond_without gnome
%bcond_with mate
Name:           verbiste
Version:        0.1.49
Release:        6%{?dist}
Summary:        French conjugation system
License:        GPL-2.0-or-later
URL:            http://sarrazip.com/dev/verbiste.html
Source0:        http://perso.b2b2c.ca/~sarrazip/dev/%{name}-%{version}.tar.gz
%if %{with gnome}
%endif
%if %{with mate}
%endif
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libgnomeui-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
# /oreon:deps
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
rm -f %{buildroot}%{_datadir}/locale/locale.alias
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n verbiste-devel -f %{oreon_filedir}/verbiste-devel.list
%files -n verbiste-gnome -f %{oreon_filedir}/verbiste-gnome.list

%changelog

%autochangelog
