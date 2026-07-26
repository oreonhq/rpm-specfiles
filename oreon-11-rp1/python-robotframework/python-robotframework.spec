%global source0_hash 6fa65c2708f0d48dd7a05bea2dc96943d0e39fdac9b3eb7290e780200b2cec57

%global srcname robotframework

Name:           python-%{srcname}
Version:        7.4.1
Release:        2%{?dist}
Summary:        Generic automation framework for acceptance testing and RPA
# Robot Framework is licensed as Apache-2.0
# Support libraries to display HTML results:
#  - jQuery, jQuery Highlight plugin: MIT
#  - jQuery Tablesorter, jQuery Templates plugin: MIT or GPLv2
#  - JSXCompressor: Apache-2.0 or LGPLv3
#  - OpenIconic icons (as base64): MIT
License:        Apache-2.0 and MIT
URL:            https://github.com/robotframework/robotframework
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-jsonschema
BuildRequires:  python3-typing-extensions

%global _description %{expand:
Robot Framework is a generic open source automation framework for acceptance
testing, acceptance test driven development (ATDD), and robotic process
automation (RPA).
It has simple plain text syntax and it can be extended easily with libraries
implemented using Python or Java.}

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

# Bundled JavaScript for reports
Provides:      bundled(jquery) = 3.5.1
Provides:      bundled(jquery-highlight)
Provides:      bundled(jquery-tablesorter) = 2.30.5
Provides:      bundled(jquery-templates) = 1.0.0pre
Provides:      bundled(jsxcompressor)

%description -n python3-%{srcname}
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files robot

%check
%{python3} utest/run.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst BUILD.rst INSTALL.rst CONTRIBUTING.rst
%license LICENSE.txt
%{_bindir}/{robot,rebot,libdoc}

%changelog
%autochangelog
