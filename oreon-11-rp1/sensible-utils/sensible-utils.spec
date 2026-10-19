%global source0_hash 46adb7a12d32a9323b29711bc6470628fcc0f94f1748fe5bae4729df50531f68
Name:           sensible-utils
Version:        0.0.26
Release:        2%{?dist}
Summary:        Utilities for sensible alternative selection
BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            https://packages.debian.org/unstable/admin/%{name}
Source0:        http://ftp.de.debian.org/debian/pool/main/s/%{name}/%{name}_%{version}.tar.xz
Requires:       /usr/bin/gettext
Requires:       /usr/bin/realpath
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  po4a
# /oreon:deps
%description
This package provides a number of small utilities which are used by programs to
sensibly select and spawn an appropriate browser, editor, or pager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

autoreconf -ifv
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
