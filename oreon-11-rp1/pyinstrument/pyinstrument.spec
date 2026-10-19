%global source0_hash d2af5a67c4a230c86759109f941e436f533009934c016eb402c0a9c42b47ccee
Name:           pyinstrument
Version:        5.1.3
Release:        1%{?dist}
Summary:        Python profiler with colorful output
License:        BSD-3-Clause AND BSD-2-Clause and MIT
URL:            https://github.com/joerick/pyinstrument
Source0:        https://github.com/joerick/pyinstrument/archive/v%{version}/pyinstrument-%{version}.tar.gz
Patch:          0001-Allow-non-vendored-deps-to-be-used.patch
Patch:          0001-test-do-not-compare-sys.path-in-test-executions.patch
Requires:       python3dist(appdirs) >= 1.4.4
Requires:       python3dist(decorator) >= 4.3.1
Recommends:     %{name}-doc
Provides:       bundled(python-keypath)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyinstrument = %{version}-%{release}
# /oreon:deps
%description

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

%build

%pyproject_wheel
export PYTHONPATH=$(echo $PWD/build/lib.linux-*)
make -C docs man
make -C docs html
rm examples/django_example/.gitignore
%py3_shebang_fix examples/django_example/manage.py
%install
%pyproject_install
install -m0644 -Dt %{buildroot}%{_mandir}/man1/ docs/_build/man/pyinstrument.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

mv pyinstrument _pyinstrument
TESTOPTS=(
    --deselect=test/test_profiler_async.py::test_greenlet
    --deselect=test/test_profiler_async.py::test_strict_with_greenlet
    --deselect=test/test_profiler.py::test_class_methods
    --deselect=test/low_level/test_frame_info.py::test_frame_info_with_classes
)
%pytest -v test/ "${TESTOPTS[@]}"
%files
%files -n pyinstrument-doc -f %{oreon_filedir}/pyinstrument-doc.list

%changelog

%autochangelog
