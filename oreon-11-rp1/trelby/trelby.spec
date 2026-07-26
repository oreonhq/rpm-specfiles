%global source0_hash 2f69f90057ca31746eeeddb5cffa944e29aa5e67905f141043f6e3a9ea6cbe3e

Name:           trelby
Version:        2.4.16.2
Release:        2%{?dist}
Summary:        The free, multiplatform, feature-rich screenwriting program

License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://github.com/trelby/trelby
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  make
BuildRequires:  python3dist(pytest)
Requires:       hicolor-icon-theme

%description
Trelby is simple, fast and elegantly laid out to make
screenwriting simple. It is infinitely configurable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%generate_buildrequires
%pyproject_buildrequires

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

%check
%pytest

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/applications/trelby.desktop
%{python3_sitelib}/trelby*
%{_mandir}/man1/trelby.1.gz
%{_datadir}/pixmaps/trelby256.png
%exclude %{python3_sitelib}/tests/

%changelog
%autochangelog
