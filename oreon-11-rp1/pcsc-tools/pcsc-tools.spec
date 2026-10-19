%global source2_hash adf955683d9a7316d29431b3511b943fc357fed47bb9ae960f57c6cd3fd9c4ec
%global source1_hash 7c2bd8cbe546d36a09bd9c565c8da556fe5f432ecfbf5fd2285aa91b55b4a6be
%global source0_hash bb87fe4a50222b6e34d11eb6e35bd6eceb830eb2f6dd4bf2a0d43381c3d1da2c
Name:           pcsc-tools
Version:        1.7.5
Release:        1%{?dist}
Summary:        Tools to be used with smart cards and PC/SC
License:        GPL-2.0-or-later
URL:            https://pcsc-tools.apdu.fr/
Source0:        https://pcsc-tools.apdu.fr/%{name}-%{version}.tar.bz2
Source1:        https://pcsc-tools.apdu.fr/%{name}-%{version}.tar.bz2.asc
Source2:        https://pcsc-tools.apdu.fr/smartcard_list.txt
Source3:        LICENCE
Requires:       pcsc-lite
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  pcsc-lite-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
The pcsc-tools package contains some useful tools for a PC/SC user:
pcsc_scan regularly scans connected PC/SC smart card readers and
prints detected events, ATR_analysis analyzes smart card ATRs (Anwser
To Reset), and scriptor sends commands to a smart card.

%package gscriptor
Summary:        GUI tool to send command to a smart card
Requires:       %{name} = %{version}-%{release}
%description gscriptor
The pcsc-tools-gscriptor package contains graphical tool gscriptor which
can send commands to a smart card. It has GTK user interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
[ -f LICENCE ] || cp -a %{SOURCE3} LICENCE
cp -a %{SOURCE2} smartcard_list.txt

%build

%configure
make %{?_smp_mflags} CPPFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --mode=644 \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications gscriptor.desktop
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pcsc-tools-gscriptor -f %{oreon_filedir}/pcsc-tools-gscriptor.list

%changelog

%autochangelog
