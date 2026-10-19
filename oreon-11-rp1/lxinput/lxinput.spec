%global source0_hash 2f15c2a17f970afb152cbd024503da26c1e15135e76e9f516e0ca97e909d6c37
Name:           lxinput
Version:        0.3.6
Release:        1%{?dist}
Summary:        Keyboard and mouse settings dialog for LXDE
License:        GPL-2.0-or-later
URL:            http://lxde.org/
Source0:        https://github.com/lxde/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       lxsession >= 0.4.0
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-2.0)
# /oreon:deps
%description
LXInput is a keyboard and mouse configuration utility for LXDE, the 
Lightweight X11 Desktop Environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

sh autogen.sh
%configure \
	--enable-man \
	--disable-silent-rules \
	%{nil}
%make_build
%install
rm -rf %{buildroot}
%make_install
desktop-file-install \
  --delete-original \
  --add-category=X-LXDE \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
