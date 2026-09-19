%global source0_hash 6fdef854115f413e5d8a0241e1e67e93f0bd29c1d1317a742f3fdb189e1d57b5

%global srcname hyperlink

%global common_description %{expand:
The humble, but powerful, URL runs everything around us. Chances are you've
used several just to read this text. Hyperlink is a featureful, pure-Python
implementation of the URL, with an emphasis on correctness.}

Name:           python-%{srcname}
Version:        21.0.0
Release:        %autorelease
Summary:        A featureful, immutable, and correct URL for Python

# MIT: main library
# BSD: searchtools.js, websupport.js and modernizr.min.js
# OFL: Inconsolata-Regular.ttf and Inconsolata-Bold.ttf
# Automatically converted from old format: MIT and BSD and OFL - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-OFL
URL:            https://github.com/python-hyper/hyperlink
Source0:        %url/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=%{pyproject_build_lib} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog
