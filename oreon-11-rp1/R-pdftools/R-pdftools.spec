%global source0_hash 4529a7669baaadbfbbb328c8c75d34c86f51cab5071945ff9cedd8f633f421c4
Name:           R-pdftools
Version:        %R_rpm_version 3.6.0
Release:        1%{?dist}
Summary:        Text Extraction, Rendering and Converting of PDF Documents
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=pdftools&version=%{version}#/pdftools_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  poppler-cpp-devel
BuildRequires:  poppler-data
# /oreon:deps
%description
Utilities based on 'libpoppler' for extracting text, fonts, attachments and
metadata from a PDF file. Also supports high quality rendering of PDF documents
into PNG, JPEG, TIFF format, or into raw bitmap vectors for further processing
in R.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
