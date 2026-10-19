%global source0_hash 5145aa844e54cca89ddab6fb7dd9e5952811d8d787c4f4bf27eb261e6c182098
Name:		mcrypt
Version:	2.6.8
Release:        39%{?dist}
License:	GPL-3.0-or-later
Summary:        Replacement for crypt()
URL:		http://mcrypt.sourceforge.net/
Source0:        http://download.sourceforge.net/mcrypt/mcrypt-%{version}.tar.gz
Patch0:		mcrypt-rfc2440-bugfixes.patch
Patch1:		mcrypt-2.6.7-format_strings.patch
Patch2:		mcrypt-2.6.7-gaafix.patch
Patch3:		mcrypt-2.6.7-native-by-default.patch
Patch4:		mcrypt-2.6.8-manpage-typofixes.patch
Patch5:		mcrypt-CVE-2012-4409.patch
Patch6:		mcrypt-2.6.8-no-gaa.patch
Patch7:		mcrypt-CVE-2012-4527-80-width-patch
Patch8:		mcrypt-2.6.8-c23.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libmcrypt-devel
BuildRequires:  make
BuildRequires:  mhash-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
