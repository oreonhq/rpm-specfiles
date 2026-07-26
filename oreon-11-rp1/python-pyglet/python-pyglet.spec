%global source0_hash 9ec8c64dff5557939495f0be0737ecfa12671574207ac1c088082074d6de2c7d

%global srcname pyglet
%global versionedname %{srcname}-%{version}

%bcond_without tests

Name: python-%{srcname}
Version: 2.0.10
Release: 10%{?dist}
Summary: A cross-platform windowing and multimedia library for Python

License: BSD-3-Clause
URL: http://www.pyglet.org/

# The upstream tarball includes some non-free files in the examples and tests,
# and a patented texture compression algorithm.
# Run the following (in rpmbuild/SOURCES) to generate the distributed tarball
# (the subcommand outputs a version number like 1.5.16):
# $ bash pyglet-get-tarball.sh $(grep Version python-pyglet.spec|cut -c10-)
# See the script for details.
Source0: %{versionedname}-repacked.tar.gz
Source1: pyglet-get-tarball.sh

# Note that unbundling pypng removes "PNGImageDecoder", which is normally
# available for advanced use cases. Instead of:
#     img = image.load(fname, decoder=PNGImageDecoder) # don't use!
# It is enough to let Pyglet choose an appropriate decoder with:
#     img = image.load(fname)
# Pyglet docs even discourage hard-coding the decoder "unless your application
# has to work around specific deficiences in an operating system decoder":
#   https://pyglet.readthedocs.io/en/latest/programming_guide/image.html?highlight=PILImageDecoder#loading-an-image
# If you do find an issue with the default decoder on Fedora, file a bug.

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

# Tests need OpenGL
# See also: https://bugzilla.redhat.com/show_bug.cgi?id=904851
%global __pytest xvfb-run -s '-screen 0 640x480x24' pytest
%if %{with tests}
BuildRequires: /usr/bin/xvfb-run mesa-dri-drivers
BuildRequires: python3-pytest
# These two for gdkpixbuf2 tests
BuildRequires: gtk2-devel
BuildRequires: gdk-pixbuf2-devel
# libpurple has sound files unbundled in the repacked tarball
BuildRequires: libpurple
# These tests fail in koji, likely due to missing devices
#BuildRequires: openal-soft
# These are not specified by upstream
BuildRequires: python3-gobject
# Some tests fail if this is present
# https://github.com/pyglet/pyglet/issues/875
#BuildRequires: python3-pytest-asyncio
%endif
Requires:       python3-gobject

%global _description %{expand:
This library provides an object-oriented programming interface for developing
games and other visually-rich applications with Python.
pyglet has virtually no external dependencies. For most applications and game
requirements, pyglet needs nothing else besides Python, simplifying
distribution and installation. It also handles multiple windows and
fully aware of multi-monitor setups.

pyglet might be seen as an alternative to PyGame.
}

%generate_buildrequires
%pyproject_buildrequires

%description %_description

%package -n python3-%{srcname}
Summary: A cross-platform windowing and multimedia library for Python 3

%{?python_provide:%python_provide python3-%{srcname}}

# The libraries are imported dynamically using ctypes, so rpm can't find them.
Requires: libGL
Requires: libGLU
Requires: libX11
Requires: fontconfig

# Needed for experimental headless mode; see: https://github.com/pyglet/pyglet/issues/51
Suggests: libEGL

# Pillow is technically optional, but in Fedora we always pull it in.
# It can open PNG images, so we can remove the bundled "png.py"
Requires: python3-pillow

%if %{with tests}
BuildRequires: libGL
BuildRequires: libGLU
BuildRequires: libEGL
BuildRequires: libX11
BuildRequires: fontconfig
BuildRequires: python3-pillow
%endif

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{versionedname}

# Remove the bundled pypng library (python-pillow provides the same functionality)
rm pyglet/image/codecs/png.py
rm pyglet/extlibs/png.py

# Get rid of hashbang lines. This is a library, it has no executable scripts.
# Also remove Windows newlines
find . -name '*.py' | xargs sed --in-place -e's|#!/usr/bin/\(env \)\?python||;s/\r//'

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pyglet

%if %{with tests}
%check
# Skip flaky tests
export CI=on

# The files are unbundled in the repacked tarball
ln -s %{_datadir}/sounds/purple/*.wav tests/data/media/

# Interactive tests are skipped for obvious reasons.
# Media player tests are skipped -- we don't have PulseAudio running.
# test_find_font_match & test_have_font skipped -- they look for a font named 'arial'
# test_font & test_freetype_face tests are skipped -- they depend on non-free font we remove
# test_push_handlers_instance has broken mocking: https://github.com/pyglet/pyglet/issues/606
# GdkPixBufTest.test_load_animation uses dinosaur.gif which we remove
%pytest \
    -vv \
    --non-interactive \
    --ignore=tests/interactive \
    --ignore=tests/integration/media \
    -m 'not (requires_user_action or requires_user_validation or only_interactive)' \
    -k 'not (test_find_font_match or test_font or test_have_font or test_freetype_face or test_openal_listener or test_push_handlers_instance)' \
    --deselect tests/integration/image/test_gdkpixbuf2.py::GdkPixBufTest::test_load_animation \
    tests
%endif

%files -n python3-%{srcname} -f %%{pyproject_files}
%license LICENSE
%doc README.md RELEASE_NOTES

%changelog
%autochangelog
