%global source0_hash bf2fffcc5c50cbc52bf79005fffff1e69ca9ef081b1ff3f46520043243b61bd2

Name: beesu
Version: 2.7
# Don't ever decrease this version (unless beesu update) or the subpackages will go backwards.
# It is easier to do this than to track a separate release field.
Release: %autorelease
Summary: Graphical wrapper for su
URL: http://www.honeybeenet.altervista.org
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://honeybeenet.altervista.org/beesu/files/beesu-sources/%{name}-%{version}.tar.bz2

Patch1:        beesu_directory_fix_f42.patch

BuildRequires: gcc-c++
BuildRequires: make

Requires: pam
Requires: usermode
Requires: usermode-gtk

Obsoletes: nautilus-beesu-manager
Obsoletes: caja-beesu-manager
Obsoletes: nemo-beesu-manager
Obsoletes: gedit-beesu-plugin
Obsoletes: pluma-beesu-plugin

%description
Beesu is a wrapper around su and works with consolehelper under
Fedora to let you have a graphic interface like gksu.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build CFLAGS="%{optflags} -fno-delete-null-pointer-checks"

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
mv %{buildroot}%{_sysconfdir}/profile.d/beesu-bash-completion.sh \
 %{buildroot}%{_sysconfdir}/bash_completion.d/

%files
%doc README
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}
%{_sysconfdir}/bash_completion.d/%{name}-bash-completion.sh
%{_libexecdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
