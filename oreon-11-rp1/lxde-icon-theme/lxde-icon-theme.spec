%global source0_hash 5b71da247ba25ddcd991a3a184ca5ac92f40b7676766e1e59437067a20f7ecf7

Name:           lxde-icon-theme
Version:        0.5.2
Release:        3%{?dist}
Summary:        Default icon theme for LXDE

# SPDX confirmed
License:        LGPL-3.0-or-later
URL:            http://lxde.org/
Source0:        https://github.com/lxde/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Provides:       nuoveXT2-icon-theme = 2.2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

%description
nuoveXT2 is a very complete set of icons for several operating systems. It is 
also the default icon-theme of LXDE, the Lightweight X11 Desktop Environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sh autogen.sh

%build
%configure
%make_build

%install
%make_install
touch $RPM_BUILD_ROOT%{_datadir}/icons/nuoveXT2/icon-theme.cache

%files
%doc AUTHORS
%license COPYING
%dir %{_datadir}/icons/nuoveXT2/
%{_datadir}/icons/nuoveXT2/*/*
%{_datadir}/icons/nuoveXT2/index.theme
%ghost %{_datadir}/icons/nuoveXT2/icon-theme.cache

%changelog
%autochangelog
