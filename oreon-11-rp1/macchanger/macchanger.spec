%global source0_hash dae2717c270fd5f62d790dbf80c19793c651b1b26b62c101b82d5fdf25a845bf

Name:           macchanger
Version:        1.7.0
Release:        30%{?dist}
Summary:        An utility for viewing/manipulating the MAC address of network interfaces
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later

URL:            https://github.com/alobbs/macchanger
#               http://www.alobbs.com/macchanger

#Source0:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
#Source1:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig

Source0:        https://github.com/alobbs/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

# no OUI update at the moment
#Patch0:         macchanger-1.X.0-OUI-list-update.diff

# prefer /dev/urandom as source of seed for random
Patch1:         macchanger-1.7.0-seed-source.diff
# fix compile time warnings to make package build with -Werror
Patch2:         macchanger-1.7.0-werror.diff

# texinfo is only needed when .info rebuild is required
#BuildRequires:    texinfo
BuildRequires: make
BuildRequires:  gcc

%description
Features:
  * set specific MAC address of a network interface
  * set the MAC randomly
  * set a MAC of another vendor
  * set another MAC of the same vendor
  * reset MAC address to its original permanent hardware value
  * display a vendor MAC list (more than 18000 items)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .seedsource
%patch -P2 -p1 -b .werror

%build
CFLAGS="$RPM_OPT_FLAGS -Werror"
%configure
make %{?_smp_mflags} V=1

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_infodir}/*.info.*
%{_mandir}/man1/*

%changelog
%autochangelog
