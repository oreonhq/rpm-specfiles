%global source2_hash 12f7beb58539e33b1e697bfb1d43cfed7e99c09e6050dd11e94dfa59588c8010
%global source1_hash 4ba4045edf88af0ca728278718fe3d30264b710dae0360d3761e01dfe0b789c7
%global source0_hash 67388ac405f9fe92a40636cb03b0e1e0bb6403ad89ccc174b2ff190ef6f32349
%global source2_key_fpr BB09FFB87563FA2E1A22146817A6D3FF338C9570
Summary:        Gnome Partition Editor
Name:		gparted
Version:	1.8.1
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		http://gparted.org
Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	https://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz.sig
Source2:	https://keys.openpgp.org/vks/v1/by-fingerprint/BB09FFB87563FA2E1A22146817A6D3FF338C9570
Requires:	PolicyKit-authentication-agent
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  gpgverify
BuildRequires:  gtkmm30-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  parted-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  polkit
BuildRequires:  polkit-devel
# /oreon:deps
%description
GParted stands for Gnome Partition Editor and is a graphical frontend to
libparted. Among other features it supports creating, resizing, moving
and copying of partitions. Also several (optional) filesystem tools provide
support for filesystems not included in libparted. These optional packages
will be detected at runtime and don't require a rebuild of GParted

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -p1

%build

%configure --enable-libparted-dmraid --enable-online-resize --enable-xhost-root
%make_build
%install
%make_install
sed -i 's#_X-GNOME-FullName#X-GNOME-FullName#' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's#sbin#bin#' %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --delete-original			\
	--dir %{buildroot}%{_datadir}/applications	\
	--mode 0644					\
	--add-category X-Fedora				\
	--add-category GTK				\
	%{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/metainfo
%{__install} -p -m755 %{name}.appdata.xml %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
