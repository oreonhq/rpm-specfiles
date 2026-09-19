%global source0_hash 9d1f8b37a689e2b7da0645592d55473a1f0f5fc571f811028441cdfaed9dbda3

%global pypi_name packageurl-python
%global purl_spec_commit c398646bb2d642ccdd43bfbf5923cf650d69dc6a

Name:           python-%{pypi_name}
Version:        0.17.6
Release:        %autorelease
Summary:        Python implementation of the package url spec

License:        MIT
URL:            https://github.com/package-url/packageurl-python
Source0:        %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# For running tests
Source1:        https://github.com/package-url/purl-spec/archive/%{purl_spec_commit}/purl-spec-%{purl_spec_commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
A parser and builder for purl aka. Package URLs for Python 2 and 3. See
https://github.com/package-url/purl-spec for details.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
mkdir -p spec
tar -C spec --strip-components=1 -xf %{S:1}
rm -rfv thirdparty/

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files packageurl

%check
%pytest tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst README.rst
%license mit.LICENSE

%changelog
%autochangelog
