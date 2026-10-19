%global source0_hash 359c84d61198c4b4b62930e21670c077c380a41a121f299313330907967949db
Name:           ldapvi
Version:        1.8
Release:        1%{?dist}
Summary:        An interactive LDAP client
License:        GPL-2.0-or-later
URL:            http://www.lichteblau.com/ldapvi/
Source0:        http://www.lichteblau.com/download/ldapvi-%{version}.tar.gz
Patch0:         GNUmakefile.in.patch
Patch1:         %{name}-1.7-getline.patch
Patch2:         dont-set-encoding-in-vim-modeline.diff
Patch3:         ldapvi-1.7-fix-use-after-free-in-sasl-code.patch
Patch4:         ldapvi-1.7-incorrect-FSF-address.patch
Patch5:         0001-Don-t-switch-off-canonical-mode.patch
Patch6:         ldapvi-c99-1.patch
Patch7:         ldapvi-c99-2.patch
Patch8:         ldapvi-c99-3.patch
Patch9:         ldapvi-c99-4.patch
Patch10:        ldapvi-c99-5.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
ldapvi is an interactive LDAP client for Unix terminals. Using it, you can
update LDAP entries with a text editor, which is the same as vi. Think of
it as vipw(1) for LDAP.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .gnumk
%patch -P1 -p2 -b .getline
%patch -P2 -p2 -b .encoding
%patch -P3 -p2 -b .doubleFree
%patch -P4 -p1 -b .FSFaddress
%patch -P5 -p1 -b .nopassword
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P 10 -p1

%build

%set_build_flags
CFLAGS="$CFLAGS -DLDAP_DEPRECATED"
%configure
%make_build
cd manual
make manual.html
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
