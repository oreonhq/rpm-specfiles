%global source0_hash 91a4b587be1840e69a0e456c8f3ac131da6841f60b53c1e6b32556289a08b4f9

Name:		gdigi
Version:	0.4.0
Release:	20140231gitcada964d%{?dist}
Summary:	Utility to control DigiTech effect pedals
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		http://desowin.org/gdigi/
Source0:	http://downloads.sourceforge.net/project/gdigi/gdigi/%{version}/%{name}-%{version}.tar.bz2
Source1:	gdigi.png
Source2:	icon.png
Patch0:		gdigi-0.4.0-git.patch
Patch1:		gdigi-define_var_as_extern.patch
BuildRequires:  gcc
BuildRequires:	expat-devel gtk3-devel alsa-lib-devel libxml2-devel desktop-file-utils
BuildRequires: make

%description
%{name} is a tool aimed to provide X-Edit functionality to Linux users.

Supported devices: RP150, RP155, RP250, RP255, RP355, RP500, RP1000,
		   GNX3000, GNX4K.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
mkdir -p $RPM_BUILD_DIR/%{name}-%{version}/images
install -m 644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_DIR/%{name}-%{version}/images/

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/%{_datadir}/applications/
mkdir -p %{buildroot}/%{_datadir}/icons/
mkdir -p %{buildroot}/%{_mandir}/man1/
make install DESTDIR=%{buildroot}
install -p -m 644 gdigi.1 %{buildroot}/%{_mandir}/man1/gdigi.1
desktop-file-validate %{buildroot}/%{_datadir}/applications/gdigi.desktop

%files
%doc AUTHORS COPYING HACKING README TODO
%{_bindir}/gdigi
%{_mandir}/man1/gdigi.1.gz
%{_datadir}/applications/gdigi.desktop
%{_datadir}/icons/gdigi.png

%changelog
%autochangelog
