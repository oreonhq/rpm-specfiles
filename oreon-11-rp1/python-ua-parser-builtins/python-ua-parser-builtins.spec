%global source0_hash 7fd272927cc60b0238deb828dff019425c9c77eb2b72cc32ba66e89a0db2a8e6

%global pkg_name ua-parser-builtins

Name:           python-%{pkg_name}
Version:        0.18.0.post1
Release:        6%{?dist}
Summary:        Precompiled rules for User Agent Parser

License:        Apache-2.0
URL:            https://github.com/ua-parser/uap-python
BuildArch:      noarch
# git clone --recursive https://github.com/ua-parser/uap-python.git ua_parser
# cd ua_parser/ua-parser-builtins
# cp ../LICENSE .
# python3 -m build --sdist
# cp dist/ua_parser_builtins-%%{version}.tar.gz ../../
# NOTE: Requested upstream to publish a sdist archive and add a LICENSE file:
# => https://github.com/ua-parser/uap-python/issues/262
Source0:        ua_parser_builtins-%{version}.tar.gz

BuildRequires:  python3-devel

%description
Precompiled rules for User Agent Parser.

%package -n python3-%{pkg_name}
Summary:        Precompiled rules for User Agent Parser

%description -n python3-%{pkg_name}
Precompiled rules for User Agent Parser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ua_parser_builtins-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l ua_parser_builtins

%check
# %%pyproject_check_import cannot be run because of circular dependency on ua-parser

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
