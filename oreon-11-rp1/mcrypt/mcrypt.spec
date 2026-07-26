%global source0_hash 5145aa844e54cca89ddab6fb7dd9e5952811d8d787c4f4bf27eb261e6c182098

Name:		mcrypt
Version:	2.6.8
Release:	39%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Summary:	Replacement for crypt()
URL:		http://mcrypt.sourceforge.net/
Source0:	http://download.sourceforge.net/mcrypt/mcrypt-%{version}.tar.gz
# From upstream, a combination of:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1191020&group_id=87941&atid=584895
# http://sourceforge.net/tracker/index.php?func=detail&aid=1872812&group_id=87941&atid=584895
Patch0:		mcrypt-rfc2440-bugfixes.patch
# From upstream:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1872809&group_id=87941&atid=584895
Patch1:		mcrypt-2.6.7-format_strings.patch
# Upstream:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1829488&group_id=87941&atid=584895
Patch2:		mcrypt-2.6.7-gaafix.patch
# Upstream:
# http://sourceforge.net/tracker/index.php?func=detail&aid=2075758&group_id=87941&atid=584895
Patch3:		mcrypt-2.6.7-native-by-default.patch
# Upstream: 
# https://sourceforge.net/tracker/index.php?func=detail&aid=3559099&group_id=87941&atid=584893
Patch4:		mcrypt-2.6.8-manpage-typofixes.patch
# Fix for CVE-2012-4409
# https://bugzilla.redhat.com/show_bug.cgi?id=855029
Patch5:		mcrypt-CVE-2012-4409.patch
# No gaa in Fedora
Patch6:		mcrypt-2.6.8-no-gaa.patch
# Fix for CVE-2012-4527 (workaround, really)
Patch7:		mcrypt-CVE-2012-4527-80-width-patch
# c23
Patch8:		mcrypt-2.6.8-c23.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libmcrypt-devel, mhash-devel, gettext, zlib-devel

%description
MCrypt is a replacement for the old crypt() package and crypt(1) command, 
with extensions. It allows developers to use a wide range of encryption 
functions, without making drastic changes to their code. It allows users 
to encrypt files or data streams without having to be cryptographers. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1 -b .format_strings
%patch -P2 -p1 -b .gaafix
%patch -P3 -p1 -b .native_by_default
%patch -P4 -p1 -b .typos
%patch -P5 -p1 -b .CVE-2012-4409
%patch -P6 -p1 -b .no-gaa
%patch -P7 -p1 -b .CVE-2012-4527
%patch -P8 -p1 -b .c23

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
