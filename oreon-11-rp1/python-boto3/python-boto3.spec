%global source0_hash 20202c84b96625bab3d1ea2577c255fceb088f9c0ad187ed09757a8e8acca9a2

%bcond tests 1
# We would like to have a BuildRequires and weak runtime dependency on
# python3-awscrt, which enables additional functionality and tests, but it is
# ExcludeArch: s390x (https://bugzilla.redhat.com/show_bug.cgi?id=2180988) and
# we do not want to add architecture conditionals to this package, so we omit
# the dependency for now.
%bcond awscrt 0

Name:           python-boto3
Version:        1.42.70
Release:        1%{?dist}
Summary:        The AWS SDK for Python

License:        Apache-2.0
URL:            https://github.com/boto/boto3
Source:        https://github.com/boto/boto3/archive/refs/tags/1.42.70/boto3-1.42.70.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

# Save space by hardlinking duplicate JSON resource files
BuildRequires:  hardlink

%if %{with tests}
# Test dependencies are in requirements-dev.txt; most are Window-specific or
# are for coverage analysis and are undesired, so we list those we need
# manually:
BuildRequires:  %{py3_dist pytest}
# Run tests in parallel. Tests are numerous and painfully slow, so this helps!
BuildRequires:  %{py3_dist pytest-xdist}
%endif

%global _description %{expand:
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use of
services like Amazon S3 and Amazon EC2.}

%description %{_description}

%package -n     python3-boto3
Summary:        %{summary}

%if %{with awscrt}
# Optional dependency that enables additional functionality and additional
# tests, and is needed for the import-only “smoke test”:
#   boto3-1.34.7/boto3/s3/transfer.py
#   185:    # This feature requires awscrt>=0.19.18
BuildRequires:  %{py3_dist awscrt} >= 0.19.18
Recommends:     %{py3_dist awscrt} >= 0.19.18
%endif

%description -n python3-boto3 %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n boto3-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# This saves, as of this writing, roughly 300kB in duplicate JSON resource
# files. Note that rpmlint will complain about cross-directory hardlinks, but
# that these are not a problem because the contents of a directory owned by
# this package are guaranteed to be on a single filesystem.
hardlink -c '%{buildroot}%{python3_sitelib}/boto3'
%pyproject_save_files boto3

%check
%if %{with tests}
# Integration tests require network access and real AWS resources.
%pytest --ignore=tests/integration -v -n auto
%else
%pyproject_check_import %{?!with_awscrt:-e boto3.crt}
%endif

%files -n python3-boto3 -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.42.70-1
- Prepare for Oreon 11 (RP1)
