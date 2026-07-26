%global source0_hash 997ce4c6dfae8529ffceb1e834d663d145d3fb22d0d96fd70f22aaa84c5b77ec

Summary:        PGP encryption and signing for caja
Name:           seahorse-caja
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Version:        1.18.5
Release:        10%{?dist}
URL:            https://github.com/darkshram/%{name}
Source0:        https://github.com/darkshram/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch1:         seahorse-fix-building-w-gpgme2.patch

BuildRequires: make
BuildRequires: mate-common
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(gcr-3)
BuildRequires: gnupg2
BuildRequires: gpgme-devel >= 1.0
BuildRequires: pkgconfig(libcaja-extension)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(cryptui-0.0)
BuildRequires: pkgconfig(libnotify)

%if 0%{?rhel}
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%endif

%description
Seahorse caja is an extension for caja which allows encryption
and decryption of OpenPGP files using GnuPG.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 1 -p1 -b .fix-building-w-gpgme2

%build
autoreconf -fiv
%configure \
    --disable-silent-rules \
    --disable-gpg-check

make %{?_smp_mflags} V=1

%install
%{make_install}

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
find %{buildroot} -type f -name "*.a" -exec rm -f {} ';'

desktop-file-validate %{buildroot}%{_datadir}/applications/mate-seahorse-pgp-encrypted.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/mate-seahorse-pgp-keys.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/mate-seahorse-pgp-signature.desktop

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/mate-seahorse-tool
%{_libdir}/caja/extensions-2.0/libcaja-seahorse.so
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.mate.seahorse.caja.*gschema.xml
%{_datadir}/seahorse-caja/
%{_mandir}/man1/mate-seahorse-tool.1*

%changelog
%autochangelog
