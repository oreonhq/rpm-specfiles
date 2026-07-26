%global source0_hash 1291a47e9ff1cb9f27d3d98d5a6d8a71293cdc806a4309906312f597660098ea

Name:           porcupine
Version:        0.1.0
Release:        28%{?dist}
Summary:        Web browser to copy URL to clipboard

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/micahflee/porcupine
Source0:        https://github.com/micahflee/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-qt5
BuildRequires:  desktop-file-utils
Requires:       python3-qt5

%description
Setting porcupine as a default browser will help you to click on any URL and
get it copied into your clipboard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Fix FTBFS with setuptools >= 61.0.0
# Upstream issue: https://github.com/micahflee/porcupine/issues/15
sed -i "21i packages=[]," setup.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications \
share/porcupine.desktop

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{python3_sitelib}/%{name}*

%changelog
%autochangelog
