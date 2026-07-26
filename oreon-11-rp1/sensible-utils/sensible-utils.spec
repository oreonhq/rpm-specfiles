%global source0_hash 46adb7a12d32a9323b29711bc6470628fcc0f94f1748fe5bae4729df50531f68

Name:           sensible-utils
Version:        0.0.26
Release:        2%{?dist}
Summary:        Utilities for sensible alternative selection

BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            https://packages.debian.org/unstable/admin/%{name}
Source0:        http://ftp.de.debian.org/debian/pool/main/s/%{name}/%{name}_%{version}.tar.xz

BuildRequires:  automake autoconf
BuildRequires:  make
BuildRequires:  po4a

# See Patch0
Requires:       /usr/bin/gettext
Requires:       /usr/bin/realpath

%description
This package provides a number of small utilities which are used by programs to
sensibly select and spawn an appropriate browser, editor, or pager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
# Needed for Patch0
autoreconf -ifv

%configure
%make_build

%install
%make_install

%files
%license debian/copyright
%doc debian/changelog
%{_bindir}/sensible-*
%{_bindir}/select-editor
%{_mandir}/man1/*.1*
%{_mandir}/*/man1/*.1*

%changelog
%autochangelog
