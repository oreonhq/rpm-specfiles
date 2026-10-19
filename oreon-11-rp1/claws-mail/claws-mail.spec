%global source0_hash 03e0549d5f0fcd7a59804186524105d05ebb5e534d42a4b86a9a90f729ca255b
%global pluginapi 4.3.1.0
%global with_dillo 0
Obsoletes: claws-mail-plugins-dillo < 4.0.0-1
%global with_python2 0
%global with_python3 1
Name:           claws-mail
Version:        4.4.0
Release:        1%{?dist}
Summary:        Email client and news reader based on GTK+
License:        GPL-3.0-or-later
URL:            http://claws-mail.org
Source0:        https://claws-mail.org/releases/%{name}-%{version}.tar.xz
Patch11:        claws-mail-system-crypto-policies.patch
%if 0%{?build_manual}
%endif
%if 0%{?with_python2}
%endif
%if 0%{?with_python3}
%endif
Requires: libetpan%{?_isa} >= 1.9.2
Provides:       claws-mail(plugin-api)%{?_isa} = %pluginapi
# oreon:deps
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  compface-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  docbook-utils-pdf
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  ghostscript
BuildRequires:  gumbo-parser-devel
BuildRequires:  libSM-devel
BuildRequires:  libetpan-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libytnef-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pilot-link-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  python3
BuildRequires:  python3-devel
# /oreon:deps
%description
Claws Mail is an email client (and news reader), based on GTK+, featuring
quick response, graceful and sophisticated interface, easy configuration,
intuitive operation, abundant features, and extensibility.

%package        devel
Summary:        Development package for %{name}
%description    devel
The %{name}-devel package contains the header files
and pkgconfig file needed for development with %{name}.

%package plugins
Summary: Additional plugins for Claws Mail
Requires: %{name}-plugins-acpi-notifier
Requires: %{name}-plugins-address-keeper
Requires: %{name}-plugins-archive
Requires: %{name}-plugins-att-remover
Requires: %{name}-plugins-attachwarner
Requires: %{name}-plugins-bogofilter
Requires: %{name}-plugins-clamd
%if 0%{?with_dillo}
Requires: %{name}-plugins-dillo
%endif
Requires: %{name}-plugins-fancy
Requires: %{name}-plugins-fetchinfo
Requires: %{name}-plugins-libravatar
Requires: %{name}-plugins-litehtml-viewer
Requires: %{name}-plugins-mailmbox
Requires: %{name}-plugins-managesieve
Requires: %{name}-plugins-newmail
Requires: %{name}-plugins-notification
Requires: %{name}-plugins-pdf-viewer
Requires: %{name}-plugins-perl
Requires: %{name}-plugins-pgp
%if 0%{?with_python2}%{?with_python3}
Requires: %{name}-plugins-python
%endif
Requires: %{name}-plugins-rssyl
Requires: %{name}-plugins-smime
Requires: %{name}-plugins-spamassassin
Requires: %{name}-plugins-spam-report
Requires: %{name}-plugins-tnef
Requires: %{name}-plugins-vcalendar
%description plugins
Meta-package to add all additional plugin packages for Claws Mail.

%package plugins-acpi-notifier
Summary:        ACPI notification plugin for Claws Mail 
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-acpi-notifier
Enables mail notification via LEDs on some laptops. Options can be found on
the 'Plugins/Acpi Notifier' page of the preferences.

%package plugins-address-keeper
Summary:        Never forget a typed address in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-address-keeper
This plugin allows saving outgoing addresses to a designated folder
in the address book. Addresses are saved only if not found in the
address book to avoid unwanted duplicates.

%package plugins-archive
Summary:        Archiving features for Claws Mail 
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-archive
%{summary}

%package plugins-attachwarner
Summary:        Attachment warner plugin for Claws Mail 
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-attachwarner
Warns when the user composes a message mentioning an attachment in the message
body but without attaching any files to the message. 

%package plugins-att-remover
Summary:        Attachments remover plugin for Claws Mail 
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-att-remover
Enables the removal of attachments from emails. When right-clicking a message,
choose 'Remove attachments' from the sub-menu.

%package plugins-bogofilter
Summary:        Bogofilter plugin for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
Requires:       bogofilter
%description plugins-bogofilter
%{summary}

%package plugins-clamd
Summary:        Use Clam AntiVirus to scan messages in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-clamd
This plugin uses Clam AntiVirus to scan all messages that are
received from an IMAP, LOCAL or POP account.
When a message attachment is found to contain a virus it can be
deleted or saved in a specially designated folder.
Options can be found in /Configuration/Preferences/Plugins/Clam AntiVirus.

%if 0%{?with_dillo}
%package plugins-dillo
Summary:        Display HTML emails in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
Requires:       dillo
%description plugins-dillo
This plugin renders HTML email via the Dillo web browser.
%endif

%package plugins-fancy
Summary:        Display HTML emails in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-fancy
This plugin renders HTML email via the GTK+ port of the WebKit library.

%package plugins-fetchinfo
Summary:        Modify headers of downloaded messages in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-fetchinfo
This plugin inserts headers containing some download information:
UIDL, Sylpheeds account name, POP server, user ID and retrieval time.

%package plugins-keyword_warner
Summary:        Keyword warner plugin for Claws Mail
Requires:	claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-keyword_warner
This plugin shows a warning when sending or queueing a message and a
reference to one or more keywords is found in the message text.

%package plugins-libravatar
Summary:        Libravatar plugin for Claws Mail
Requires:	claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-libravatar
This plugin allows showing the profile picture associated to email
addresses provided by https://www.libravatar.org/. You can read
more about what is this at http://wiki.libravatar.org/description/.

%package plugins-litehtml-viewer
Summary:        LiteHTML plugin for Claws Mail
Requires:	claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-litehtml-viewer
This is an HTML viewer plugin that uses the litehtml to render the
HTML message parts in the Claws Mail message view window. Users of
old Fancy plugin may find this viewer more similar than other HTML
viewer plugins, though you may miss some feature.

%package plugins-mailmbox
Summary:        Add support for mailboxes in mbox format to Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-mailmbox
This plugin provides direct support for mailboxes in mbox format.

%package plugins-managesieve
Summary:        Add Manage sieve support to Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-managesieve
Manage sieve filters on a server using the ManageSieve protocol.

%package plugins-newmail
Summary:        Make Claws Mail write a message header summary to a file
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-newmail
Write a message header summary to a log file (defaults to ~/Mail/NewLog) on
arrival of new mail *after* sorting.

%package plugins-notification
Summary:        Various ways to notify about new messages in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-notification
This plugin collects various ways to notify the user of new (and possibly
unread) mail. Currently, a pop-up and a mail banner are implemented.

%package plugins-pdf-viewer
Summary:        Enables the viewing of PDF and PostScript attachments
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-pdf-viewer
This plugin handles PDF and Postscript attachments.

%package plugins-perl
Summary:        Perl based extended filtering engine for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-perl
This plugin provides an extended filtering engine for the email client
Claws Mail. It allows for the use of full perl power in email filters.

%package plugins-pgp
Summary:        PGP plugin for signing and encrypting with Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
Requires:       pinentry-gui
%description plugins-pgp
%{summary}

%if 0%{?with_python2}%{?with_python3}
%package plugins-python
Summary:        Python scripting access to Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-python
This plugin offers a Python scripting access to Claws Mail. Python code can be
entered interactively into an embedded Python console or stored in scripts
under ~/.claws-mail/python-scripts. The scripts are then accessible via the
menu of the main window.
%endif

%package plugins-rssyl
Summary:        RSS plugin for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-rssyl
Allows you to read your favorite RSS news feeds in Claws Mail. RSS 1.0,
2.0 and Atom feeds are currently supported.

%package plugins-smime
Summary:        S/MIME support for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
Requires:       claws-mail-plugins-pgp%{?_isa} = %{version}-%{release}
%description plugins-smime
This plugin handles S/MIME signed and/or encrypted mails. You can decrypt
mails, verify signatures or sign and encrypt your own mails.

%package plugins-spamassassin
Summary:        Spamassassin plugin for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
Requires:       spamassassin
%description plugins-spamassassin
%{summary}

%package plugins-spam-report
Summary:        Report spam mail to various places with Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-spam-report
This plugin for Claws Mail can report spam mail to various places.

%package plugins-tnef
Summary:        TNEF message parsing for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-tnef
This plugin allows reading of application/ms-tnef attachments.

%package plugins-vcalendar
Summary:        Handling of vCalendar messages in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
%description plugins-vcalendar
This plugin enables vCalendar message handling like that produced by
Evolution or Outlook. It also supports subscribing to remote webCal feeds, and
exporting of your meetings or all your calendars.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# guard for pluginapi
SOURCEAPI=$(grep -A 1 VERSION_NUMERIC src/common/version.h | tr -d '\n' | perl -ne 's/[\\\s]//g; m/(\d+),(\d+),(\d+),(\d+)/; print("$1.$2.$3.$4");')
[ "%pluginapi" == "$SOURCEAPI" ] || exit -1

#cat << EOF > README.Fedora
#Firefox and Claws Mail
#
#    Be sure to set the TMPDIR environment variable, so both applications
#    always use the same directory for temporary files. Else the directory
#    would vary depending on whether or not Claws Mail is launched as mailer
#    from within Firefox. [ https://bugzilla.redhat.com/956380 ]
#EOF

%build

autopoint -f
autoreconf -f
%configure --disable-dependency-tracking \
           --disable-rpath \
%if 0%{?with_dillo}
           --enable-dillo-plugin \
%else
           --disable-dillo-plugin \
%endif
           --enable-fancy-plugin \
           --enable-litehtml_viewer-plugin \
%if 0%{?with_python2}%{?with_python3}
           --enable-python-plugin \
%else
           --disable-python-plugin \
%endif
           --enable-libetpan
sed -i -e 's!\"/usr/bin/mh/inc\"!\"/usr/bin/inc\"!g' src/common/defs.h
grep DEFAULT_INC_PATH src/common/defs.h || exit -1
grep 'PERL_LDFLAGS *=' configure || exit -1
sed -i 's!\(PERL_LDFLAGS *=\).*$!\1-lperl!g' configure
%if 0%{?with_python2}
grep 'PYTHON_SHARED_LIB=.*\.so\"$' configure || exit -1
sed -i 's!\(PYTHON_SHARED_LIB=.*\.so\)\"$!\1.1.0\"!' configure
grep 'PYTHON_SHARED_LIB=.*\.so\"$' configure && exit -1
grep 'dlopen.*PYTHON_SHARED_LIB' src/plugins/python/* -R || exit -1
%endif
make %{?_smp_mflags} LIBTOOL=%{_bindir}/libtool
%install
export LIBTOOL=%{_bindir}/false
make DESTDIR=%{buildroot} install
%find_lang claws-mail
desktop-file-install \
--add-category="Office" \
--remove-category="GTK" \
--remove-key="Encoding" \
--remove-key="Info" \
--dir=%{buildroot}%{_datadir}/applications \
%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
find %{buildroot}%{_libdir}/claws-mail/plugins/ -type f -name \
"*.a" -exec rm -f {} ';'
%if 0%{?build_manual}
rm -rf _tmp_manual && mkdir _tmp_manual
mv %{buildroot}%{_datadir}/doc/claws-mail/manual _tmp_manual
rm -f %{buildroot}%{_datadir}/doc/claws-mail/RELEASE_NOTES
%endif
for file in AUTHORS;
do iconv -f iso8859-1 -t utf-8 ${file} > \
 ${file}.conv && mv -f ${file}.conv ${file}
done;
rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache
touch -r NEWS %{buildroot}%{_includedir}/%{name}/config.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
