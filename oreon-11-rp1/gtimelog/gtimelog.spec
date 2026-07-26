%global source0_hash 8eccde32fb11f2dd3a7e28d14693dea5052b9922aacef14235232e109be236ab

Name:           gtimelog
Version:        0.12.0
Release:        9%{?dist}
Summary:        Unobtrusively keep track of your time

License:        GPL-2.0-or-later
URL:            https://gtimelog.org/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-freezegun
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-install
BuildRequires:  /usr/bin/msgfmt
BuildRequires:  /usr/bin/rst2man
Requires:       gtk3
Requires:       libsecret
Requires:       libsoup3
Requires:       python3-gobject
Recommends:     yelp

%description
GTimeLog is a small GTK+ app for keeping track of your time. It's main goal is
to be as unobtrusive as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{__python3} setup.py build
# Generates the man pages.
make all

%install
%{__python3} setup.py install --skip-build --root %{buildroot}
desktop-file-install %{name}.desktop
# Needed for the desktop file.
install -d %{buildroot}/%{_datadir}/pixmaps
mv %{buildroot}%{python3_sitelib}/%{name}/*.png %{buildroot}/%{_datadir}/pixmaps
install -Dpm 644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
install -Dpm 644 %{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
install -Dpm 644 src/gtimelog/data/org.gtimelog.gschema.xml %{buildroot}/%{_datadir}/glib-2.0/schemas/org.gtimelog.gschema.xml

%check
# Runs tests on the source tree.
%{__python3} ./runtests
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc CHANGES.rst CONTRIBUTING.rst src/gtimelog/CONTRIBUTORS.rst README.rst TODO.rst
%license COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gtimelog.gschema.xml
%{_datadir}/pixmaps/%{name}*.png
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{name}*

%changelog
%autochangelog
