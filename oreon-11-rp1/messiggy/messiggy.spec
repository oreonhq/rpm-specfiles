%global source0_hash 50e3669d607bd73b36bd96df6f4b57364107b81f8b6b167b256f7ce005b15772

Name:		messiggy
Version:	0.5.0
Release:	37%{?dist}
Summary:	Messiggy is a database of celestial objects

License:	GPL-2.0-or-later
URL:		http://www.coyotegulch.com/products/messiggy/index.html
Source0:	http://www.coyotegulch.com/distfiles/%{name}-%{version}.tar.gz
Source1:	messiggy.desktop
Patch0:		messiggy-format-string.patch
Patch1: messiggy-configure-c99.patch
Patch2: messiggy-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	itzam-core-devel, gtk2-devel, desktop-file-utils, hicolor-icon-theme

%description
Messiggy is a database of celestial objects, as cataloged by the French
astronomer Charles Messier in the mid-18th century.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
ln -s %{_datadir}/messiggy/pixmaps/messiggy.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/messiggy.png

%files
%doc ChangeLog COPYING README
%{_bindir}/messiggy
%{_datadir}/messiggy
%{_datadir}/applications/messiggy.desktop
%{_datadir}/icons/hicolor/32x32/apps/messiggy.png

%changelog
%autochangelog
