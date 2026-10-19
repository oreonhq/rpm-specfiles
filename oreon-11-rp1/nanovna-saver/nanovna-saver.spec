%global source0_hash 932a9d54e6cdf3a7ee4fd9e5c75f8721b5a249b1de320feefb013de293717cd1
Name:		nanovna-saver
Version:	0.7.3
Release:        1%{?dist}
Summary:        Tool for reading, displaying and saving data from the NanoVNA
License:	GPL-3.0-only
URL:		https://github.com/NanoVNA-Saver/%{name}
Source0:        https://github.com/NanoVNA-Saver/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	hicolor-icon-theme
Patch:		nanovna-saver-0.7.3-python3.patch
Patch:		nanovna-saver-0.7.3-drop-setuptools-scm-version.patch
Patch:		nanovna-saver-0.7.3-relax-deps.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-nanovna-saver = %{version}-%{release}
# /oreon:deps
%description
A multiplatform tool to save Touchstone files from the NanoVNA, sweep
frequency spans in segments to gain more than 101 data points, and
generally display and analyze the resulting data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# fix version, https://github.com/NanoVNA-Saver/nanovna-saver/issues/814
sed -i '/^\s*dynamic\s*=\s*\['"'"'version'"'"'\].*/ s/^\s*dynamic\s*=\s*\['"'"'version'"'"'\].*/version = "%{version}"/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
rm -rf %{buildroot}%{python3_sitelib}/test
install -Dpm 0644 docs/man/NanoVNASaver.1 %{buildroot}%{_mandir}/man1/NanoVNASaver.1
desktop-file-install NanoVNASaver.desktop
install -Dpm 0644 NanoVNASaver_48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/NanoVNASaver_48x48.png
rm -rf %{buildroot}%{python3_sitelib}/tools
%oreon_autofiles main

%files

%changelog

%autochangelog
