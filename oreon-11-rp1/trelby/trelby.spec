%global source0_hash 2f69f90057ca31746eeeddb5cffa944e29aa5e67905f141043f6e3a9ea6cbe3e
Name:           trelby
Version:        2.4.16.2
Release:        1%{?dist}
Summary:        The free, multiplatform, feature-rich screenwriting program
License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://github.com/trelby/trelby
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-trelby = %{version}-%{release}
# /oreon:deps
%description
Trelby is simple, fast and elegantly laid out to make
screenwriting simple. It is infinitely configurable.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

make
%pyproject_wheel
rm -rf doc/.gitignore
%install
%pyproject_install
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{python3_sitelib}/trelby/resources/icon256.png %{buildroot}%{_datadir}/pixmaps/trelby256.png
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications trelby/resources/trelby.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/trelby.desktop
mkdir -p %{buildroot}%{_mandir}/man1/
install -m644 trelby/trelby.1.gz %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

%pytest
%files

%changelog

%autochangelog
