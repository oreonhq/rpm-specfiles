%global source0_hash 8387e25e5fb0b4cbe701e5dc092d666d6510b833fd3e7e462e9170d36ec3c15f
Name:		telepathy-idle
Version:	0.2.2
Release:        8%{?dist}
Summary:        IRC connection manager for Telepathy
License:	LGPL-2.1-only AND LGPL-2.1-or-later
URL:		https://telepathy.freedesktop.org/
Source0:        https://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Requires:	dbus-common
Requires:	telepathy-filesystem
# oreon:deps
BuildRequires:  dbus-daemon
BuildRequires:  gcc
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  python3-dbus
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-service-identity
BuildRequires:  python3-twisted
# /oreon:deps
%description
A full-featured IRC connection manager for the Telepathy project.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# https://gitlab.freedesktop.org/telepathy/telepathy-idle/-/issues/45
sed -i -e "s|@TEST_PYTHON@|%{python3}|g" tests/twisted/run-test.sh.in

# fails in mock environment
for i in connect-close-ssl connect-reject-ssl connect-success-ssl disconnect-during-cert-verification;do
    sed -i "/$i/d" tests/twisted/Makefile.in
done

%build

%configure PYTHON="%{__python3}"
%make_build
%check

make check
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
