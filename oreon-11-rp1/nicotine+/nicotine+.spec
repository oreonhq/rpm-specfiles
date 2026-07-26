%global source0_hash 3917ebc562f2d6a6b26b3d815d7cbdf1d11c058d994b1f47794bbb850489b35e

%global altname nicotine
%global appdata_id org.nicotine_plus.Nicotine

Name:           nicotine+
Version:        3.3.10
Release:        6%{?dist}
Summary:        A graphical client for Soulseek

# - pynicotine/external/tinytag.py is MIT
# - IP2Location Country Database (pynicotine/external/data/ip_country_data.csv)
#   is CC-BY-SA-4.0 (see pynicotine/external/README.md)
License:        GPL-3.0-or-later AND MIT AND CC-BY-SA-4.0
URL:            https://nicotine-plus.github.io/nicotine-plus/
Source0:        https://github.com/nicotine-plus/nicotine-plus/archive/%{version}/%{name}-%{version}.tar.gz
# Disable metadata tests because they fail on Koji builders, while they pass
# locally with mock (builder architecture? SELinux issues?)
Patch0:         %{name}-3.3.10-tests.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
# Needed for tests
BuildRequires:  gobject-introspection
BuildRequires:  gtk4
# Runtime dependencies are not declared in setup.py but are actually required
# (see doc/DEPENDENCIES.md)
Requires:       (gtk4 or gtk3)
Requires:       (gtk3 and gspell)
Requires:       (gtk4 and libadwaita)
Requires:       hicolor-icon-theme
Requires:       %{py3_dist pygobject}
# pynicotine/external/tinytag.py is a bundled fork of
# https://pypi.org/project/tinytag/
Provides:       bundled(python3dist(tinytag))
BuildArch:      noarch

%description
Nicotine+ is a graphical client for the Soulseek peer-to-peer file sharing
network. It is an attempt to keep Nicotine working with the latest libraries,
kill bugs, keep current with the Soulseek protocol, and add some new features
that users want and/or need.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n nicotine-plus-%{version} -p0

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pynicotine

%check
%python3 -m unittest

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{appdata_id}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{appdata_id}.appdata.xml

%files -f %{pyproject_files}
%doc AUTHORS.md NEWS.md README.md
%license COPYING
%{_bindir}/%{altname}
%{_datadir}/applications/%{appdata_id}.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/%{appdata_id}.appdata.xml
%{_mandir}/man1/%{altname}.1.*

%changelog
%autochangelog
