# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 68789589cfde7098e8933fe3e69bbd864f7f0c22f118937b424d94d0e1b7760f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global srcname requests_file

Name:           python-requests-file
Version:        3.0.0
Release:        2%{?dist}
Summary:        Transport adapter for using file:// URLs with python-requests

License:        Apache-2.0
URL:            https://codeberg.org/dashea/requests-file
Source0:        https://files.pythonhosted.org/packages/source/r/requests_file/requests_file-3.0.0.tar.gz

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
%oreon_verify_sources
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
