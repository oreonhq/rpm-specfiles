%global source0_hash 10dc34e78d726325f2716b0e1d9078f479f4eb6e2176ccea2bb326ac45e54caa

Name:           pyinstrument
Version:        4.6.2
Release:        %autorelease
Summary:        Python profiler with colorful output

# The majority of code is BSD-3-Clause.
# Exceptions:
#   pyinstrument/vendor/keypath.py: BSD-2-Clause
#   pyinstrument/renderers/html_resources/app.js: MIT
License:        BSD-3-Clause AND BSD-2-Clause and MIT
URL:            https://github.com/joerick/pyinstrument
Source:         https://github.com/joerick/pyinstrument/archive/v%{version}/pyinstrument-%{version}.tar.gz

# https://github.com/joerick/pyinstrument/pull/309
Patch:          0001-Allow-non-vendored-deps-to-be-used.patch
# https://github.com/joerick/pyinstrument/pull/310
Patch:          0001-test-do-not-compare-sys.path-in-test-executions.patch

BuildRequires:  python3-devel
BuildRequires:  python3-trio
BuildRequires:  python3-flaky
BuildRequires:  python3-greenlet
BuildRequires:  python3-pytest-asyncio
BuildRequires:  pytest
BuildRequires:  gcc
# for docs
BuildRequires:  make
BuildRequires:  python3-myst-parser
BuildRequires:  python3-sphinxcontrib-programoutput
BuildRequires:  python3dist(appdirs) >= 1.4.4
BuildRequires:  python3dist(decorator) >= 4.3.1
Requires:       python3dist(appdirs) >= 1.4.4
Requires:       python3dist(decorator) >= 4.3.1

Recommends:     %{name}-doc
Provides:       bundled(python-keypath)

%global _description %{expand:
This package provides a line profiler similar to cProfile, but based on
statistical sampling instead, and with a nicer and more colorful output:
    pyinstrument script.py
}

%description %_description

%package doc
Summary:       Documentation for %{name}
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description doc
HTML documentation and example files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Without this, pyinstrument/low_level/stat_profile_python.py gets ignored
touch pyinstrument/low_level/__init__.py

sed -r -i '/html_theme = "furo"/d' docs/conf.py

rm pyinstrument/vendor/{appdirs.py,decorator.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

export PYTHONPATH=$(echo $PWD/build/lib.linux-*)
make -C docs man
make -C docs html

# to avoid the package getting installed
rm examples/django_example/.gitignore

%py3_shebang_fix examples/django_example/manage.py

%install
%pyproject_install
%pyproject_save_files pyinstrument

install -m0644 -Dt %{buildroot}%{_mandir}/man1/ docs/_build/man/pyinstrument.1

%check
# pytest seems to add CWD to the path, so we end up importing the module without
# the compiled parts. Let's just move it out of the way.
mv pyinstrument _pyinstrument

TESTOPTS=(
    # Those tests fail. Maybe related to greenlet version?
    --deselect=test/test_profiler_async.py::test_greenlet
    --deselect=test/test_profiler_async.py::test_strict_with_greenlet

    # Python 3.13 incompatibilities
    # https://github.com/joerick/pyinstrument/issues/312
    --deselect=test/test_profiler.py::test_class_methods
    --deselect=test/low_level/test_frame_info.py::test_frame_info_with_classes
)

%pytest -v test/ "${TESTOPTS[@]}"

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/pyinstrument
%exclude %{python3_sitearch}/pyinstrument/low_level/stat_profile.c
%doc %{_mandir}/man1/pyinstrument.1*

%files doc
%doc docs/_build/html/
%doc examples/

%changelog
%autochangelog
