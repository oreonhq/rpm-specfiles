%global source0_hash d28a9b17ec54eab29f39e3dbd490956e9a588357209d523b1978c3df40d7bee2

Name:    sugar-artwork
Summary: Artwork for Sugar look-and-feel
Version: 0.121
Release: 7%{?dist}
URL:     http://sugarlabs.org
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Patch0: empy-fix.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: perl-XML-Parser
BuildRequires: python3
BuildRequires: python3-empy
BuildRequires: icon-naming-utils
BuildRequires: xcursorgen
BuildRequires: autoconf automake libtool
Requires: gtk3

# Disable generation of useless debuginfo package, which fails to build, causing an abort
# See https://fedoraproject.org/wiki/Packaging:Debuginfo?rd=Packaging/Debuginfo#Debuginfo_packages
%global debug_package %{nil}

%description
sugar-artwork contains the themes and icons that make up the Sugar default
look and feel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -vif
%configure --without-gtk2
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete

%post
touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :

%postun
touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :

%files
%license COPYING
%{_datadir}/icons/sugar
%{_datadir}/icons/sugar-lh

#gtk3
%{_datadir}/themes/sugar-100/gtk-3.0/gtk.css
%{_datadir}/themes/sugar-100/gtk-3.0/gtk-widgets.css
%{_datadir}/themes/sugar-100/gtk-3.0/settings.ini
%{_datadir}/themes/sugar-100/gtk-3.0/assets/*
%{_datadir}/themes/sugar-100/gtk-3.20/gtk.css
%{_datadir}/themes/sugar-100/gtk-3.20/gtk-widgets.css
%{_datadir}/themes/sugar-100/gtk-3.20/assets/*
%{_datadir}/themes/sugar-72/gtk-3.0/gtk.css
%{_datadir}/themes/sugar-72/gtk-3.0/gtk-widgets.css
%{_datadir}/themes/sugar-72/gtk-3.0/settings.ini
%{_datadir}/themes/sugar-72/gtk-3.0/assets/*
%{_datadir}/themes/sugar-72/gtk-3.20/gtk.css
%{_datadir}/themes/sugar-72/gtk-3.20/gtk-widgets.css
%{_datadir}/themes/sugar-72/gtk-3.20/assets/*

%changelog
%autochangelog
