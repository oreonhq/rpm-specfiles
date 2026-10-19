%global source0_hash e51d9a9a30c7b5faf6d6a9c120a2c5f294ea5ba028d536af926fcf1c5c19c9d4
%global commit 7303ada0a83b70863b1805452288919e8efdc235
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           pyhoca-cli
Version:        0.6.1.3
Release:        1%{?dist}
Summary:        Command line X2Go client written in Python
License:        AGPL-3.0-or-later
URL:            http://www.x2go.org/
Source0:        http://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-setproctitle
Requires:       python%{python3_pkgversion}-x2go
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyhoca-cli = %{version}-%{release}
# /oreon:deps
%description
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - LDAP support
   - client side mass storage mounting support
   - client side printing support
   - audio support
   - authentication by smartcard and USB stick

PyHoca-CLI provides a simple and flexible command line client
written in Python that allows you to control X2Go client sessions
on desktops and thin clients.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_shebang_fix %{name}
%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}/%{_bindir}/
cp -p %{name} %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/
cp -rp man/* %{buildroot}/%{_mandir}/
%oreon_autofiles main

%files

%changelog

%autochangelog
