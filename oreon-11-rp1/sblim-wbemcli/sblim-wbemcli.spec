%global source0_hash e493065a6a485ef19cdae5d2bb1561eb9aa4b3d53f35237f6c32cf101a93a796

Name:           sblim-wbemcli
Version:        1.6.3
Release:        31%{?dist}
Summary:        SBLIM WBEM Command Line Interface

License:        EPL-1.0
URL:            https://sourceforge.net/projects/sblim/
Source0:        https://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         sblim-wbemcli-1.5.1-gcc43.patch
Patch1:         sblim-wbemcli-1.6.2-https-segfaults.patch
Patch2:         sblim-wbemcli-1.6.1-ssl-proto-option.patch
Patch3:         sblim-wbemcli-1.6.3-fix-exit-status.patch
Patch4:         sblim-wbemcli-1.6.3-covscan-fixes.patch
Patch5:         sblim-wbemcli-1.6.3-fix-cmx-crash.patch

BuildRequires: make
BuildRequires:  curl-devel >= 7.9.3
BuildRequires:  binutils-devel >= 2.17.50.0.3-4
BuildRequires:  autoconf automake libtool pkgconfig
BuildRequires:  gcc-c++
Requires:       curl >= 7.9.3

%description
WBEM Command Line Interface is a standalone, command line WBEM client. It is
specially suited for basic systems management tasks as it can be used in
scripts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
autoreconf --install --force
%patch -P0 -p1 -b .gcc43
%patch -P1 -p1 -b .https-segfaults
%patch -P2 -p1 -b .ssl-proto-option
%patch -P3 -p1 -b .fix-exit-status
%patch -P4 -p1 -b .covscan-fixes
%patch -P5 -p1 -b .fix-cmx-crash

%build
%configure CACERT=/etc/pki/Pegasus/client.pem
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}

%files
%license COPYING
%{_bindir}/wbem*
%{_mandir}/man1/*
%{_datadir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.3-31
- Prepare for Oreon 11 (RP1)
