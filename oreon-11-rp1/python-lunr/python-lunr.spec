%global source0_hash b46cf5059578d277a14bfc901bb3d5666d013bf73c035331ac0222fdac358228
Name:           python-lunr
Version:        0.8.0
Release:        1%{?dist}
Summary:        A Python implementation of Lunr.js
License:        MIT
URL:            https://github.com/yeraydiazdiaz/lunr.py
BuildArch:      noarch
Source0:        https://files.pythonhosted.org/packages/source/l/lunr/lunr-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-fancy-pypi-readme) >= 22.8.0
Requires:       python3-lunr = %{version}-%{release}
# /oreon:deps
%package -n       python3-lunr+languages
Summary:        Metapackage for python3-lunr languages extras
Requires:       python3-lunr = %{version}-%{release}
Provides:       python3dist(lunr[languages]) = %{version}-%{release}

%description -n python3-lunr+languages
Metapackage for python3-lunr languages extras.

%package -n       python3-lunr+tests
Summary:        Metapackage for python3-lunr tests extras
Requires:       python3-lunr = %{version}-%{release}
Provides:       python3dist(lunr[tests]) = %{version}-%{release}

%description -n python3-lunr+tests
Metapackage for python3-lunr tests extras.

%package -n       python3-lunr+docs
Summary:        Metapackage for python3-lunr docs extras
Requires:       python3-lunr = %{version}-%{release}
Provides:       python3dist(lunr[docs]) = %{version}-%{release}

%description -n python3-lunr+docs
Metapackage for python3-lunr docs extras.

%package -n       python3-lunr+local
Summary:        Metapackage for python3-lunr local extras
Requires:       python3-lunr = %{version}-%{release}
Provides:       python3dist(lunr[local]) = %{version}-%{release}

%description -n python3-lunr+local
Metapackage for python3-lunr local extras.

%package -n       python3-lunr+dev
Summary:        Metapackage for python3-lunr dev extras
Requires:       python3-lunr = %{version}-%{release}
Provides:       python3dist(lunr[dev]) = %{version}-%{release}

%description -n python3-lunr+dev
Metapackage for python3-lunr dev extras.

%description
This Python version of Lunr.js aims to bring the simple and powerful full text
search capabilities into Python guaranteeing results as close as the original
implementation as possible.

%package -n python3-lunr
Summary:        A Python implementation of Lunr.js
%description -n python3-lunr
This Python version of Lunr.js aims to bring the simple and powerful full text
search capabilities into Python guaranteeing results as close as the original
implementation as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir lunr-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lunr usr/lib/python3*/site-packages/lunr* usr/lib64/python3*/site-packages/lunr* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lunr* usr/lib64/python3*/site-packages/lunr* usr/bin/*

%check

%pytest -k "not test_reduces_words_to_their_stem and \
            not test_lunr_function_registers_nltk_stemmers_in_pipeline and \
            not test_lunr_registers_lun_stemmers_in_pipeline_if_language_is_en and \
            not test_search_stems_search_terms and \
            not test_search_stems_search_terms_for_both_languages and \
            not acceptance"
%files
%files -n python3-lunr -f %{oreon_filedir}/python3-lunr.list

%changelog

%autochangelog
