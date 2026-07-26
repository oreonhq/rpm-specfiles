%global source0_hash 22d12da1080080ef3494b38a994a43ac5711ef6492e8fe3a08b0e6d148ab9caa

Name:           python-crochet
Version:        2.1.1
Release:        12%{?dist}
Summary:        A library that makes it easier to use Twisted from blocking code

# Patches needed for compatibility with Python 3.12
Patch1:         https://github.com/itamarst/crochet/pull/150.patch

License:        MIT
URL:            https://github.com/itamarst/crochet
Source0:        %{url}/archive/%{version}/crochet-%{version}.tar.gz
BuildArch:      noarch

%global _description %{expand:
Crochet is an MIT-licensed library that makes it easier to use Twisted from
regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with Twisted more
  cleanly from their threaded parts. For example, this can be useful when using
  Twisted as a WSGI container.}

%description %_description

%package doc
Summary: Documentation for python-crochet

BuildRequires:  make
BuildRequires:  python3-sphinx

%description doc
Documentation for python-crochet.

%package -n python3-crochet
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-crochet %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n crochet-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%make_build -C docs html
rm docs/_build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files -l crochet

%check
%{py3_test_envvars} %{python3} -m unittest discover -v crochet.tests

%files -n python3-crochet -f %{pyproject_files}
%doc README.rst

%files doc
%license LICENSE
%doc docs/_build/html

%changelog
%autochangelog
