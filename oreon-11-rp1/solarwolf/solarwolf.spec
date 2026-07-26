%global source0_hash 24f7379c8ab63745ecc813ecaf4c6841186aa11bdaca4a8ec2077b30c5caa600

Name: solarwolf
Version:  1.6.0
Release:  26%{?dist}.a4
Summary: A Python port of SolarFox

License: LGPL-2.0-or-later
URL: http://pygame.org/shredwheat/solarwolf
Source0: solarwolf-d19d830.tar.gz
Source1: solarwolf.desktop
Patch1: solarwolf-1.6.0a4-python3.patch
BuildArchitectures: noarch
BuildRequires: desktop-file-utils python3-devel python3-setuptools
Requires: hicolor-icon-theme python3-pygame

%description
The point of the game is to scramble through 60 levels
collecting space boxes. Each level gets is harder than
the previous. Obstacles like bullets, mines, and asteroids
cover your every move. Beat the Skip timer and grab the
powerups for your only chance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn solarwolf-d19d830

%patch -P1 -p0

%build
%python3 setup.py build

%install
%python3 setup.py install --skip-build --root %{buildroot} --prefix %{_prefix}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 dist/solarwolf.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps

%files
%{_bindir}/solarwolf
%{python3_sitelib}/solarwolf/
%{python3_sitelib}/solarwolf-*.egg-info/
%license lgpl.txt
%doc README.rst
%{_datadir}/applications/solarwolf.desktop
%{_datadir}/icons/hicolor/64x64/apps/solarwolf.png

%changelog
%autochangelog
