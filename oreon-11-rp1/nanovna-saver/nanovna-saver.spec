%global source0_hash 932a9d54e6cdf3a7ee4fd9e5c75f8721b5a249b1de320feefb013de293717cd1

Name:		nanovna-saver
Version:	0.7.3
Release:	9%{?dist}
Summary:	Tool for reading, displaying and saving data from the NanoVNA
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/NanoVNA-Saver/%{name}

Source:		%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	coreutils
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	python3-pyserial
BuildRequires:	python3-numpy
BuildRequires:	python3-scipy
BuildRequires:	python3-qt5
BuildRequires:	python3-Cython
BuildRequires:	pyside6-tools
BuildRequires:	desktop-file-utils
# for fixing the version
BuildRequires:	sed
Requires:	hicolor-icon-theme
# https://github.com/NanoVNA-Saver/nanovna-saver/issues/815
Patch:		nanovna-saver-0.7.3-python3.patch
# https://github.com/NanoVNA-Saver/nanovna-saver/issues/814
Patch:		nanovna-saver-0.7.3-drop-setuptools-scm-version.patch
# https://github.com/NanoVNA-Saver/nanovna-saver/issues/813
Patch:		nanovna-saver-0.7.3-relax-deps.patch

%description
A multiplatform tool to save Touchstone files from the NanoVNA, sweep
frequency spans in segments to gain more than 101 data points, and
generally display and analyze the resulting data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# fix version, https://github.com/NanoVNA-Saver/nanovna-saver/issues/814
sed -i '/^\s*dynamic\s*=\s*\['"'"'version'"'"'\].*/ s/^\s*dynamic\s*=\s*\['"'"'version'"'"'\].*/version = "%{version}"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -p

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files NanoVNASaver

# Drop tests
rm -rf %{buildroot}%{python3_sitelib}/test

# manual page
install -Dpm 0644 docs/man/NanoVNASaver.1 %{buildroot}%{_mandir}/man1/NanoVNASaver.1

# desktop file
desktop-file-install NanoVNASaver.desktop

# icon
install -Dpm 0644 NanoVNASaver_48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/NanoVNASaver_48x48.png

# remove build artifacts
rm -rf %{buildroot}%{python3_sitelib}/tools

# https://github.com/NanoVNA-Saver/nanovna-saver/issues/443
#%%check
#%%{tox}

%files -f %{pyproject_files}
%license licenses/LICENSE.txt
%doc README.rst docs/CODE_OF_CONDUCT.md docs/CONTRIBUTING.md licenses/AUTHORS.rst
%{_bindir}/NanoVNASaver
%{_bindir}/NanoVNASaver-gui
%{_mandir}/man1/NanoVNASaver.1*
%{_datadir}/icons/hicolor/48x48/apps/NanoVNASaver_48x48.png
%{_datadir}/applications/NanoVNASaver.desktop

%changelog
%autochangelog
