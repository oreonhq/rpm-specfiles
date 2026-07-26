%global source0_hash bc5b1869a85f82dd26c62977012615c16ddfe5330685cc938905f481534c9e09

Name:           python-jaconv
Version:        0.3.4
Release:        8%{?dist}
Summary:        Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, Zenkaku and more

License:        MIT-0
URL:            https://github.com/ikegami-yukino/jaconv
Source:         %{url}/archive/v%{version}/jaconv-%{version}.tar.gz
# switch from nose to pytest for tests
Patch0:         https://patch-diff.githubusercontent.com/raw/ikegami-yukino/jaconv/pull/36.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
a Python Natural Language Processing (NLP) library to transliterate hiragana,
katakana and kanji (Japanese text) into rōmaji (Latin/Roman alphabet).
It can handle characters in NFC form.}

%description %_description

%package -n python3-jaconv
Summary:        %{summary}

%description -n python3-jaconv %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jaconv-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

rm -f %{buildroot}/usr/CHANGES.rst %{buildroot}/usr/README.rst
%pyproject_save_files -l jaconv -l

%check
%pytest

%files -n python3-jaconv -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
%autochangelog
