%global source0_hash 2575fbbf26c22719d1cb882b59602c9900c7f747118ac130883f63419be46a80
Name:           unpaper
Version:        7.0.0
Release:        16%{?dist}
Summary:        Post-processing of scanned and photocopied book pages
SourceLicense:  GPL-2.0-only AND 0BSD AND MIT AND Apache-2.0
License:        GPL-2.0-only AND 0BSD
URL:            https://www.flameeyes.eu/projects/%{name}
Source0:        https://www.flameeyes.eu/files/%{name}-%{version}.tar.xz
Patch0:         unpaper-7.0.0-Use-avformat_alloc_output_context2-to-create-the-out.patch
Patch1:         unpaper-7.0.0-Set-the-update-option-to-suppress-the-ffmpeg-5.1-war.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  python3-pillow
BuildRequires:  python3-sphinx
BuildRequires:  python3dist(pytest)
# /oreon:deps
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
Requires:       python3-pillow
Requires:       python3-pytest
Requires:       python3-pytest-xdist
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%check

%meson_test
%install
%meson_install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a tests %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
export TEST_IMGSRC_DIR=tests/source_images
export TEST_GOLDEN_DIR=tests/golden_images
export TEST_UNPAPER_BINARY=%{_bindir}/unpaper
cd %{_libexecdir}/%{name} && exec pytest -v -n "$(getconf _NPROCESSORS_ONLN)" tests/unpaper_tests.py
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n unpaper-tests -f %{oreon_filedir}/unpaper-tests.list

%changelog

%autochangelog
