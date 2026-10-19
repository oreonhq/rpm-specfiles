%global source0_hash 8ab635151e2408cccdc3f028ba01ef0115d9be26a878e14186fde1fd8b7e68eb
Name:           R-tesseract
Version:        %R_rpm_version 5.2.4
Release:        1%{?dist}
Summary:        Open Source OCR Engine
License:        Apache-2.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=tesseract&version=%{version}#/tesseract_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  pkgconfig(lept)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  tesseract-langpack-eng
# /oreon:deps
%description
Bindings to 'Tesseract' <https://opensource.google/projects/tesseract>: a
powerful optical character recognition (OCR) engine that supports over 100
languages. The engine is highly configurable in order to tune the detection
algorithms and obtain the best possible results.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f tesseract/tests/spelling.R # unconditional suggest, should be fixed

%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
