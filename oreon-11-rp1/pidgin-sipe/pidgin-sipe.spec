%global source0_hash 5a42810e447c3af2632961e88d7c683b6619aeda03accdcbaad222d8337ec676

Name:           pidgin-sipe
Summary:        Pidgin protocol plugin to connect to MS Office Communicator
Version:        1.25.0
Release:        24%{?dist}

License:        GPL-2.0-or-later
URL:            http://sipe.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/sipe/sipe/pidgin-sipe-%{version}/pidgin-sipe-%{version}.tar.bz2
Patch1:         pidgin-sipe-1.25.0-fix-false-negative-configure-checks.patch
Patch2:         pidgin-sipe-1.25.0-fix-glib-2.68-build.patch
Patch3:         pidgin-sipe-1.25.0-fix-libxml2-2.12-build.patch
Patch4:         pidgin-sipe-1.25.0-add-appstreamcli-no-net.patch
Patch5:         pidgin-sipe-1.25.0-core-fix-build-for-stricter-strstr.patch

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(gio-2.0) >= 2.18.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.18.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.18.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-rtp-1.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nice) >= 0.1.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(purple) >= 2.8.0
BuildRequires:  appstream
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gssntlmssp-devel >= 0.5.0
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make

%if ! 0%{?rhel}
BuildRequires:  pkgconfig(freerdp-shadow2)
%endif

Requires:       purple-sipe = %{version}-%{release}


%description
A third-party plugin for the Pidgin multi-protocol instant messenger.
It implements the extended version of SIP/SIMPLE used by various products:

    * Skype for Business
    * Microsoft Office 365
    * Microsoft Business Productivity Online Suite (BPOS)
    * Microsoft Lync Server
    * Microsoft Office Communications Server (OCS 2007/2007 R2)
    * Microsoft Live Communications Server (LCS 2003/2005)

With this plugin you should be able to replace your Microsoft Office
Communicator client with Pidgin.

This package provides the icon set for Pidgin.


%package -n purple-sipe
Summary:        Libpurple protocol plugin to connect to MS Office Communicator
License:        GPL-2.0-or-later

Requires:       gssntlmssp >= 0.5.0

%description -n purple-sipe
A third-party plugin for the Pidgin multi-protocol instant messenger.
It implements the extended version of SIP/SIMPLE used by various products:

    * Skype for Business
    * Microsoft Office 365
    * Microsoft Business Productivity Online Suite (BPOS)
    * Microsoft Lync Server
    * Microsoft Office Communications Server (OCS 2007/2007 R2)
    * Microsoft Live Communications Server (LCS 2003/2005)

This package provides the protocol plugin for libpurple clients.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
# steps copied from "autogen.sh" in upstream source tree
autopoint --force
AUTOPOINT="intltoolize --copy --force --automake" \
    autoreconf --force --install

%configure \
    --with-krb5 \
    --with-vv \
    --enable-purple \
    --disable-telepathy
%make_build


%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Pidgin doesn't have 24 or 32 pixel icons
rm -f \
   %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/24/sipe.png \
   %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/32/sipe.png
%find_lang %{name}


%if ! 0%{?rhel}
%check
%make_build check
%endif

%files -n purple-sipe -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_libdir}/purple-2/libsipe.so


%files
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/pixmaps/pidgin/protocols/*/sipe.*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.25.0-24
- Prepare for Oreon 11 (RP1)
