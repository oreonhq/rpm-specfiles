%global source1_hash 915bba33382697c109f134c943d506d00a340578acda6d9424a5f42d19207782
%global source0_hash a358e890441486821e44b0c4a68494cbc15fc0d9351298bb91dd1a2b381f5bd6
Name:		isomaster
Summary:        An easy to use GUI CD image editor
Version:	1.3.17
Release:        1%{?dist}
License:	GPL-2.0-only
URL:		http://littlesvr.ca/isomaster/
Source0:        http://littlesvr.ca/isomaster/releases/isomaster-%{version}.tar.bz2
Source1:	http://timeoff.wsisiz.edu.pl/rpms/isomaster/text-editor-0.1.tar.gz
Patch1:		isomaster-1.3.17-desktop.diff
Patch2:		isomaster-1.3.17-iniparser-include.patch
Requires:	xdg-utils
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  iniparser-devel
BuildRequires:  make
# /oreon:deps
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
make %{?_smp_mflags} PREFIX=%{_prefix} OPTFLAGS="%{optflags}" USE_SYSTEM_INIPARSER=1 DEFAULT_VIEWER=xdg-open DEFAULT_EDITOR=text-editor.sh
%install
rm -fr %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} USE_SYSTEM_INIPARSER=1
cp text-editor.sh %{buildroot}%{_bindir}/text-editor.sh
%find_lang %{name}
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	--delete-original \
	--add-category="Audio" \
	--add-category="Video" \
	%{buildroot}%{_datadir}/applications/isomaster.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
