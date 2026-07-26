%global source0_hash 5581db0b209972fec4a0fe861af5081c42bfeca2d4350948bc13fd1ccaf301be

Name:           python-aiomysql
Version:        0.2.0
Release:        11%{?dist}
Summary:        MySQL driver for asyncio

License:        MIT
URL:            https://github.com/aio-libs/aiomysql
Source0:        %{url}/archive/v%{version}/aiomysql-%{version}.tar.gz
BuildArch:      noarch

%global _description %{expand:
aiomysql is a “driver” for accessing a MySQL database from the asyncio
(PEP-3156/tulip) framework. It depends on and reuses most parts of PyMySQL .
aiomysql tries to be like awesome aiopg library and preserve same api, look and
feel.}

%description %{_description}

%package -n     python3-aiomysql
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-aiomysql %{_description}

%pyproject_extras_subpkg -n python3-aiomysql sa rsa

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n aiomysql-%{version}
# Upstream has pinned setuptools_scm due to the generated wheel version being wrong:
# https://github.com/aio-libs/aiomysql/commit/fb85893635d7f9c0da3b1ff8c6d0fc436357633a
# We must work with what we have.
sed -r -i 's/"(setuptools_scm.*), <.*"/"\1"/' pyproject.toml
# Furthermore, we don’t need setuptools_scm_git_archive.
sed -r -i '/"setuptools_scm_git_archive/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x sa,rsa

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aiomysql

%check
%pyproject_check_import
# Upstream testing is done with a Docker container. Setting up a MySQL server
# for testing might be possible, but not trivial. See the python-asyncmy
# package for inspiration.

%files -n python3-aiomysql -f %{pyproject_files}
# LICENSE is handled by pyproject_files; verify with “rpm -qL -p …”
%doc README.rst

%changelog
%autochangelog
