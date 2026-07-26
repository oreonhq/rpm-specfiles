%global source0_hash 41764d771043d0c06c23d75b1e3ca6b2b94279191483d03f10c5e034d6722ebf

Name:     i3blocks
Version:  1.5
Release:  14%{?dist}
Summary:  A feed generator for text based status bars
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:  GPL-3.0-or-later
URL:      https://github.com/vivien/%{name}
Source:   %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make

%description
A feed generator for text based status bars

i3blocks executes your command lines and generates a status line from
their output. Commands are scheduled at configured time intervals,
upon signal reception or on clicks.

The generated line is meant to be displayed by the i3 window manager
through its i3bar component, as an alternative to i3status.

i3blocks is meant to be highly flexible but intuitive. No library
package is required, just output what your status bar expects, from
your favorite programming language and your preferred format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
./autogen.sh
%configure
%make_build

%install
%make_install
# these are useless in a i3bar/swaybar:
rm -rf %{buildroot}/usr/share/bash-completion

%files
%license COPYING

%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
