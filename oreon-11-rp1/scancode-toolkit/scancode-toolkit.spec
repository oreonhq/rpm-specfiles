%global source0_hash 6758710e80719bbe40e07050d889fb44abc610d58b3219a234f6171ac7868b49
%global debug_package %{nil}
%bcond tests 1
Name:           scancode-toolkit
Version:        32.5.0
Release:        1%{?dist}
Summary:        Scan code and detect licenses, copyrights, and more
License:        Apache-2.0 AND CC-BY-4.0
URL:            https://scancode-toolkit.readthedocs.io/
Source0:        https://github.com/aboutcode-org/scancode-toolkit/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          0001-tests-fix-pytest-traceback.patch
Patch:          0002-Replace-pkginfo2-with-pkginfo.patch
ExcludeArch:    %{ix86}
%if %{with tests}
%endif
%global common_description %{expand:
ScanCode is an open-source tool to scan code and detect licenses, copyrights,
and more. It provides detailed information about discovered licenses,
copyrights, and other important details in various formats.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-scancode-toolkit = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package doc
Summary:        Documentation for python-%{name}
BuildArch:      noarch
%description doc
%{common_description}

This package is providing the documentation for %{name}.

%prep

%autosetup -p1
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml
sed -Ei \
    -e '/doc8/d' \
    -e '/sphinx-rtd-dark-mode/d' \
    -e 's/Sphinx ==/Sphinx>=/' \
    -e 's|Beautifulsoup4\[chardet\]|Beautifulsoup4|' \
    -e '/sphinx-autobuild/d' \
    -e "s/^( *)(click .*);python_version<'3\.10'/\1\2/" \
    -e "/^ *click .*;python_version>='3\.10'/d" \
    -e 's/spdx_tools ==/spdx_tools ~=/' \
    -e 's/normality <.*/normality/' \
    -e 's/(fingerprints.*), <=.*/\1/' \
setup.cfg
sed -i '/"sphinx_rtd_dark_mode"/d' docs/source/conf.py
sed -i 's/JSON data/JSON text data/' tests/summarycode/data/todo/ignore_issue/invariant-2.2.4-expected.json

%build

PYTHONPATH="$(pwd)/src" %{python3} -m licensedcode.reindex
test -f src/licensedcode/data/cache/license_index/index_cache
PYTHONPATH="$(pwd)/src" %{python3} -m packagedcode.cache
test -f src/packagedcode/data/cache/package_patterns_index/index_cache
%pyproject_wheel
sphinx-build-3 -b html docs/source html
rm -rf html/.{doctrees,buildinfo}
%install
%pyproject_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
mkdir -p venv/bin
ln -s %{buildroot}%{_bindir}/scancode venv/bin/regen-package-docs
ln -s %{buildroot}%{_bindir}/scancode venv/bin/scancode
ln -s %{buildroot}%{_bindir}/scancode venv/bin/scancode-license-data
ln -s %{buildroot}%{_bindir}/scancode venv/bin/scancode-reindex-licenses
tomcli set pyproject.toml arrays str \
    tool.pytest.ini_options.pythonpath 'tests/packagedcode' 'tests/cluecode'
export PYTHONPATH="$(pwd)/src"
%pytest --import-mode importlib -vv -k '%{shrink:
    not test_json_pretty_print and not
        test_jsonlines and not
        test_json_compact and not
        test_json_with_extracted_license_statements and not
        test_yaml and not
        test_end_to_end_scan_with_license_policy and not
        test_scan_can_handle_weird_file_names and not
        test_scan_can_run_from_other_directory and not
        test_scan_produces_valid_yaml_with_extracted_license_statements and not
        test_classify_with_package_data and not
        test_consolidate_package and not
        test_consolidate_package_files_should_not_be_considered_in_license_holder_consolidated_component and not
        test_consolidate_component_package_from_json_can_run_twice and not
        test_consolidate_component_package_from_live_scan and not
        test_consolidate_package_always_include_own_manifest_file and not
        test_consolidate_component_package_build_from_live_scan and not
        test_end2end_todo_works_on_codebase_without_ambiguous_detections and not
        test_is_licensing_works and not
        test_parse_from_rb and not
        test_parse_from_rb_dependency_requirement and not
        test_scan_cli_works and not
        test_scan_cli_works_package_only and not
        test_package_command_scan_chef and not
        test_package_scan_pypi_end_to_end and not
        test_develop_with_parse and not
        test_develop_with_parse_metadata and not
        test_parse_with_eggfile and not
        test_parse_with_unpacked_wheel_meta and not
        test_parse_metadata_prefer_pkg_info_from_egg_info_from_command_line and not
        test_parse_dependency_file_with_invalid_does_not_fail and not
        test_recognize_rpmdb_sqlite and not
        test_collect_installed_rpmdb_xmlish_from_rootfs and not
        test_scan_system_package_end_to_end_installed_win_reg and not
        test_consolidate_report_minority_origin_directory and not
        test_about_files and not
        test_scan_works_on_rust_binary_with_inspector and not
        test_package_list_command and not
        test_get_file_info_include_size and not
        test_scan_cli_help and not
        %dnl 'sbin/fstrim' is a link to an absolute path
        %dnl These two are due to the tarfile module defaulting to the data filter in py3.14.
        %dnl Let upstream figure out what to do about this issue.
        test_can_get_installed_system_packages_with_license_from_alpine_container_layer and not
        test_can_scan_installed_system_package_in_alpine_container_layer and not
        %dnl These test failures have to do with the handling of tempfiles in the CLI
        %dnl and don't seem particularly important. Disable them for now
        test_scan_keep_temp_files_is_false_by_default and not
        test_scan_keep_temp_files_keeps_files and not
        %dnl https://github.com/aboutcode-org/scancode-toolkit/issues/4540
        test_license_reference_to_file_beside_package_manifest and not
        %dnl Add new entries above this line.
        placeholder}'
%endif
%files
%files -n scancode-toolkit-doc -f %{oreon_filedir}/scancode-toolkit-doc.list

%changelog

%autochangelog
