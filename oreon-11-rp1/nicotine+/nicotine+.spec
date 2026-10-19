%global source0_hash 0021c20f6ee8a151a4eda78c38a0735cddbcedebf5ef834f4d0769384e76556b
%global altname nicotine
%global appdata_id org.nicotine_plus.Nicotine
Name:           nicotine+
Version:        3.3.11
Release:        1%{?dist}
Summary:        A graphical client for Soulseek
License:        GPL-3.0-or-later AND MIT AND CC-BY-SA-4.0
URL:            https://nicotine-plus.github.io/nicotine-plus/
Source0:        https://github.com/nicotine-plus/nicotine-plus/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-3.3.10-tests.patch
Requires:       (gtk4 or gtk3)
Requires:       (gtk3 and gspell)
Requires:       (gtk4 and libadwaita)
Requires:       hicolor-icon-theme
Requires:       %{py3_dist pygobject}
Provides:       bundled(python3dist(tinytag))
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-nicotine+ = %{version}-%{release}
# /oreon:deps
%description
Nicotine+ is a graphical client for the Soulseek peer-to-peer file sharing
network. It is an attempt to keep Nicotine working with the latest libraries,
kill bugs, keep current with the Soulseek protocol, and add some new features
that users want and/or need.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n nicotine-plus-%{version} -p0

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%python3 -m unittest
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{appdata_id}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{appdata_id}.appdata.xml
%files

%changelog

%autochangelog
