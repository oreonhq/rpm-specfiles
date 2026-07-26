%global source0_hash b46cf5059578d277a14bfc901bb3d5666d013bf73c035331ac0222fdac358228

Name:           python-lunr
Version:        0.8.0
Release:        6%{?dist}
Summary:        A Python implementation of Lunr.js

License:        MIT
URL:            https://github.com/yeraydiazdiaz/lunr.py
BuildArch:      noarch
Source0:        %{pypi_source lunr}

BuildRequires:  python3-devel
# For tests
BuildRequires:  python3dist(pytest)

%description
This Python version of Lunr.js aims to bring the simple and powerful full text
search capabilities into Python guaranteeing results as close as the original
implementation as possible.

%package -n python3-lunr
Summary:        %{summary}

%description -n python3-lunr
This Python version of Lunr.js aims to bring the simple and powerful full text
search capabilities into Python guaranteeing results as close as the original
implementation as possible.

%pyproject_extras_subpkg -n python3-lunr languages

%generate_buildrequires
%pyproject_buildrequires -r -x languages

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n lunr-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lunr

%check
# test_reduces_words_to_their_stem requires missing tests/fixtures/stemming_vocab.json
# test_lunr_function_registers_nltk_stemmers_in_pipeline requires network
# test_lunr_registers_lun_stemmers_in_pipeline_if_language_is_en requires network
# test_search_stems_search_terms requires network
# test_search_stems_search_terms_for_both_languages requires network
%pytest -k "not test_reduces_words_to_their_stem and \
            not test_lunr_function_registers_nltk_stemmers_in_pipeline and \
            not test_lunr_registers_lun_stemmers_in_pipeline_if_language_is_en and \
            not test_search_stems_search_terms and \
            not test_search_stems_search_terms_for_both_languages and \
            not acceptance"

%files -n python3-lunr -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
