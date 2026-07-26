%global source0_hash dc1cddb165983ba66f2863c8314d39d077aadf53e4e5802afc5eea4eef46cb36

Name:		stripesnoop
Version:	1.5
Release:	43%{?dist}
License:	GPL-1.0-or-later
Summary:	Magnetic Stripe Reader
URL:		http://stripesnoop.sourceforge.net
Source0:	http://download.sourceforge.net/stripesnoop/ss-%{version}-src.zip
Patch0:		stripesnoop-1.5-rpmoptflags.patch
Patch1:		stripesnoop-1.5-deflinux.patch
Patch2:		stripesnoop-1.5-asmio.patch
Patch3:		stripesnoop-1.5-pathing.patch
Provides:	stripesnoop-devel = %{version}-%{release}
Obsoletes:	stripesnoop-devel
# ppc and other arches have no inb/outb
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=240499
ExclusiveArch:	%{ix86} x86_64
BuildRequires: make
BuildRequires:	gcc, gcc-c++

%description
Stripe Snoop is a suite of research tools that captures, modifies, validates, 
generates, analyzes, and shares data from magstripe cards. Numerous readers 
are supported to gather this information. In addition to simply displaying 
the raw characters that are encoded on the card, Stripe Snoop has a database 
of known card formats. It uses this to give you more detailed information 
about the card.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
%ifarch ppc
%patch -P2 -p1
%endif
%patch -P3 -p1
chmod -x cards.txt ChangeLog.txt COPYING.txt README.txt visa-pre.txt \
	 hardware/* samples/*

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m0644 dl-iin.csv visa-pre.txt $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -m0755 bitgen mod10 $RPM_BUILD_ROOT/%{_bindir}
install -m0755 ss $RPM_BUILD_ROOT/%{_bindir}/stripesnoop

%files
%doc ChangeLog.txt COPYING.txt README.txt hardware/ samples/
%{_bindir}/stripesnoop
%{_bindir}/bitgen
%{_bindir}/mod10
%{_datadir}/%{name}/

%changelog
%autochangelog
