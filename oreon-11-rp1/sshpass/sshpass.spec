%global source0_hash ad1106c203cbb56185ca3bad8c6ccafca3b4064696194da879f81c8d7bdfeeda

Summary:    Non-interactive SSH authentication utility
Name:       sshpass
Version:    1.10
Release:    1%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:    GPL-2.0-only
Url:        http://sshpass.sourceforge.net/
Source0:        https://downloads.sourceforge.net/sshpass/sshpass-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%description
Tool for non-interactively performing password authentication with so called
"interactive keyboard password authentication" of SSH. Most users should use
more secure public key authentication of SSH instead.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/sshpass
%{_datadir}/man/man1/sshpass.1.gz
%doc AUTHORS COPYING ChangeLog NEWS

%changelog
%autochangelog
