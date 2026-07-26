%global source0_hash 4a3b9141033798e4fb07886ff26254e635e022acbdd708375eac6f56e323506c

%global srcname apache-libcloud
%global shortname libcloud

%global _description %{expand:
libcloud is a client library for interacting with many of
the popular cloud server providers.  It was created to make
it easy for developers to build products that work between
any of the services that it supports.}

# Don't duplicate the same documentation
%global _docdir_fmt %{name}

Name:           python-%{shortname}
Version:        3.6.0
Release:        17%{?dist}
Summary:        A Python library to address multiple cloud provider APIs

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://libcloud.apache.org/
Source0:        %{pypi_source}
BuildArch:      noarch

# This is a downstream only patch persuant to
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch0:         000-remove-linter-deps.patch

# https://issues.apache.org/jira/browse/LEGAL-572
# Removing version restriction on python-requests
%{?el9:Patch1:  001-requests-chardet-unbundled.patch}

%description %{_description}

%package -n python3-%{shortname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{shortname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Don't package the test suite. We dont run it anyway
# because it requires valid cloud credentials.
rm -r %{shortname}/test/

# Delete shebang lines in the demos
sed -i '1d' demos/gce_demo.py demos/compute_demo.py

# Fix permissions for demos
chmod -x demos/gce_demo.py demos/compute_demo.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{shortname}

%files -n python3-%{shortname} -f %{pyproject_files}
%doc README.rst demos/
%license LICENSE

%check
%pyproject_check_import -t %{shortname}

%changelog
%autochangelog
