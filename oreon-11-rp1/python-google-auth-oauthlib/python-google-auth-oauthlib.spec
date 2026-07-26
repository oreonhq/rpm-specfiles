%global source0_hash 3ca93859c6cc9003c8e12b2a0868915209d7953f05a70f4880ab57d57e56ee3e

%global pypi_name google-auth-oauthlib

Name:           python-%{pypi_name}
Version:        1.2.4
Release:        %autorelease
Summary:        Google oAuth Authentication Library

License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib
Source0:        %{pypi_source google_auth_oauthlib}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pytest)

%description
This library provides oauthlib integration with google-auth.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This library provides oauthlib integration with google-auth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n google_auth_oauthlib-%{version} -p1
rm -rf /docs/

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files google_auth_oauthlib

# Re-enable when the authpin patch is dropped.
#%%check
#%%pytest -k 'not test_run_local_server_bind_addr'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/google-oauthlib-tool

%changelog
%autochangelog
