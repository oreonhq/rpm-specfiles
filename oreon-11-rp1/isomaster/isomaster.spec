%global source0_hash 915bba33382697c109f134c943d506d00a340578acda6d9424a5f42d19207782

Name:		isomaster
Summary:	An easy to use GUI CD image editor
Version:	1.3.17
Release:	6%{?dist}
License:	GPL-2.0-only
URL:		http://littlesvr.ca/isomaster/
#moved to .rpmmacros
#Packager:	Marcin Zajaczkowski <mszpak ATT wp DOTT pl>
Source0:	http://littlesvr.ca/isomaster/releases/isomaster-%{version}.tar.bz2
Source1:	http://timeoff.wsisiz.edu.pl/rpms/isomaster/text-editor-0.1.tar.gz
Patch1:		isomaster-1.3.17-desktop.diff
Patch2:		isomaster-1.3.17-iniparser-include.patch
#to call viewers for the files
Requires:	xdg-utils
BuildRequires:	gcc
#author is not sure about gtk2 version, but 2.8 should be enough
BuildRequires:	gtk2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:  iniparser-devel >= 4.1
BuildRequires: make

%description
ISO Master: an easy to use graphical CD image editor. 
It allows to extract files from an ISO, add files to an ISO, 
and create bootable ISOs - all in a graphical user interface.
It can open ISO, NRG, and some MDF files but can only save as ISO.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%setup -q -T -D -a 1
%patch -P1 -p0
%patch -P2 -p1

%build
rm -rf iniparser-4.1
#PREFIX is required to specify a correct dir for icons
make %{?_smp_mflags} PREFIX=%{_prefix} OPTFLAGS="%{optflags}" USE_SYSTEM_INIPARSER=1 DEFAULT_VIEWER=xdg-open DEFAULT_EDITOR=text-editor.sh

%install
rm -fr %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} USE_SYSTEM_INIPARSER=1
cp text-editor.sh %{buildroot}%{_bindir}/text-editor.sh

%find_lang %{name}

desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
	-vendor fedora \
%endif
	--dir %{buildroot}%{_datadir}/applications \
	--delete-original \
	--add-category="Audio" \
	--add-category="Video" \
	%{buildroot}%{_datadir}/applications/isomaster.desktop

%files -f %{name}.lang
%attr(0755,root,root) %{_bindir}/isomaster
%attr(0755,root,root) %{_bindir}/text-editor.sh
%{_datadir}/%{name}
%doc CHANGELOG.TXT CREDITS.TXT LICENCE.TXT README.TXT TODO.TXT
%{_datadir}/applications/*isomaster.desktop
%{_mandir}/man1/isomaster.1*

%changelog
%autochangelog
