%global source0_hash 669c04cbc83e64dc580c5c350d773efab7363c300c7934aec57cc35943f5b913

Name:           python-dragonmapper
Version:        0.3.0
Release:        %autorelease
Summary:        Identification and conversion functions for Chinese text processing

License:        MIT
URL:            https://github.com/tsroten/dragonmapper
Source:         %{url}/archive/v%{version}/dragonmapper-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Dragon Mapper is a Python library that provides identification and conversion
functions for Chinese text processing.

Features

- Convert between Chinese characters, Pinyin, Zhuyin, and the International
Phonetic Alphabet.
- Identify a string as Traditional or Simplified Chinese, Pinyin, Zhuyin, or the
International Phonetic Alphabet.}

%description %_description

%package -n     python3-dragonmapper
Summary:        %{summary}

%description -n python3-dragonmapper %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n dragonmapper-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dragonmapper

%check
%pyproject_check_import
%pytest

%files -n python3-dragonmapper -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
