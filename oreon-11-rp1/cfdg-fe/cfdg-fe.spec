%global source0_hash none

Name: cfdg-fe
Version:  0.1
Release:  40%{?dist}
Summary: A front end to cfdg

License: GPL-2.0-or-later
URL: http://impulzus.com/~tchibo/ 
Source0: http://impulzus.com/~tchibo/cfdg-fe.tgz_
Source1: cfdg-fe.desktop
Patch0: cfdg-fe-pixmap-path.patch
Patch1: pointer-types.patch
BuildRequires:  gcc
BuildRequires: autoconf, automake, desktop-file-utils, glib2-devel, gtk2-devel
BuildRequires: make
Requires: cfdg

%description
A front end to cfdg

%prep
%setup -qn cfdg-fe

%patch -P 0 -p0
%patch -P 1 -p0

%build
aclocal
autoconf
automake --add-missing
./configure --libdir=%{_libdir}
make CFLAGS="$RPM_OPT_FLAGS" LIBS="-lm"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 src/cfdg-fe %{buildroot}%{_bindir}/cfdg-fe
mkdir -p %{buildroot}%{_datadir}/cfdg-fe/
install -m 644 pixmaps/* %{buildroot}%{_datadir}/cfdg-fe/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 pixmaps/icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/cfdg-fe-icon.png

%files
%{_bindir}/cfdg-fe
%doc AUTHORS INSTALL COPYING README
%{_datadir}/icons/hicolor/32x32/apps/cfdg-fe-icon.png
%{_datadir}/applications/cfdg-fe.desktop
%{_datadir}/cfdg-fe
%{_datadir}/cfdg-fe/icon.png
%{_datadir}/cfdg-fe/logo.png

%changelog
%autochangelog
