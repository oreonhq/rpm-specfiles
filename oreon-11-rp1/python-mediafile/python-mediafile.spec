%global source0_hash d75d805a06ed56150dbcea76505e700f9809abd9e98f98117ae46f5df2ccf1d7

%global shortname mediafile
Name:           python-mediafile
Version:        0.12.0
Release:        12%{dist}
Summary:        Elegant audio file tagging in Python

License:        MIT
URL:            https://github.com/beetbox/mediafile
Source0:        %{pypi_source mediafile}
Patch0:         0001-Set-new-ORIGINALDATE-tag-for-m4a-files-in-addition-t.patch
Patch1:         0002-Version-bump-changelog-for-71.patch
Patch2:         0003-remove-usage-of-six-__future__.patch
Patch3:         0004-Changelog-for-72.patch
Patch4:         0005-Bump-minimum-Python-versions.patch
# From PR 73 but without the binary change
Patch5:         49da9728a69ae8a63af8a4630fccc55c10e66392-nobinary.patch

BuildArch:     noarch
BuildRequires:  python3-devel

%global _description %{expand:
MediaFile is a simple interface to the metadata tags for many audio file
formats. It wraps Mutagen, a high-quality library for low-level tag
manipulation, with a high-level, format-independent interface for a common set
of tags.}

%description %{_description}

%package -n python3-%{shortname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{shortname}}

Requires:       python3 >= 3.6
Requires:       python3-filetype >= 1.2.0
Requires:       python-mutagen

%description -n python3-%{shortname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{shortname}-%{version} -p1
rm test/rsrc/only-magic-bytes.jpg

%generate_buildrequires
%pyproject_buildrequires -r -t -e %{toxenv}-test

%build
%pyproject_wheel

%check
%tox -e %{toxenv}-test

%install
%pyproject_install
%pyproject_save_files '*%{shortname}*'

%files -n python3-%{shortname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
