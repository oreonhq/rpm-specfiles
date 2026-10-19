%global source0_hash ab5a243c52ed1fb479ca1ed01d837d61deb246960691695deecaae4ad65b60c4
Name: gxkb
Version: 0.9.6
Release:        1%{?dist}
Summary:        X11 keyboard indicator and switcher
License: GPL-2.0-or-later
URL: https://github.com/zen-tools/gxkb
Source0:        https://github.com/zen-tools/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxklavier)
# /oreon:deps
%description
gxkb is a tiny indicator applet which allows to quickly switch between
different keyboard layouts in X. A flag corresponding to the country of the
active layout is shown in the indicator area. The applet is written in C and
uses GTK+ library and therefore does not depend on any GNOME components.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure \
    --enable-appindicator=no
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_licensedir}/%{name}/
mv %{buildroot}%{_docdir}/%{name}/COPYING %{buildroot}%{_licensedir}/%{name}/
cp -p README.md %{buildroot}%{_docdir}/%{name}/
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
