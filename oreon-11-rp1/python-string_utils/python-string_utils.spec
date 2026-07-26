%global source0_hash 0f0ec393ec2ac0f936e766be7fad605980a474de7d0421ed56fd79e8c1a2e2c7

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-string_utils
Version:        1.0.0
Release:        23%{?dist}
Summary:        Utility functions for strings validation and manipulation

# SPDX
License:        MIT
URL:            https://github.com/daveoncode/python-string-utils
Source0:        %{url}/archive/v%{version}/python-string-utils-%{version}.tar.gz

# Remove README.md as packaged data in the wheel
# https://github.com/daveoncode/python-string-utils/pull/16
#
# This keeps it from being installed to the bizarre path
# %%{_prefix}/README/README.md.
Patch:          %{url}/pull/16.patch

BuildArch:      noarch

%global _description %{expand:
A handy library to validate, manipulate and generate strings, which is:

  • Simple and “pythonic”
  • Fully documented and with examples! (html version on readthedocs.io)
  • 100% code coverage! (see it with your own eyes on codecov.io)
  • Tested (automatically on each push thanks to Travis CI) against all
    officially supported Python versions
  • Fast (mostly based on compiled regex)
  • Free from external dependencies
  • PEP8 compliant}

%description %{_description}

# The source package is named python-string_utils for historical reasons.  The
# binary package, python3-python-string-utils, is named using the canonical
# project name[1]; see also [2].
#
# The %%py_provides macro is used to provide an upgrade path from
# python3-string_utils and to produce the appropriate Provides for the
# importable module[3].
#
# [1] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_canonical_project_name
# [2] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming
# [3] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%package -n python3-python-string-utils
Summary:        %{summary}

# Provide an upgrade path
%py_provides python3-string_utils
Obsoletes:      python3-string_utils < 1.0.0-11

BuildRequires:  python3-devel

%description -n python3-python-string-utils %{_description}

%package doc
Summary:        Documentation for python-string-utils

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
# The HTML theme is used as a Sphinx extension, so it is needed even when not
# producing HTML output.
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n python-string-utils-%{version} -p1

# Remove bogus executable permissions from non-script files. This corresponds
# to the upstream pull request:
#
# Change files permissions to 644
# https://github.com/daveoncode/python-string-utils/pull/4
find . -type f -perm /0111 \
    -exec gawk '!/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t chmod -v a-x

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files string_utils

%check
%tox

%files -n python3-python-string-utils -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/PythonStringUtils.pdf
%endif

%changelog
%autochangelog
