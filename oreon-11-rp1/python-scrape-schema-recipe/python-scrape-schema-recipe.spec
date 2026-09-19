%global source0_hash 32940a11635faa7fdf73fc6b91f4a902c09cf2015123f99298be2bfc6dacb870

%global         srcname         scrape-schema-recipe
%global         forgeurl        https://github.com/micahcochran/scrape-schema-recipe
Version:        0.2.2
%global         tag             %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Scrape recipes from HTML into Python dictionaries

License:        Apache-2.0
URL:            %{forgeurl}
# Prepare source offline to not include files with proprietary licenses
Source0:        %{srcname}-cleaned-%{version}.tar.gz
Source1:        prepare.sh
# Modify function not to return names of removed files
Patch:          example-names.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

BuildArch: noarch

%global _description %{expand:
Scrapes recipes from HTML https://schema.org/Recipe (Microdata/JSON-LD)
into Python dictionaries.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files scrape_schema_recipe -l

%check
%pyproject_check_import
# Do not run tests that require network access and
# that cannot use data that cannot be redistributed
# in Fedora
sed -i 's/DISABLE_NETWORK_TESTS = False/DISABLE_NETWORK_TESTS = True/g'\
    test_scrape.py
k="${k-}${k+ and }not TestUnsetTimeDate"
k="${k-}${k+ and }not TestTypeList"
k="${k-}${k+ and }not (TestEscaping and test_unescape_ingredients)"
k="${k-}${k+ and }not (TestEscaping and test_unescape_name_description)"
k="${k-}${k+ and }not (TestLoads and test_loads)"
k="${k-}${k+ and }not (TestUnMigratedSchema and test_recipe1)"
k="${k-}${k+ and }not (TestUnMigratedSchema and test_recipe2)"
k="${k-}${k+ and }not (TestExampleOutput and test_example_output)"
k="${k-}${k+ and }not (TestGraph and test_graph)"
k="${k-}${k+ and }not (TestParsingFileMicroData and test_name)"
k="${k-}${k+ and }not (TestParsingFileMicroData and test_num_recipes)"
k="${k-}${k+ and }not (TestParsingFileMicroData and test_recipe_keys)"
k="${k-}${k+ and }not (TestParsingFileMicroData and test_recipe_yield)"
k="${k-}${k+ and }not (TestParsingFileMicroData and test_totalTime_sum)"
k="${k-}${k+ and }not (TestParsingFileLDJSON and test_category)"
k="${k-}${k+ and }not (TestParsingFileLDJSON and test_duration)"
k="${k-}${k+ and }not (TestParsingFileLDJSON and test_ingredients)"
k="${k-}${k+ and }not (TestParsingFileLDJSON and test_instructions)"
k="${k-}${k+ and }not (TestParsingFileLDJSON and test_name)"
k="${k-}${k+ and }not (TestParsingFileLDJSON and test_num_recipes)"
k="${k-}${k+ and }not (TestParsingFileLDJSON and test_recipe_keys)"
k="${k-}${k+ and }not (TestTimeDelta and test_timedelta)"
k="${k-}${k+ and }not (TestTimeDelta and test_totalTime_sum)"
k="${k-}${k+ and }not (TestDateTime and test_datetime_tz_python_obj)"
k="${k-}${k+ and }not (TestDateTime and test_datetime_tz_python_obj_isodate)"
k="${k-}${k+ and }not (TestDateTime and test_publish_date_python_obj)"
k="${k-}${k+ and }not (TestPythonObjects and testDateTypes)"
k="${k-}${k+ and }not (TestPythonObjects and testDatesEqual)"
k="${k-}${k+ and }not (TestPythonObjects and testDurationEqual)"
k="${k-}${k+ and }not (TestPythonObjects and testDurationTypes)"

%pytest -k "${k-}"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
 
%changelog
%autochangelog
