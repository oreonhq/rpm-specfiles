%global source0_hash b6ec7937bf0f36c947d17f06539906c021681122789fefb07405f8c243f383b9
%global bbdbsupport 1
%global pkgdir %{_emacs_sitelispdir}/vm
%global etcdir %{_datadir}/emacs/vm
%global pixmapdir %{etcdir}/pixmaps
%global initfile %{_emacs_sitestartdir}/vm-init.el
Summary:        Emacs VM mail reader
Summary(sv): Emacs postläsare VM
Name: emacs-vm
%global forgeurl https://gitlab.com/emacs-vm/vm/
%global version0 8.3.2
%global commit edecae201ca7261e0d5adedded25cea0bbaea432
%forgemeta
Version: %forgeversion
Release:        1%{?dist}
License: GPL-1.0-or-later AND GPL-2.0-or-later
URL: %forgeurl
Source0:        %{forgeurl}/-/archive/%{commit}/vm-%{commit}.tar.bz2
Source1: emacs-vm.metainfo.xml
Patch: marker-pointer.patch
Requires: emacs(bin) >= %{_emacs_version}
BuildArch: noarch
Requires: emacs-bbdb
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  emacs
BuildRequires:  emacs-bbdb
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# /oreon:deps
%description
VM (View Mail) is an Emacs subsystem that allows e-mail to be read
and disposed of within Emacs.  Commands exist to do the normal things
expected of a mail user agent, such as generating replies, saving
messages to folders, deleting messages and so on.  There are other
more advanced commands that do tasks like bursting and creating
digests, message forwarding, and organizing message presentation
according to various criteria. 

%description -l sv
VM (View Mail) är ett undersystem för Emacs som gör att e-post
kan läsas och hanteras inifrån Emacs.  Det finns kommandon för att
göra de vanliga sakerna som förväntas av ett postprogram, såsom skapa
svar, spara meddelanden till mappar, radera meddelanden och så vidare.
Det finns andra mer avancerade kommandon som gör saker som att
splittra upp eller skapa sammandrag, vidarebefordra meddelanden och
organisera presentationen av meddelanden enligt olika kriterier.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

autoupdate
autoconf
%configure --with-etcdir=%{etcdir} --with-docdir=%{_pkgdocdir}
make
%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}/%{_emacs_sitestartdir}
echo "(require 'vm-autoloads)" > %{buildroot}/%{initfile}
install -d %{buildroot}%{_datadir}/metainfo
cp -p %{SOURCE1} %{buildroot}%{_datadir}/metainfo
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
	       %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
