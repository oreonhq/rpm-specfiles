%global source0_hash e08b402a4b8d19aa6c983c8cfc3328de5c5d2fdfaf96f55a2b67610e0297d599

Name:           python-sdkmanager
Version:        0.6.10
Release:        %autorelease
Summary:        Android SDK manager written in Python

License:        AGPL-3.0-or-later
URL:            https://gitlab.com/fdroid/sdkmanager
Source:         %{pypi_source sdkmanager}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A drop-in replacement for sdkmanager from the Android SDK
written in Python. It implements the exact API of the
sdkmanager command line.  It only deviates from that API
if it can be done while being 100 percent compatible.

The project also attempts to maintain the same terminal
output so it can be compatible with things that scrape
sdkmanager output.}

%description %_description

%package -n     python3-sdkmanager
Summary:        Android SDK manager written in Python

%description -n python3-sdkmanager %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sdkmanager-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
sed -i '/env python3/d' sdkmanager.py
chmod -x sdkmanager.py
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sdkmanager

%check
%pyproject_check_import
# Tests require internet access

%files -n python3-sdkmanager -f %{pyproject_files}
%{_bindir}/sdkmanager

%changelog
%autochangelog
