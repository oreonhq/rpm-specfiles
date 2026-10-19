%global source0_hash c3132a0ed9032dfe5d256ab74a0870e75a39d148e6e4a7e46c26fcda9001db10
%bcond blender 1
%bcond skimage 1
Name:           python-trimesh
Version:        5.1.0
Release:        1%{?dist}
Summary:        Import, export, process, analyze and view triangular meshes
License:        MIT AND BSD-3-Clause
URL:            https://trimsh.org
Source0:        https://github.com/mikedh/trimesh/archive/%{version}/trimesh-%{version}.tar.gz
Source1:        trimesh.1
%global debug_package %{nil}
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-trimesh = %{version}-%{release}
# /oreon:deps
%package -n       python3-trimesh+easy
Summary:        Metapackage for python3-trimesh easy extras
Requires:       python3-trimesh = %{version}-%{release}
Requires:       python3dist(manifold3d) >= 2.3.0
Requires:       python3dist(mapbox-earcut) >= 1.0.2
Provides:       python3dist(trimesh[easy]) = %{version}-%{release}

%description -n python3-trimesh+easy
Metapackage for python3-trimesh easy extras.

%package -n       python3-trimesh+recommend
Summary:        Metapackage for python3-trimesh recommend extras
Requires:       python3-trimesh = %{version}-%{release}
Requires:       python3dist(pyglet) < 2
Provides:       python3dist(trimesh[recommend]) = %{version}-%{release}

%description -n python3-trimesh+recommend
Metapackage for python3-trimesh recommend extras.

%package -n       python3-trimesh+test
Summary:        Metapackage for python3-trimesh test extras
Requires:       python3-trimesh = %{version}-%{release}
Provides:       python3dist(trimesh[test]) = %{version}-%{release}

%description -n python3-trimesh+test
Metapackage for python3-trimesh test extras.

%package -n       python3-trimesh+test_more
Summary:        Metapackage for python3-trimesh test_more extras
Requires:       python3-trimesh = %{version}-%{release}
Requires:       python3dist(dracopy) >= 1.7.0
Provides:       python3dist(trimesh[test_more]) = %{version}-%{release}

%description -n python3-trimesh+test_more
Metapackage for python3-trimesh test_more extras.

%package -n       python3-trimesh+deprecated
Summary:        Metapackage for python3-trimesh deprecated extras
Requires:       python3-trimesh = %{version}-%{release}
Provides:       python3dist(trimesh[deprecated]) = %{version}-%{release}

%description -n python3-trimesh+deprecated
Metapackage for python3-trimesh deprecated extras.

%package -n       python3-trimesh+all
Summary:        Metapackage for python3-trimesh all extras
Requires:       python3-trimesh = %{version}-%{release}
Provides:       python3dist(trimesh[all]) = %{version}-%{release}

%description -n python3-trimesh+all
Metapackage for python3-trimesh all extras.

%description

%package -n     python3-trimesh
Summary:        Import, export, process, analyze and view triangular meshes
BuildArch:      noarch
Recommends:     python3-trimesh+easy = %{version}-%{release}
Recommends:     python3-trimesh+recommend = %{version}-%{release}
Provides:       bundled(python3dist(pyrender))
Obsoletes:      python3-trimesh+recommends < 4.0.0~~dev0-1
Obsoletes:      python3-trimesh+all < 4.0.0~~dev0-1
%if %{with blender}
BuildRequires:  (blender or python3(s390-64))
Recommends:     (blender or python3(s390-64))
%endif
BuildRequires:  /usr/bin/dot
Recommends:     /usr/bin/dot
BuildRequires:  (draco or python3(s390-64))
Recommends:     (draco or python3(s390-64))
BuildRequires:  /usr/bin/openscad
Recommends:     /usr/bin/openscad
# oreon:reqs
Requires:       python3dist(numpy) >= 1.21
# /oreon:reqs
%description -n python3-trimesh

# We skip packaging the “deprecated” extra, since we no longer wish to maintain
# python-openctm. We therefore cannot package the “all” extra, either.
# Note that the "recommend" extra does have an arch-dependent dependency.

# We elect not to build a documentation package, for the following reasons:
#
#  1. A (relatively simple) patch is required to build them offline without
#     pip-installing requirements from PyPI.
#  2. The documentation includes notebooks translated to HTML from .ipynb
#     using nbconvert.
#      a. Some conversions fail (wholly or on a per-cell basis, if continuing
#         on errors is requested) in architecture-dependent ways. This means
#         that the contents of the documentation package would depend on the
#         builder architecture, and it could not be noarch—an undesirable
#         situation.
#      b. An “HTML-ified” notebook contains a blob of JavaScript and other
#         web assets that is exceptionally difficult (at best, tedious) to
#         account for under current bundling guidelines.
#  3. Sphinx-generated HTML documentation is not suitable for packaging in
#     general—see https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for
#     discussion—and (because of the notebooks, if nothing else) the trimesh
#     documentation is not well-suited to building as a PDF instead of HTML.

%prep

%autosetup -p1
# Stub out unavailable pyinstrument test dependency; we don’t really need to do
# profiling anyway. Note that this does mean that API function
# trimesh.viewer.windowed.SceneViewer(…) will not work with “profile=True”.
#
# Packaging pyinstrument would be difficult due to a vue.js-based HTML
# renderer. Since guidelines forbid pre-built minified or compiled JS or CSS,
# this would have to be patched out, or the web asset pipeline would have to be
# somehow executed in the RPM build environment. (Or, of course, we can
# continue to do without pyinstrument.)
mkdir -p _stub
cat > _stub/pyinstrument.py <<'EOF'
class Profiler(object):
    def __enter__(self, *args, **kwds):
        return self

    def __exit__(self, *args, **kwds):
        return False

    def output_text(self, *args, **kwds):
        return """
Profiling output would be here if pyinstrument were available.
"""

    def print(self, *args, **kwds):
        return self.output_text(*args, **kwds)
EOF

# Patch out unavailable dependencies from extras:

# easy extra:
#   embreex: not packaged, https://github.com/mikedh/embreeX; this would
#            require version 2.x of embree, which was once available in a
#            compat package (https://src.fedoraproject.org/rpms/embree2) but
#            was retired; the current version was 4.x.
#   manifold3d: not yet packaged, https://github.com/elalish/manifold/
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.easy' '(embreex|manifold3d)\b.*'

# recommend extra:
#   pyglet: incompatible version 2.x, beginning with F41. See “Path to
#           supporting Pyglet 2?” https://github.com/mikedh/trimesh/issues/2155
#   manifold3d: not yet packaged, https://github.com/elalish/manifold/
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.recommend' '(pyglet|manifold3d)\b.*'
%if %{without skimage}
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.recommend' 'scikit-image\b.*'
%endif
%ifarch s390x
# The python-cascadio package is currently ExcludeArch: s390x
# python-cascadio: Tests for cascadio fail on s390x, wrong endianness
# https://bugzilla.redhat.com/show_bug.cgi?id=2298452
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.recommend' 'cascadio\b.*'
%endif

# test extra:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#   pytest-cov: linters/coverage/etc.
#   pyinstrument: not packaged; see “stub” workaround in %%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
#   ruff: linters/coverage/etc.
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.test' '(pytest-cov|pyinstrument|ruff)\b.*'

# test_more extra:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#   coveralls: linters/coverage/etc.
#   pyright: linters/coverage/etc.
#   xatlas: not yet packaged, https://github.com/mworchel/xatlas-python;
#           depends on https://github.com/jpcy/xatlas, also not yet packaged
#   pytest-beartype: linters/coverage/etc.
#   pymeshlab: not yet packaged
#   triangle: nonfree license
#   marimo: not yet packaged
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.test_more' \
    '(coveralls|pyright|xatlas|pytest-beartype|pymeshlab|triangle|marimo)\b.*'

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D '%{SOURCE1}'
%oreon_autofiles python3-trimesh usr/lib/python3*/site-packages/trimesh* usr/lib64/python3*/site-packages/trimesh* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/trimesh* usr/lib64/python3*/site-packages/trimesh* usr/bin/*

%build

%pyproject_wheel
%check

%{pyproject_check_import \
  -e trimesh.ray.ray_pyembree \
  -e trimesh.viewer.widget \
  -e trimesh.viewer.windowed \
}
while read -r t
do
  k="${k-}${k+ and }not ($(sed -r 's/::/ and /' <<<"${t}"))"
done < <(sed -r '/^[[:blank:]]*($|#)/d' <<'EOF'
%ifnarch x86_64
CacheTest::test_hash
%endif
%ifarch s390x
GLTFTest::test_export_custom_attributes
OBJTest::test_vertex_color
PermutateTest::test_permutate
PlyTest::test_face_attributes
PlyTest::test_uv_export
PlyTest::test_vertex_attributes
test_boolean
test_multiple
test_multiple_difference
%endif
test_data_model
test_obb_mesh_large
test_primitives
EOF
)
export PYTHONPATH="${PWD}/_stub:%{buildroot}%{python3_sitelib}"
%pytest -v -k "${k-}" -n auto
%pytest -v -k 'test_obb_mesh_large'
%files
%files -n python3-trimesh -f %{oreon_filedir}/python3-trimesh.list

%changelog

%autochangelog
