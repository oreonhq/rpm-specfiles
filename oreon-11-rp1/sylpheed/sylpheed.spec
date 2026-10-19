%global source0_hash eb23e6bda2c02095dfb0130668cf7c75d1f256904e3a7337815b4da5cb72eb04
%global desktopvendor redhat
%global is_prerelease 0
%if 0%{?is_prerelease}
%global prerelease rc2
%endif
Name:           sylpheed
Version:        3.7.0
Release:        1%{?dist}
Summary:        GTK+ based, lightweight, and fast email client
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            http://sylpheed.sraoss.jp/
Source0:        http://%{name}.sraoss.jp/%{name}/v3.7/%{name}-%{version}.tar.bz2
Source1:        sylpheed.1
%{!?_without_gpgme:BuildRequires: gpgme-devel}
%{!?_without_compface:BuildRequires: compface-devel}
%{!?_without_ldap:BuildRequires: openldap-devel}
%{?_with_oniguruma:BuildRequires: oniguruma-devel}
%{?_with_jpilot:BuildRequires: jpilot-devel}
Patch1:         sylpheed-3.1.0-defs.h.patch
Patch2:         sylpheed-3.5.0-desktop.patch
Patch3:         sylpheed-2.5.0-certsdir.patch
Patch4:         sylpheed-3.7.0-uri-check.patch
Patch5:         sylpheed-3.7.0-types.patch
Requires: sylpheed-libs%{?_isa} = %{version}-%{release}
Requires: xdg-utils
# oreon:deps
BuildRequires:  compface-devel
BuildRequires:  desktop-file-utils
BuildRequires:  enchant-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gpgme-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtkspell-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  xdg-utils
# /oreon:deps
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
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
pushd plugin/attachment_tool
make install-plugin DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
popd
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 sylpheed-64x64.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/sylpheed.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --delete-original \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sylpheed-libs -f %{oreon_filedir}/sylpheed-libs.list
%files -n sylpheed-devel -f %{oreon_filedir}/sylpheed-devel.list

%changelog

%autochangelog
