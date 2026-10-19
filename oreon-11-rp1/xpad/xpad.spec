%global source0_hash 16c35f52cd550a7bf920a57aa07ed7bfda6fa9eec50a98024e93acb7fe16dca3
Name:           xpad
Version:        5.9.0
Release:        1%{?dist}
Summary:        Sticky notepad for GTK
License:        GPL-3.0-or-later
URL:            https://launchpad.net/xpad
Source0:        https://launchpad.net/xpad/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
Patch1:         xpad-5.8.0-gettext-version.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  intltool
BuildRequires:  libSM-devel
BuildRequires:  libappstream-glib
BuildRequires:  libayatana-appindicator-gtk3-devel
BuildRequires:  make
# /oreon:deps
%description
Xpad is a sticky note application that strives to be simple, fault-tolerant, 
and customizable. It consists of independent pad windows; each is basically a 
text box in which notes can be written. Despite being called xpad, all that is
needed to run or compile it is the GTK+ 2.0 libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
desktop-file-install  \
        --delete-original \
        --dir=%{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
