%global source0_hash b1e1f59e4fbd8bf99367a5d761caf7cca276c1f63f46cd021e1d6e7177c14051
%global owner gbcox
%global commit a63b06415cfa9a7c258fa3b64f8afb25944d1329
%global shortcommit %(c=%{commit}; echo ${c:0:12})
Name:     ykocli
Version:  1.4.0
Release:        1%{?dist}
Summary:        Front-end script for ykman to obtain TOTP tokens
License:  GPL-3.0-or-later
URL:      https://bitbucket.org/%{owner}/%{name}
Source0:        https://bitbucket.org/%{owner}/%{name}/get/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:  %{name}.rpmlintrc
BuildArch:      noarch
Requires:       figlet
Requires:       copyq
Requires:       yubikey-manager
Requires:       zbar
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
ykocli is a front-end command line utility (actually, a bash script)
that places ykman obtained TOTP tokens into the CopyQ clipboard.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{owner}-%{name}-%{shortcommit}

%build

%install
%make_install prefix=%{_prefix} sysconfdir=%{_sysconfdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
