%global source0_hash 3ab2c6f099b7f17e383ccb0c4fdd8c27a657ba629967d2edb3c768fc3dc315c6
Name:           R-qpdf
Version:        %R_rpm_version 1.4.1
Release:        1%{?dist}
Summary:        Split, Combine and Compress PDF Files
License:        Apache-2.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=qpdf&version=%{version}#/qpdf_%{version}.tar.gz
Patch:          0001-Don-t-download-files-during-build.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  qpdf-devel
# /oreon:deps
%description
Content-preserving transformations transformations of PDF files such as split,
combine, and compress. This package interfaces directly to the 'qpdf' C++ API
and does not require any command line utilities. Note that 'qpdf' does not read
actual content from PDF files: to extract text and data you need the 'pdftools'
package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1
rm -rf qpdf/src/{include,libqpdf} # remove bundled

%build

%install
export EXTERNAL_QPDF=yes
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
