%global source0_hash d241acdbf8d82f1ae0910bfc5cfc7872e1fdb2331415257fbe20d65965bcdfc3

%global upname bubblemail-gnome-shell

Name:           gnome-shell-extension-bubblemail
Version:        27
Release:        1%{?dist}
Summary:        GNOME Shell indicator for new and unread mail using Bubblemail 

License:        GPL-2.0-or-later
URL:            http://bubblemail.free.fr/
Source0:        https://framagit.org/razer/%{upname}/-/archive/v%{version}/%{upname}-v%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gettext

Requires:       bubblemail >= 1.7
Requires:       gnome-shell >= 45.0

BuildArch:      noarch

%description
%{name} relies on the Bubblemail service to display
notifications in GNOME shell about new and unread messages in local (mbox,
Maildir) and remote (POP3, IMAP) mailboxes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upname}-v%{version}
mv src/LICENSE ./

%build	
%meson -Dgnome_shell_libdir=%{_datadir}/gnome-shell/extensions/ \
       -Dgsettings_schemadir=%{_datadir}/glib-2.0/schemas/
%meson_build

%install
%meson_install
%find_lang %{upname}

%files -f %{upname}.lang
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.bubblemail.gschema.xml
%{_datadir}/gnome-shell/extensions/bubblemail@razer.framagit.org/

%changelog
%autochangelog
