%global source0_hash 0333e160fa5ed0a7d3aa2f80904bb48b2a16455439f2896a49d2695dfccaaddb
Name:		xgridloc
Version:	1.8.4
Release:        13%{?dist}
Summary:        A GTK+ application for the calculation of Maidenhead QRA Locators
License:	GPL-3.0-only
URL:		https://www.qsl.net/5b4az/
Source0:        https://www.qsl.net/5b4az/pkg/locator/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0: xgridloc-configure-c99.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
xgridloc is a GTK+ graphical version of gridloc and performs the same basic
functions for ham radio operators, but additionally it can use xplanet to
display the home and DX locations and the great circle path between them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/pixmaps/
ln -rs %{buildroot}%{_datadir}/%{name}/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
desktop-file-install  \
	--dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
