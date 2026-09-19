%global source0_hash 3ab2c6f099b7f17e383ccb0c4fdd8c27a657ba629967d2edb3c768fc3dc315c6

Name:           R-qpdf
Version:        %R_rpm_version 1.4.1
Release:        %autorelease
Summary:        Split, Combine and Compress PDF Files

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}
Patch:          0001-Don-t-download-files-during-build.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  qpdf-devel

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

%generate_buildrequires
%R_buildrequires

%build

%install
export EXTERNAL_QPDF=yes
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
