%global source0_hash 2f15c2a17f970afb152cbd024503da26c1e15135e76e9f516e0ca97e909d6c37

# Review: https://bugzilla.redhat.com/show_bug.cgi?id=498130

Name:           lxinput
Version:        0.3.6
Release:        3%{?dist}
Summary:        Keyboard and mouse settings dialog for LXDE

# SPDX confirmed
License:        GPL-2.0-or-later
URL:            http://lxde.org/
#VCS: git:git://lxde.git.sourceforge.net/gitroot/lxde/lxinput
Source0:        https://github.com/lxde/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-utils
BuildRequires:  docbook-style-xsl
Requires:       lxsession >= 0.4.0

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

%files -f %{name}.lang
#FIXME: add ChangeLog and NEWS if there is content
%doc AUTHORS
%doc README
%license COPYING

%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.ui

%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
