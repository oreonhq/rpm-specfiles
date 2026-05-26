%global srcname s3transfer
%global _description \
S3transfer is a Python library for managing Amazon S3 transfers.

Name:           python-%{srcname}
Version:        0.16.0
Release:        2%{?dist}
Summary:        Amazon S3 Transfer Manager

License:        Apache-2.0
URL:            https://pypi.org/project/s3transfer/
Source0:        https://files.pythonhosted.org/packages/source/s/s3transfer/s3transfer-0.16.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 8e990f13268025792229cd52fa10cb7163744bf56e719e0b9cb925ab79abf920
%global source0_file s3transfer-0.16.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
# required to run the test suite
BuildRequires:  python3dist(botocore) >= 1.12.36
BuildRequires:  python3dist(botocore) < 2.0
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/s3transfer-0.16.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8e990f13268025792229cd52fa10cb7163744bf56e719e0b9cb925ab79abf920" || { echo "oreon: Source0 SHA256 mismatch for s3transfer-0.16.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest tests/unit tests/functional

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.0-2
- Prepare for Oreon 11 (RP1)
