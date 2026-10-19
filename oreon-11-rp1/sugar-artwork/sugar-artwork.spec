%global source0_hash d28a9b17ec54eab29f39e3dbd490956e9a588357209d523b1978c3df40d7bee2
Name:    sugar-artwork
Summary:        Artwork for Sugar look-and-feel
Version: 0.121
Release:        1%{?dist}
URL:     http://sugarlabs.org
License: Apache-2.0
Source0:        http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Patch0: empy-fix.patch
Requires: gtk3
%global debug_package %{nil}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  icon-naming-utils
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-XML-Parser
BuildRequires:  python3
BuildRequires:  python3-empy
BuildRequires:  xcursorgen
# /oreon:deps
%description
sugar-artwork contains the themes and icons that make up the Sugar default
look and feel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure --without-gtk2
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
%oreon_autofiles main

%post

touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :
%postun

touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
