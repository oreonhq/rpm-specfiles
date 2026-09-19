%global source0_hash 2575fbbf26c22719d1cb882b59602c9900c7f747118ac130883f63419be46a80

Name:           unpaper
Version:        7.0.0
Release:        16%{?dist}
Summary:        Post-processing of scanned and photocopied book pages
# AUTHORS:      GPL-2.0-only
# constants.h:  GPL-2.0-only
# doc/basic-concepts.md:    GPL-2.0-only
# doc/file-formats.md:      GPL-2.0-only
# doc/image-processing.md:  GPL-2.0-only
# doc/img/*.png.license:    GPL-2.0-only
# doc/unpaper.1.rst:        GPL-2.0-only
# file.c:           GPL-2.0-only
# imageprocess.c:   GPL-2.0-only
# imageprocess.h:   GPL-2.0-only
# LICENSES/0BSD.txt:    0BSD text
# LICENSES/GPL-2.0-only.txt:    GPL-2.0 text
# other files:      GPL-2.0-only
# README.md:        GPL-2.0-only
# version.h.in:     0BSD
## In tests subpackage
# LICENSES/MIT.txt: MIT text
# tests/golden_images/*.license     GPL-2.0-only
# tests/source_images/*.license     GPL-2.0-only
# tests/unpaper_tests.py:           GPL-2.0-only AND MIT
## Not in any binary package
# doc/conf.py:      MIT
# LICENSES/Apache-2.0.txt:      Apache-2.0 text
# meson.build:      MIT
# .dir-locals.el:   MIT
# .editorconfig:    0BSD
# .github/workflows/meson-build-and-test.yml:   Apache-2.0
# .github/workflows/pre-commit.yml: MIT
# .gitignore:       MIT
# .mailmap:         MIT
# .mergify.yml:     MIT
# .pre-commit-config.yaml:  MIT
SourceLicense:  GPL-2.0-only AND 0BSD AND MIT AND Apache-2.0
License:        GPL-2.0-only AND 0BSD
URL:            https://www.flameeyes.eu/projects/%{name}
Source0:        https://www.flameeyes.eu/files/%{name}-%{version}.tar.xz
# Missing a signature, requested by e-mail
# <https://flameeyes.blog/2022/05/10/unpaper-7-0-0-release/>.
#Source1:        https://www.flameeyes.eu/files/%%{name}-%%{version}.tar.xz.sig
## A key exported from keyserver <hkp://pgp.surfnet.nl> on 2022-02-25.
#Source2:        gpgkey-BDAEF3008A1CC62079C2A16847664B94E36B629F.gpg
# 1/2Set an update option to supress a warning with ffmpeg-5.1,
# in upstream after 7.0.0,
# <https://github.com/unpaper/unpaper/issues/113>
Patch0:         unpaper-7.0.0-Use-avformat_alloc_output_context2-to-create-the-out.patch
# 2/2 Set an update option to supress a warning with ffmpeg-5.1,
# in upstream after 7.0.0,
# <https://github.com/unpaper/unpaper/issues/113>
Patch1:         unpaper-7.0.0-Set-the-update-option-to-suppress-the-ffmpeg-5.1-war.patch
BuildRequires:  gcc
#BuildRequires:  gnupg2
BuildRequires:  meson >= 0.57
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  python3-sphinx >= 3.4
# Tests:
BuildRequires:  python3dist(pytest)
# python3-pillow for PIL Python module
BuildRequires:  python3-pillow

%description
unpaper is a post-processing tool for scanned sheets of paper, especially for
book pages that have been scanned from previously created photocopies. The
main purpose is to make scanned book pages better readable on screen after
conversion to PDF. Additionally, unpaper might be useful to enhance the
quality of scanned pages before performing optical character recognition (OCR).

unpaper tries to clean scanned images by removing dark edges that appeared
through scanning or copying on areas outside the actual page content (e.g. dark
areas between the left-hand-side and the right-hand-side of a double-sided
book-page scan).

The program also tries to detect misaligned centering and rotation of pages
and will automatically straighten each page by rotating it to the correct
angle. This process is called "deskewing".

%package tests
Summary:        Tests for %{name}
License:        GPL-2.0-only AND MIT
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# python3-pillow for PIL Python module
Requires:       python3-pillow
Requires:       python3-pytest
# Parallelize tests
Requires:       python3-pytest-xdist

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%{gpgverify} --keyring='%%{SOURCE2}' --signature='%%{SOURCE1}' --data='%%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a tests %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
export TEST_IMGSRC_DIR=tests/source_images
export TEST_GOLDEN_DIR=tests/golden_images
export TEST_UNPAPER_BINARY=%{_bindir}/unpaper
cd %{_libexecdir}/%{name} && exec pytest -v -n "$(getconf _NPROCESSORS_ONLN)" tests/unpaper_tests.py
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%files
%license LICENSES/0BSD.txt LICENSES/GPL-2.0-only.txt
%{_bindir}/unpaper
%{_mandir}/man1/unpaper.*
%doc AUTHORS doc/*.md doc/img NEWS README.md

%files tests
%license LICENSES/MIT.txt
%{_libexecdir}/%{name}

%changelog
%autochangelog
