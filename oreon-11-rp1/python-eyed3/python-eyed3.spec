%global source0_hash 8c0052e8d9285169da24c4fda86a0a5d699f4dc0d001210142602ceb1c28b8ad

%global srcname eyed3

Name:           python-%{srcname}
Version:        0.9.9
Release:        1%{?dist}
Summary:        Python audio data toolkit (ID3 and MP3)
License:        GPL-3.0-or-later
URL:            https://github.com/nicfit/eyeD3
Source0:        https://github.com/nicfit/eyeD3/releases/download/v%{version}/eyeD3-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-deprecation
BuildRequires:  python3-filetype
BuildRequires:  python3-setuptools
# Test dependencies.
BuildRequires:  python3-factory-boy
BuildRequires:  python3-pytest
BuildRequires:  python3-six

%global _description\
A Python module and program for processing ID3 tags. Information about\
mp3 files(i.e bit rate, sample frequency, play time, etc.) is also\
provided. The formats supported are ID3 v1.0/v1.1 and v2.3/v2.4.

%description %_description

%package -n python3-%{srcname}
Summary: %summary
Requires:       python3-six
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n eyeD3-%{version}

%build
%py3_build

%install
%py3_install

%check
# Ignore tests which require:
# - test data (test_classic_plugin.py, test_core.py, id3/test_frames.py,
# id3_test_rva.py, test_issues.py)
py.test-%{python3_version} --ignore=tests/{test_classic_plugin.py,test_core.py,id3/test_frames.py,test_jsonyaml_plugin.py,id3/test_rva.py,test_issues.py}

%files -n python3-%{srcname}
%doc AUTHORS.rst HISTORY.rst README.rst examples/
%license LICENSE
%{_bindir}/eyeD3
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/eyed3-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
