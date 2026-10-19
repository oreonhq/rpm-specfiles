%global source0_hash d12be7fb9170d650ae78197983fac05af21ddbf47f7b1a2a14de9aa832ed602c
Name:       ccgo
Version:    0.3.6.5
Release:        29%{?dist}
Summary:        An IGS (Internet Go Server) client written in C++
License:    GPL-3.0-or-later
SourceLicense:  GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND FSFUL AND FSFULLR AND FSFULLRWD AND X11 AND LicenseRef-Fedora-Public-Domain
URL:        http://ccdw.org/~cjj/prog/%{name}/
Source0:        http://ccdw.org/~cjj/prog/%{name}/src/%{name}-%{version}.tar.gz
Source1:    %{name}.appdata.xml
Patch0:     ccgo-0.3.6.5-Port-to-libsigc-2.6.0.patch
Patch1:     ccgo-0.3.6.5-Adapt-to-glibc-assert-change.patch
Requires:       gnugo
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gconfmm-2.6)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  sed
# /oreon:deps
%description
ccGo allows you to play go with GNU Go on your computer or with other players
on an Internet Go Server (IGS) on the Internet. It supports smart game format
(SGF) suitable for exchanging game records.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Make XDG desktop file compliant
sed -i -e '/^Encoding/d' -e '/^Categories/s/Application;//' \
    %{name}.desktop.in
# Update config.sub to support aarch64, bug #925132
# Remove bundled files
rm ABOUT-NLS aclocal.m4 configure compile config.guess config.sub depcomp gettext.h \
    go/Makefile.in igs/Makefile.in igs/parser/Makefile.in install-sh m4/* \
    Makefile.in missing po/Makefile.in.in
# gettextize breaks configure.ac. Rather symlink the header file.
ln -s /usr/share/gettext/gettext.h gettext.h
autoreconf -i -f

%build

%configure
%{make_build}
%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%install
%{make_install}
install -d %{buildroot}%{_datadir}/appdata
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
