%global source0_hash 2a331f3ae2c7fefe039231371a0cc9765c594527fc3ef09cf75950c69770b729
Name:           porcupine
Version:        0.2.2
Release:        1%{?dist}
Summary:        Web browser to copy URL to clipboard
License:        GPL-3.0-only
URL:            https://github.com/micahflee/porcupine
Source0:        https://github.com/micahflee/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-qt5
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-qt5
BuildRequires:  python3-setuptools
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
