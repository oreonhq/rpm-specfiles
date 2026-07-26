%global source0_hash 806c122bd0a8a1a14becfa8e0189b16e2cd529d63b53d606c3f8b53e914d0c01

# Not packaged: python-hijri-converter (needed by calendars extra)
%bcond_with calendars
# Not packaged: python-fasttext (needed by fasttext extra)
%bcond_with fasttext
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
# Skip PDF generation on EL9 due to missing /usr/bin/xindy dependency.
%if 0%{?el9} || 0%{?centos} >= 9 || 0%{?flatpak}
%bcond_with doc_pdf
%else
%bcond_without doc_pdf
%endif
# Tests use parameterized extensively, orphaned in Fedora
%bcond_with tests

Name:           python-dateparser
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python parser for human readable dates

License:        BSD-3-Clause
URL:            https://github.com/scrapinghub/dateparser
Source0:        %{url}/archive/v%{version}/dateparser-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on --help
Source1:        dateparser-download.1

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
Key Features

  • Support for almost every existing date format: absolute dates, relative
    dates ("two weeks ago" or "tomorrow"), timestamps, etc.
  • Support for more than 200 language locales.
  • Language autodetection
  • Customizable behavior through settings.
  • Support for non-Gregorian calendar systems.
  • Support for dates with timezones abbreviations or UTC offsets
    ("August 14, 2015 EST", "21 July 2013 10:15 pm +0500"…)
  • Search dates in longer texts.}

%description %{common_description}

%package -n python3-dateparser
Summary:        %{summary}

%py_provides python3-dateparser-cli
%py_provides python3-dateparser-data

%description -n python3-dateparser %{common_description}

%pyproject_extras_subpkg -n python3-dateparser %{?with_calendars:calendars} %{?with_fasttext:fasttext} langdetect

%package -n python3-dateparser-scripts
Summary:        %{summary}

Requires:       python3-dateparser = %{version}-%{release}
# From dateparser_scripts/requirements.txt; not included in the
# install_requires. It is questionable whether these scripts need to be
# installed at all. See:
# https://github.com/scrapinghub/dateparser/issues/705#issuecomment-1464503426.
Requires:       %{py3_dist gitpython}
Requires:       %{py3_dist parsel}
Requires:       %{py3_dist requests}
Requires:       %{py3_dist ruamel.yaml}

%description -n python3-dateparser-scripts %{common_description}

This package contains scripts used in developing the dateparser package.

%package doc
Summary:        Documentation for %{name}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  /usr/bin/xindy
BuildRequires:  tex-xetex-bin
# HTML theme is used as an extension even when building PDFs; we could perhaps
# patch it out of “extensions” in docs/conf.py, but it hardly seems worth the
# effort.
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n dateparser-%{version}

%if %{without calendars}
sed -r -i '/\<calendars\>/d' tox.ini
%endif

%if %{without fasttext}
sed -r -i '/\<fasttext\>/d' tox.ini
%endif

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/\<pytest-cov\>/d' tox.ini
sed -r -i 's/--cov[^[:blank:]]+//g' tox.ini

cat >> docs/conf.py <<'EOF'
# We cannot resolve remote Intersphinx mappings in an offline build.
intersphinx_mapping.clear()
# Since pdflatex cannot handle Unicode inputs in general:
latex_engine = 'xelatex'
EOF

%generate_buildrequires
%global toxenv -e all
%pyproject_buildrequires %{?with_tests:-t %{?toxenv}} %{?with_calendars:-x calendar }%{?with_fasttext:-x fasttext }-x langdetect dateparser_scripts/requirements.txt

%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs html SPHINXOPTS='%{?_smp_mflags}'
#%%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files dateparser dateparser_cli dateparser_data dateparser_scripts
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'

%check
%pyproject_check_import %{!?with_calendars:-e '*hijri*' -e '*jalali*'} %{!?with_fasttext:-e '*fasttext*'} -e '*.write_complete_data'
%if %{with tests}
%if %{without calendars}
# Uses hijri_convert
# --ignore does not seem to prevent doctest collection in tests/
rm -vf tests/test_hijri.py
ignore="${ignore-} --ignore=tests/test_hijri.py"
ignore="${ignore-} --ignore=dateparser/calendars/hijri.py"
ignore="${ignore-} --ignore=dateparser/calendars/hijri_parser.py"
# Uses convertdate
# --ignore does not seem to prevent doctest collection in tests/
rm -vf tests/test_jalali.py
ignore="${ignore-} --ignore=tests/test_jalali.py"
ignore="${ignore-} --ignore=dateparser/calendars/jalali.py"
ignore="${ignore-} --ignore=dateparser/calendars/jalali_parser.py"
%endif

%if %{without fasttext}
# Uses fasttext
# --ignore does not seem to prevent doctest collection in tests/
rm -vf tests/test_language_detect.py
ignore="${ignore-} --ignore=dateparser/custom_language_detection/fasttext.py"
ignore="${ignore-} --ignore=tests/test_language_detect.py"
%endif

# Fuzzing tests requires atheris which is not packaged in fedora.
# --ignore does not seem to prevent doctest collection in fuzzing/
rm -vf fuzzing/dateparser_fuzzer.py
rm -vf fuzzing/fuzz_helpers.py
ignore="${ignore-} --ignore=fuzzing/dateparser_fuzzer.py"
ignore="${ignore-} --ignore=fuzzing/fuzz_helpers.py"

# From the docstring containing this doctest:
#   In the example below, since no day information is present, the day is
#   assumed to be current day ``16`` from *current date* (which is June 16,
#   2015, at the moment of writing this). Hence, the level of precision is
#   ``month``:
# Obviously, yet bizarrely, this only works when it is *executed* on the 16th
# of some month.
k="${k-}${k+ and }not (DateDataParser and get_date_data)"

# The doctest parser does not like the line continuation here:
#     File "<doctest dateparser.search.search_dates[2]>", line 1
#       search_dates('The first artificial Earth satellite was launched on 4 October 1957.',
#                   ^
#   SyntaxError: '(' was never closed
k="${k-}${k+ and }not search_dates"

%tox -- -- ${ignore-} -k "${k-}" -v
%endif

%files -n python3-dateparser -f %{pyproject_files}
%exclude %{python3_sitelib}/dateparser_scripts/

%{_bindir}/dateparser-download
%{_mandir}/man1/dateparser-download.1*

%files -n python3-dateparser-scripts
%{python3_sitelib}/dateparser_scripts/

%files doc
%license LICENSE
%doc AUTHORS.rst
%doc CONTRIBUTING.rst
%doc HISTORY.rst
%doc README.rst
%if %{with doc_pdf}
#%%doc docs/_build/latex/dateparser.pdf
%doc docs/_build/html/
%endif

%changelog
%autochangelog
