%global source0_hash 4225eacefc30354f867dc14b7974efe8e8fcef031117def1098db652e1ad48b7
%global srcnm Qalculate
Summary:        A multi-purpose desktop calculator for GNU/Linux
Name:		qalculate-gtk
Version:	5.12.0
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		https://qalculate.github.io/
Source0:        https://github.com/%{srcnm}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires:	gnuplot
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libqalculate-devel
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
# /oreon:deps
%description
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides a (GTK+) graphical interface for Qalculate! 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i 's/<i>//' data/qalculate-gtk.appdata.xml.in
sed -i 's/<\/i>//' data/qalculate-gtk.appdata.xml.in

%build

%configure 
%make_build
%install
%make_install
pushd doc
cp -pr html %{buildroot}/%{_datadir}/doc/%{name}
popd
desktop-file-install --delete-original			\
	--remove-category Application			\
	--dir %{buildroot}%{_datadir}/applications	\
	--mode 0644					\
	%{buildroot}%{_datadir}/applications/qalculate-gtk.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
