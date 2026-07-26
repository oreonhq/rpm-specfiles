%global source0_hash 2f32b6e95b6500d24cd6332207eb67b9324298f60fe1d7d8948a2964aaebea53

%global commit 5acbe50717a4f53a411310f03eb5f6ad13b3d1ea

Name:           python-sphinxcontrib-globalsubs
Version:        0.1.1
Release:        %autorelease
Summary:        Global substitutions defined in conf.py
License:        BSD-2-Clause
URL:            https://github.com/missinglinkelectronics/sphinxcontrib-globalsubs
%global forgeurl %{url}
%forgemeta
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
This extension adds support for global substitutions to conf.py.
One of the main use cases are central abbreviation lists, but any valid
reST markup can be substituted.
}
%description %_description

%package -n python3-sphinxcontrib-globalsubs
Summary:        %{summary}

%description -n python3-sphinxcontrib-globalsubs %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sphinxcontrib-globalsubs-%{commit}

%build
%py3_build

%install
%py3_install

# %%check
# upstream has no testsuite

%files -n python3-sphinxcontrib-globalsubs
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/sphinxcontrib/*
%{python3_sitelib}/sphinxcontrib_globalsubs-%{version}-py%{python3_version}.egg-info/
%exclude %{python3_sitelib}/sphinxcontrib_globalsubs-*.pth

%changelog
%autochangelog
