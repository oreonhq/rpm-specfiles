%global source0_hash 714a106ac5d4266ee2caa8f74c8e04111de9e2b7b77680ca41008ef628045751

Name:           R-rsvg
Version:        %R_rpm_version 2.7.0
Release:        %autorelease
Summary:        Render SVG Images into PDF, PNG, PostScript, or Bitmap Arrays

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  librsvg2-devel

%description
Renders vector-based svg images into high-quality custom-size bitmap arrays
using 'librsvg2'. The resulting bitmap can be written to e.g. png, jpeg or webp
format. In addition, the package can convert images directly to various formats
such as pdf or postscript.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f rsvg/tests/spelling.R # devel stuff

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
