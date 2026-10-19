%global source0_hash 185996756885564f2ac1a231a618ec0ae70cc9b3a24e9b67d5761d5db899b5fb
%define vmsupport 1
%define lispdir %{_emacs_sitelispdir}/bbdb
Name:           emacs-bbdb
Version:        3.2.2b
Release:        1%{?dist}
Epoch:          1
Summary:        A contact management utility for use with Emacs
Summary(sv):    Ett verktyg för att hantera kontakter i Emacs
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
URL:            http://savannah.nongnu.org/projects/bbdb/
Source0:        bbdb-20220729.tar.xz
Source1:	emacs-bbdb.metainfo.xml
Patch0:		bbdb-3.2-migrate-fix.patch
Patch1:		bbdb-3.2-mh-folder-mode-fix.patch
Patch2:         bbdb-compiler-warnings.patch
BuildArch:      noarch
%if %{vmsupport}
%endif
Requires:       emacs(bin) >= %{_emacs_version}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  emacs
BuildRequires:  emacs-vm
BuildRequires:  info
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# /oreon:deps
%description 
BBDB is the Insidious Big Brother Database contact manager for GNU
Emacs.  It provides an address book for email and snail mail
addresses, phone numbers and the like.  It can be linked with various
Emacs mail clients (Message and Mail mode, Rmail, Gnus, MH-E, and VM).
BBDB is fully customizable.

%description -l sv
BBDB är kontakthanteraren Insidious Big Brother Database för GNU
Emacs.  Den tillhandahåller en adressbok för e-post och traditionella
postadresser, telefonnummer och liknande.  Den kan kopplas ihop med
olika Emacs-postklienter (Message- och Mail-läge, Rmail, Gnus, MH-E
och VM).  BBDB går att anpassa fullständigt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bbdb
%oreon_prep
%build

./autogen.sh
%if %{vmsupport}
%configure --with-lispdir=%{_emacs_sitelispdir}/bbdb --with-vm-dir=%{_emacs_sitelispdir}/vm
%else
%configure --with-lispdir=%{_emacs_sitelispdir}/bbdb
%endif
make all
%install
make DESTDIR=%{buildroot} install
install -d $RPM_BUILD_ROOT%{_emacs_sitestartdir}
cat > $RPM_BUILD_ROOT%{_emacs_sitestartdir}/bbdb-init.el << EOF
(require 'bbdb-loaddefs)
EOF
mv %{buildroot}%{_docdir}/bbdb %{buildroot}%{_pkgdocdir}
rm %{buildroot}%{_pkgdocdir}/COPYING
rm %{buildroot}%{_infodir}/dir
rm %{buildroot}%{_infodir}/bbdb.info
rm %{buildroot}%{_pkgdocdir}/bbdb.pdf
install -d %{buildroot}%{_datadir}/metainfo
cp -p %{SOURCE1} %{buildroot}%{_datadir}/metainfo
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
	       %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
