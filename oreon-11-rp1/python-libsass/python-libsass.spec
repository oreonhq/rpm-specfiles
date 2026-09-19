%global source0_hash 4bff7819756f52f6e4592f03f205104d1ca431088d9452aed5042f89a36f9873

Name:           python-libsass
Version:        0.23.0
Release:        %autorelease
Summary:        Sass for Python: A straightforward binding of libsass for Python

# SPDX
License:        MIT
URL:            https://github.com/dahlia/libsass-python
Source:         %{url}/archive/%{version}/libsass-python-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l sass pysassc sasstests sassutils _sass

# Selected test dependencies from requirements-dev.txt; most entries in that
# file are for linters, code coverage, etc.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  (%{py3_dist werkzeug} with %{py3_dist werkzeug} >= 0.9)

BuildRequires:  make
BuildRequires:  gcc-c++

BuildRequires:  libsass-devel >= 3.6.6

BuildRequires:  help2man

%global common_description %{expand:
This package provides a simple Python extension module sass which is binding
LibSass (written in C/C++ by Hampton Catlin and Aaron Leung). It’s very
straightforward and there isn’t any headache related to Python
distribution/deployment. That means you can add just libsass into your
setup.py’s install_requires list or requirements.txt file. No need for Ruby nor
Node.js.}

%description %{common_description}

%package -n python3-libsass
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/
#   #_provides_for_importable_modules
# This package is messy; it occupies quite a few top-level names.
%py_provides python3-sass
%py_provides python3-pysassc
%py_provides python3-sasstests
%py_provides python3-sassutils

# PDF documentation build and -doc subpackage dropped in Fedora 42; we can
# remove this after Fedora 44 reaches end-of-life.
Obsoletes:      python-libsass-doc < 0.23.0-6

%description -n python3-libsass %{common_description}

%prep -a
# While upstream has the executable bit set, we will install this in
# site-packages without executable permissions; therefore, the shebang becomes
# useless, and we should remove it downstream.
sed -r -i '1{/^#!/d}' pysassc.py

%generate_buildrequires -p
export SYSTEM_SASS='1'

%build -p
export SYSTEM_SASS='1'

%install -p
export SYSTEM_SASS='1'

%install -a
# We build the man page in %%install rather than %%build because we need to use
# the entry point in %%{buildroot}/%%{_bindir}.
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitearch}' \
    help2man --no-info --output='%{buildroot}%{_mandir}/man1/pysassc.1' \
    '%{buildroot}%{_bindir}/pysassc'

%check -a
%pytest -v sasstests.py

%files -n python3-libsass -f %{pyproject_files}
%doc README.rst
%doc docs/changes.rst
%{_bindir}/pysassc
%{_mandir}/man1/pysassc.1*

%changelog
%autochangelog
