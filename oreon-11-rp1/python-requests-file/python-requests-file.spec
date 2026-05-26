%global srcname requests_file

Name:           python-requests-file
Version:        3.0.0
Release:        2%{?dist}
Summary:        Transport adapter for using file:// URLs with python-requests

License:        Apache-2.0
URL:            https://codeberg.org/dashea/requests-file
Source0:        https://files.pythonhosted.org/packages/source/r/requests_file/requests_file-3.0.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 68789589cfde7098e8933fe3e69bbd864f7f0c22f118937b424d94d0e1b7760f
%global source0_file requests_file-3.0.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Requests-File is a transport adapter for use with the Requests Python
library to allow local file system access via file:// URLs.}

%description %_description

%package -n python3-requests-file
Summary:        %{summary}

%description -n python3-requests-file %_description

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/requests_file-3.0.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "68789589cfde7098e8933fe3e69bbd864f7f0c22f118937b424d94d0e1b7760f" || { echo "oreon: Source0 SHA256 mismatch for requests_file-3.0.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files requests_file

%check
%{pytest}

%files -n python3-requests-file -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-2
- Prepare for Oreon 11 (RP1)
