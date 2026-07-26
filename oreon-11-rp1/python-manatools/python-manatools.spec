%global source0_hash 4afbf616f95141d28a1a7094ecbc7ea41362bd5765500759622b13b2180b8211

%global module manatools

Name:           python-%{module}
Version:        0.0.4
Release:        17%{?dist}

Summary:        A Python framework to build ManaTools applications
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/manatools/python-manatools
Source0:        https://github.com/manatools/python-manatools/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Python ManaTools aim is to help in writing tools based on libYui
(SUSE widget abstraction library), to be collected under the
ManaTools banner and hopefully with the same look and feel.

Every output module supports the Qt, GTK, and ncurses interfaces.

%package -n python3-%{module}
Summary:        %{summary}
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

%files -n python3-%{module}
%doc README.md NEWS
%license LICENSE
%{python3_sitelib}/%{module}/
%{python3_sitelib}/python_manatools-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
