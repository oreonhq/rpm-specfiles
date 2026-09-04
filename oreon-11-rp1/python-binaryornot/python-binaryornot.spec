%global source0_hash cc8d57cfa71d74ff8c28a7726734d53a851d02fad9e3a5581fb807f989f702f0

%global modname binaryornot
%global sum A pure Python package to check if a file is binary or text

Name:               python-binaryornot
Version:            0.6.0
Release:            %autorelease
Summary:            %{sum}

License:            BSD-3-Clause
URL:                http://pypi.python.org/pypi/BinaryOrNot
Source:             https://pypi.python.org/packages/source/b/binaryornot/binaryornot-%{version}.tar.gz
# Required to fix a test https://github.com/binaryornot/binaryornot/pull/52
Patch:              38dee57986c6679d99.patch
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-hypothesis

%global _description %{expand:
Ultra-lightweight pure Python package to guess whether a file is binary or
text, using a heuristic similar to Perl's pp_fttext and its analysis by
@eliben.

Has tests for these file types:
* Text: .txt, .css, .json, .svg, .js, .lua, .pl, .rst * Binary: .png, .gif,
.jpg, .tiff, .bmp, .DS_Store, .eot, .otf, .ttf, .woff, .rgb

Has tests for numerous encodings.}

%description %_description

%package -n         python3-%{modname}
Summary:            %{sum}

%description -n python3-binaryornot %_description

%package -n         python-%{modname}-docs
Summary:            Documentation for python-binaryornot
BuildRequires:      python3-sphinx
BuildRequires:      make

%description -n python-%{modname}-docs
Documentation for python-binaryornot

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

make -C docs html PYTHONPATH=$(pwd)
rm -rf docs/_build/html/.buildinfo

%install
%pyproject_install

%pyproject_save_files -l %{modname}

%check
%{__python3} -m unittest discover -v

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%files -n python-%{modname}-docs
%doc docs/_build/html

%changelog
%autochangelog
