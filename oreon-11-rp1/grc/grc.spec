%global source0_hash a7b10d4316b59ca50f6b749f1d080cea0b41cb3b7258099c3eb195659d1f144f

Name:           grc
Version:        1.13
Release:        %autorelease
Summary:        Generic Colorizer

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://korpus.juls.savba.sk/~garabik/software/grc.html
Source0:        https://github.com/garabik/grc/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  sed

%description
Generic Colorizer is yet another colorizer for beautifying your log files or
output of commands.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# replace symlinks with plain files
rm COPYING CHANGES
cp debian/copyright COPYING
cp debian/changelog CHANGES
sed -i -e '/^#!\//, 1d' grc.fish grc.zsh
sed -i.bak -e 's/env python/python/' grc grcat
sed -i -e 's/cp -fv /cp -fvp /' install.sh

%build

%install
./install.sh "$RPM_BUILD_ROOT%{_prefix}" "$RPM_BUILD_ROOT"

%files
%doc CREDITS README.markdown TODO CHANGES Regexp.txt
%license COPYING
%{_bindir}/grc
%{_bindir}/grcat
%{_datadir}/grc/
%config(noreplace) %{_sysconfdir}/grc.conf
%config(noreplace) %{_sysconfdir}/grc.fish
%config(noreplace) %{_sysconfdir}/grc.zsh
%config(noreplace) %{_sysconfdir}/profile.d/grc.sh
%{_mandir}/man1/grc.1*
%{_mandir}/man1/grcat.1*

%changelog
%autochangelog
