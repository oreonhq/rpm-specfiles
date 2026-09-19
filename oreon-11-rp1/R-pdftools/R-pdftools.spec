%global source0_hash 4529a7669baaadbfbbb328c8c75d34c86f51cab5071945ff9cedd8f633f421c4

Name:           R-pdftools
Version:        %R_rpm_version 3.6.0
Release:        %autorelease
Summary:        Text Extraction, Rendering and Converting of PDF Documents

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  poppler-cpp-devel
BuildRequires:  poppler-data

%description
Utilities based on 'libpoppler' for extracting text, fonts, attachments and
metadata from a PDF file. Also supports high quality rendering of PDF documents
into PNG, JPEG, TIFF format, or into raw bitmap vectors for further processing
in R.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
