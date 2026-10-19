%global source0_hash 7d4ee044f2f5cd03902aee8a759093881ff72a614f0f9664f8fbbd0e4f70d95a
%global module manatools
Name:           python-%{module}
Version:        0.99.3
Release:        1%{?dist}
Summary:        A Python framework to build ManaTools applications
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/manatools/python-manatools
Source0:        https://github.com/manatools/python-manatools/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-yui
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
Python ManaTools aim is to help in writing tools based on libYui
(SUSE widget abstraction library), to be collected under the
ManaTools banner and hopefully with the same look and feel.

Every output module supports the Qt, GTK, and ncurses interfaces.

%package -n python3-%{module}
Summary:        A Python framework to build ManaTools applications
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-yui
%{?python_provide:%python_provide python3-%{module}}
Requires:       python3-yui
Recommends:     (libyui-mga-qt if qt5-qtbase-gui)
Recommends:     (libyui-mga-gtk if gtk3)
%description -n python3-%{module}
Python ManaTools aim is to help in writing tools based on libYui
(SUSE widget abstraction library), to be collected under the
ManaTools banner and hopefully with the same look and feel.

Every output module supports the Qt, GTK, and ncurses interfaces.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i 's|0.0.1|%{version}|' manatools/version.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-manatools -f %{oreon_filedir}/python3-manatools.list

%changelog

%autochangelog
