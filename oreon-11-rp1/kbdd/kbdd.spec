%global source0_hash 17b3ee6054e86f9d54e70023582061f287a14a96bd8841a99b61921f3a3b165a

Name:           kbdd
Version:        0.7.1
Release:        20%{?dist}
Summary:        Per window keyboard layout

# Upstream license ticket https://github.com/qnikst/kbdd/issues/48
License:        GPLv3+
URL:            https://github.com/qnikst/kbdd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires: make

Requires:       dbus

%description
Simple daemon and library to make per window layout using XKB
(X KeyBoard Extension).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README README.rst
%{_bindir}/%{name}
%{_datadir}/dbus-1/interfaces/%{name}-service-interface.xml
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
