%global source0_hash 1e8b11bd1baa0f6756326b58f87eb95a56b38a25d7336fdfb65c2dfca46d03a6

# 'rel' is always the release number.
# If you're building from SVN, set 'svn' to the SVN revision. If not, set it to 0
%global rel 3
%global svn 0 
%if %{svn}
# svn co https://osmo-pim.svn.sourceforge.net/svnroot/osmo-pim/trunk osmo-pim
# tar cvJf osmo-%{svn}.tar.xz osmo-pim/ --exclude=".svn*"
%global release 0.%{rel}.svn%{svn}%{?dist}.12
%global tarname %{name}-%{svn}.tar.xz
%global _dirname osmo-pim
%else
%global release %{rel}%{?dist}
%global tarname %{name}-%{version}.tar.gz
%global _dirname %{name}-%{version}
%endif

Summary:        Personal organizer
Summary(pl):    Osobisty organizer
Summary(de):    Persönlicher Organizer
Name:           osmo
Version:        0.4.4
Release:        %{release}
License:        GPLv2+
Group:          Applications/Productivity
URL:            http://osmo-pim.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}-pim/%{tarname}

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtkspell3-devel
BuildRequires:  libical-devel
BuildRequires:  libnotify-devel
BuildRequires:  libxml2-devel
# for contacts 
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  libgringotts-devel
BuildRequires:  libgcc
BuildRequires:	gcc
BuildRequires:  libtar-devel
# for the SyncML plugin - disabled due to broken libsyncml (adamw 2012/09)
# BuildRequires:  libsyncml-devel
BuildRequires:  autoconf
BuildRequires:  automake

Requires:       hicolor-icon-theme
Requires:       tzdata
Requires:       xdg-utils
Requires:       alsa-utils
Requires:       gtk3
Requires:       gtkspell3
Requires:       webkit2gtk4.1
Requires:       libgringotts
Requires:       libtar
Requires:       libxml2
Requires:       gettext

#
%description
Osmo is a handy personal organizer which includes calendar, tasks manager and
address book modules. It was designed to be a small, easy to use and good
looking PIM tool to help to manage personal information. In current state the
organizer is quite convenient in use - for example, user can perform nearly
all operations using keyboard. Also, a lot of parameters are configurable to
meet user preferences.

%description -l pl
Osmo to podręczny organizer, zawierający kalendarz, menedżer zadań i książkę
adresową. W zamierzeniu był małym, prostym w obsłudze i dobrze wyglądającym 
menedżerem informacji osobistych. Osmo jest bardzo wygodny - niemal wszystkie
operacje można wykonać za pomocą klawiatury. Program udostępnia wiele opcji,
które użytkownik może zmienić, by program bardziej mu odpowiadał.

%description -l de
Osmo ist ein handlicher persönlicher Organzier mit Kalender, Aufgabenliste und
Adressbuch. Er wurde als kleines, einfach zu benutzendes und gut aussehendes 
PIM-Werkzeug zur Verwaltung persönlicher Informationen entworfen. Im 
gegenwärtigen Zustand ist er sehr angenehm zu benutzen, so kann der Nutzer zum 
Beispiel fast alle Aktionen mit der Tastatur ausführen. Außerdem lassen sich 
viele Parameter einstellen, um die Vorlieben des Benutzers zu treffen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_dirname}
#%patch0 -p1 -b .configure
#%patch10 -p1 -b .aplay
# Use webkit2gtk-4.1
# https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
sed -i configure.ac -e 's|webkit2gtk-4.0|webkit2gtk-4.1|'
autoreconf -vif

%build
%configure --enable-backup=yes --enable-printing=yes \
  --with-contacts --with-tasks --with-notes
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

make install DESTDIR=%{buildroot} INSTALL="install -p"

# icon
mv %{buildroot}%{_datadir}/pixmaps/%{name}.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

# Remove empty directory.
rm -rf %{buildroot}%{_datadir}/pixmaps/

%find_lang %{name}

desktop-file-install \
    %if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor fedora \
    %endif
    --delete-original \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TRANSLATORS
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/actions/%{name}-*.png
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/sounds/osmo
%{_datadir}/sounds/osmo/alarm.wav

%changelog
%autochangelog
