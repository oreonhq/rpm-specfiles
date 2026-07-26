%global source0_hash 2ac77f3233ddaef718f89c9371ab5165af29cf9738ed46b6bea64b37e45d4b60

Summary:       Graphical LDAP directory browser and editor
Name:          gq
Version:       1.3.4
Release:       56%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://sourceforge.net/projects/gqclient/
Source0:       http://downloads.sourceforge.net/project/gqclient/GQ%20Unstable/%{version}/gq-%{version}.tar.gz
Patch0:        gq-1.2.1-desktop.patch
Patch1:        gq-1.3.4-kerberos.patch
Patch2:        gq-1.3.4-configure.patch
Patch3:        gq-1.3.4-dso.patch
Patch4:        gq-1.3.4-glibfix.patch
Patch5:        gq-1.3.4-errorchain.patch
Patch6:        gq-1.3.4-strcmp-null-safe.patch
Patch7:        gq-1.3.4-sanity-check.patch
Patch8:        gq-1.3.4-format.patch
Patch9:        gq-1.3.4-openssl.patch
Patch10: gq-configure-c99.patch
BuildRequires: gcc
BuildRequires: gtk2-devel
BuildRequires: libglade2-devel
Buildrequires: libgcrypt-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libxml2-devel
BuildRequires: krb5-devel
Buildrequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: gnome-doc-utils
BuildRequires: openldap-devel
BuildRequires: openssl-devel
BuildRequires: perl(XML::Parser)
# for /usr/bin/iconv
BuildRequires: glibc-common
BuildRequires: make
%description
GQ is a graphical browser for LDAP directories and schemas.  Using GQ,
an administrator can search through a directory and modify objects
stored in that directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
for f in TODO AUTHORS ChangeLog ; do
    mv $f $f.iso88591
    iconv -f ISO-8859-1 -t UTF-8 -o $f $f.iso88591
    touch -r $f.iso88591 $f
    rm -f $f.iso88591
done

%build
export CFLAGS="%{optflags} -fcommon -Wno-incompatible-pointer-types -Wno-return-mismatch"
%configure --with-included-gettext      \
           --disable-update-mimedb      \
           --with-default-codeset=UTF-8 \
           --disable-scrollkeeper       \
           --enable-cache               \
           --enable-browser-dnd         \
           --with-kerberos-prefix=%{_prefix}/kerberos
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-install --delete-original      \
        --dir %{buildroot}%{_datadir}/applications          \
        %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README* TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/pixmaps/%{name}/*.xpm
%{_datadir}/pixmaps/%{name}/*.png
%{_datadir}/mime/packages/%{name}-ldif.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/omf/gq-manual
%{_datadir}/gnome/help/gq-manual
%{_datadir}/icons/hicolor/16x16/apps/ldap-*.png
%dir %{_datadir}/pixmaps/%{name}
%dir %{_datadir}/%{name}

%changelog
%autochangelog
