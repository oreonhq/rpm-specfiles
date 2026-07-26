%global source0_hash 1c0e8c7e7a339b2f045624787e9d2b0616ca011ec7484c76502cd4191c9359cd

%define svn_revision 39
%define snapshot_date 20071107

Name:           upslug2
Version:        0.0
Release:        0.35.%{snapshot_date}.svn%{svn_revision}%{?dist}
Summary:        Firmware update utility for the nslu2
License:        MIT
URL:            http://www.nslu2-linux.org/wiki/Main/UpSlug2
# To recreate:
# svn export -r %{svn_revision} http://svn.nslu2-linux.org/svnroot/upslug2/trunk %{name}
# tar cvfz %{name}-svn-%{svn_revision}.tar.gz %{name}
Source0:        %{name}-svn-%{svn_revision}.tar.gz
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  automake libpcap-devel

%description
upslug2 is a command line program intended to allow the upgrade of a LinkSys
NSLU2 firmware to new or different versions.  Unlike upslug and the LinkSys
(Sercomm) upgrade utilities, upslug2 will synthesise a complete 'image'
from a kernel and a root file system, as such it duplicates part of the
functionality of 'slugimage'.

upslug2 also optimizes the upload to avoid transmitted parts of the image which
need not be written or are 'blank' (set to the erased flash value of all 1's).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
autoreconf -i

%build
%configure --with-libpcap
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -p -m 644 upslug2.8 $RPM_BUILD_ROOT/%{_mandir}/man8

%files
%doc AUTHORS ChangeLog COPYING README
%{_sbindir}/upslug2
%{_mandir}/man8/upslug2.8.gz

%changelog
%autochangelog
