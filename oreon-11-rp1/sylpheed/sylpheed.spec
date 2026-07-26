%global source0_hash eb23e6bda2c02095dfb0130668cf7c75d1f256904e3a7337815b4da5cb72eb04

# should be vendor 'fedora', but that would break upgrades for
# people who have linked the desktop icon
%global desktopvendor redhat

%global is_prerelease 0

%if 0%{?is_prerelease}
%global prerelease rc2
%endif

Name:           sylpheed
Version:        3.7.0
Release:        20%{?prerelease:.%{?prerelease}}%{?dist}
Summary:        GTK+ based, lightweight, and fast email client

License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            http://sylpheed.sraoss.jp/
#VCS:           https://github.com/sylpheed-mail/sylpheed

Source0:        http://sylpheed.sraoss.jp/sylpheed/v3.7/%{name}-%{version}%{?prerelease}.tar.bz2
Source1:        sylpheed.1

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  openssl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  xdg-utils
%{!?_without_gpgme:BuildRequires: gpgme-devel}
%{!?_without_compface:BuildRequires: compface-devel}
%{!?_without_ldap:BuildRequires: openldap-devel}
%{?_with_oniguruma:BuildRequires: oniguruma-devel}
%{?_with_jpilot:BuildRequires: jpilot-devel}
BuildRequires:  gtkspell-devel
BuildRequires:  enchant-devel

# customisations for default program paths
Patch1:         sylpheed-3.1.0-defs.h.patch
# customisations in the .desktop file
Patch2:         sylpheed-3.5.0-desktop.patch
# customisation for /etc/pki/tls/
Patch3:         sylpheed-2.5.0-certsdir.patch
# harden link checker
# https://bugzilla.redhat.com/show_bug.cgi?id=1988552
Patch4:         sylpheed-3.7.0-uri-check.patch
# various type and format related fixes
Patch5:         sylpheed-3.7.0-types.patch

Requires: sylpheed-libs%{?_isa} = %{version}-%{release}
# For xdg-open in patch1
Requires: xdg-utils

%description
This program is an X based fast email client which has features like:

o user-friendly and intuitive interface
o integrated NetNews client (partially implemented)
o ability of keyboard-only operation
o Mew/Wanderlust-like key bind
o multipart MIME
o unlimited multiple account handling
o message queueing
o assortment function
o XML-based address book

See /usr/share/doc/sylpheed*/README for more information.

%package libs
Summary: Libraries for sylpheed

%description libs
This package contains libraries for Sylpheed.

%package devel
Summary: Development files for sylpheed
Requires: sylpheed-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for Sylpheed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup %{?prerelease:-n %{name}-%{version}%{?prerelease}} -p1

%build
%global optflags %{optflags} -std=gnu17

%configure --disable-silent-rules \
    --enable-ssl --disable-updatecheck \
    --with-plugindir=%{_libdir}/%{name}/plugins \
    %{!?_without_gpgme:--enable-gpgme} \
    %{?_without_compface:--disable-compface} \
    %{!?_without_ldap:--enable-ldap} \
    %{?_with_oniguruma:--enable-oniguruma} \
    %{?_with_jpilot:--enable-jpilot}
# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install

# Install plugins
pushd plugin/attachment_tool
make install-plugin DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
popd

find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

# Install an icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 sylpheed-64x64.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/sylpheed.png

# Install menu entries
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --delete-original \
  %if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor %{desktopvendor} \
  %endif
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

# Install the manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog ChangeLog-1.0 COPYING COPYING.LIB LICENSE
%doc NEWS NEWS-1.0 NEWS-2.0 README TODO
%lang(ja) %doc ChangeLog.ja ChangeLog-1.0.ja README.ja INSTALL.ja TODO.ja
%lang(es) %doc README.es
%{_bindir}/sylpheed
%{_datadir}/sylpheed/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{_libdir}/sylpheed/

%files libs
%doc COPYING COPYING.LIB LICENSE
%{_libdir}/libsylph-0.so.*
%{_libdir}/libsylpheed-plugin-0.so.*

%files devel
%doc PLUGIN.txt 
%lang(ja) %doc PLUGIN.ja.txt
%{_includedir}/sylpheed/
%{_libdir}/*.so

%changelog
%autochangelog
