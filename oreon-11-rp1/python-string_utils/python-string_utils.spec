%global source0_hash 0f0ec393ec2ac0f936e766be7fad605980a474de7d0421ed56fd79e8c1a2e2c7
%bcond_without doc_pdf
Name:           python-string_utils
Version:        1.0.0
Release:        1%{?dist}
Summary:        Utility functions for strings validation and manipulation
License:        MIT
URL:            https://github.com/daveoncode/python-string-utils
Source0:        https://github.com/daveoncode/python-string-utils/archive/v%{version}/python-string-utils-%{version}.tar.gz
Patch:          %{url}/pull/16.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-string_utils = %{version}-%{release}
# /oreon:deps
%description

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
Summary:        Utility functions for strings validation and manipulation
%py_provides python3-string_utils
Obsoletes:      python3-string_utils < 1.0.0-11
BuildRequires:  python3-devel
%description -n python3-python-string-utils

%package doc
Summary:        Documentation for python-string-utils
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
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

%build

%pyproject_wheel
%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif
%install
%pyproject_install
%oreon_autofiles python3-python-string-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%tox
%files
%files -n python3-python-string-utils -f %{oreon_filedir}/python3-python-string-utils.list
%files -n python-string_utils-doc -f %{oreon_filedir}/python-string_utils-doc.list

%changelog

%autochangelog
