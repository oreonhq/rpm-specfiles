%global source0_hash faf19801c3742ed5a05a8ce388e0d8fe1a07f8d095c82201eb904f5d27ad571f

%global srcname inflect
Name:           python-%{srcname}
Version:        7.5.0
Release:        6%{?dist}
Summary:        Correctly generate plurals, singular nouns, ordinals and indefinite articles

License:        MIT
URL:            https://github.com/jazzband/inflect
Source0:        %pypi_source

Patch1:         0001-Remove-test-dependencies-on-linters.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The methods of the class 'engine' in module 'inflect.py' provide plural
inflections, singular noun inflections, "a"/"an" selection for English words,
and manipulation of numbers as words.

Plural forms of all nouns, most verbs, and some adjectives are provided. Where
appropriate, "classical" variants (for example: "brother" -> "brethren",
"dogma" -> "dogmata", etc.) are also provided.

Single forms of nouns are also provided. The gender of singular pronouns can be
chosen (for example "they" -> "it" or "she" or "he" or "they").

Pronunciation-based "a"/"an" selection is provided for all English words, and
most initialisms.

It is also possible to inflect numerals (1,2,3) to ordinals (1st, 2nd, 3rd) and
to English words ("one", "two", "three").}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%generate_buildrequires
# There is a tox env for generating html docs from pydoc comments, but it's broken; skip it
%pyproject_buildrequires -t

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -rf inflect.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l inflect

%check
%tox

%files -n python3-inflect -f %{pyproject_files}
%doc NEWS.rst README.rst SECURITY.md

%changelog
%autochangelog
