%global source0_hash 6387584c38e5758431f5d61c269860892f57b7442c0cf9bd712ad64231b9bb1c

%global short_name lsp-black

%global _description %{expand:
lsp-black is a python-lsp-server plugin that adds support to black
autoformatter. This is forked from pyls-black to be compatible wth
community maintained language-server (python-lsp-server).
}

Name:           python-%{short_name}
Version:        2.0.0
Release:        %autorelease
Summary:        A python-lsp-server plugin that adds support to black autoformatter

%global forgeurl https://github.com/python-lsp/python-lsp-black
%forgemeta

# SPDX
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}
# Fix tests failing since `black >= 24.3.0`
# https://github.com/python-lsp/python-lsp-black/issues/57
Patch:          %{forgeurl}/pull/59.patch
# And two more failing since `black >= 24.4.0`
# https://github.com/python-lsp/python-lsp-black/issues/57
Patch:          %{forgeurl}/pull/56.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pytest

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}

Supplements:    python3dist(python-lsp-server)

%description -n python3-%{short_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
# Remove version pinning from python-lsp-server dependency
sed -i -r -e 's/(lsp-server)>=.*/\1/' setup.cfg
# Remove Python version upper bound
sed -i -e 's/; python_version.*//' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x extras_require

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pylsp_black

%check
%pytest -v

%files -n python3-%{short_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
