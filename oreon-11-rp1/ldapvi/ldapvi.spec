%global source0_hash 6f62e92d20ff2ac0d06125024a914b8622e5b8a0a0c2d390bf3e7990cbd2e153

Name:           ldapvi
Version:        1.7
Release:        54%{?dist}
Summary:        An interactive LDAP client

License:        GPL-2.0-or-later
URL:            http://www.lichteblau.com/ldapvi/
Source0:        http://www.lichteblau.com/download/ldapvi-%{version}.tar.gz
Patch0:         GNUmakefile.in.patch
Patch1:         %{name}-1.7-getline.patch
# discussed upstream
# http://lists.askja.de/pipermail/ldapvi/2011-January/000089.html
# but never applied
Patch2:         dont-set-encoding-in-vim-modeline.diff
# Reported upstream
# http://lists.askja.de/pipermail/ldapvi/2013-April/000114.html
Patch3:         ldapvi-1.7-fix-use-after-free-in-sasl-code.patch
# Reported upstream
# http://lists.askja.de/pipermail/ldapvi/2013-September/000116.html
Patch4:         ldapvi-1.7-incorrect-FSF-address.patch
# http://lists.askja.de/pipermail/ldapvi/2017-December/000120.html
Patch5:         0001-Don-t-switch-off-canonical-mode.patch
Patch6:         ldapvi-c99-1.patch
Patch7:         ldapvi-c99-2.patch
Patch8:         ldapvi-c99-3.patch
Patch9:         ldapvi-c99-4.patch
Patch10:        ldapvi-c99-5.patch

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
# Declare additional historic OpenLDAP functions in header files.
CFLAGS="$CFLAGS -DLDAP_DEPRECATED"
%configure
%make_build
cd manual
make manual.html

%install
%make_install

%files
%license COPYING
%doc NEWS manual/bg.png manual/manual.html manual/manual.css
%{_mandir}/man1/ldapvi.1*
%{_bindir}/ldapvi

%changelog
%autochangelog
