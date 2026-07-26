%global source0_hash 1e51802b09d4aa46568ca9618ed39e6977a0813cede3296783c9f8f21a93f2a6

Name:               python-Mastodon
Version:            2.1.4
Release:            1%{?dist}
Summary:            Python wrapper for the Mastodon API

License:            MIT
URL:                https://github.com/halcy/Mastodon.py
Source:             %{url}/archive/v%{version}/Mastodon.py-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      tomcli

%description
%{summary}.

%package -n python3-Mastodon
Summary:            %{summary}

%description -n python3-Mastodon
%{summary}.

%pyproject_extras_subpkg -n python3-Mastodon webpush blurhash

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Mastodon.py-%{version}
# Not packaged, and not strictly required:
tomcli set pyproject.toml lists delitem project.optional-dependencies.test \
    pytest-retry
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem project.optional-dependencies.test \
    pytest-cov
tomcli set pyproject.toml del tool.pytest.ini_options.addopts
# Avoid conflict of python3-magic with python3-file-magic, and it's not needed.
tomcli set pyproject.toml lists delitem project.dependencies 'python-magic ; platform_system!="Windows"'

%generate_buildrequires
%pyproject_buildrequires -x webpush,blurhash,test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mastodon

%check
#Disable tests until after 2.0.1
#%%pytest

%files -n python3-Mastodon -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
