%global source0_hash ad1106c203cbb56185ca3bad8c6ccafca3b4064696194da879f81c8d7bdfeeda
Summary:        Non-interactive SSH authentication utility
Name:       sshpass
Version:    1.10
Release:        1%{?dist}
License:    GPL-2.0-only
Url:        http://sshpass.sourceforge.net/
Source0:        https://downloads.sourceforge.net/sshpass/sshpass-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
