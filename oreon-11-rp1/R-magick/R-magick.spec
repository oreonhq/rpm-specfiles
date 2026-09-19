%global source0_hash 477d717075651d2d508a66c313fd82b5e530b5ba7603b4a6cafa8c8e8cb6dfba

Name:           R-magick
Version:        %R_rpm_version 2.9.0
Release:        %autorelease
Summary:        Advanced Graphics and Image-Processing in R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(Magick++)

%description
Bindings to 'ImageMagick': the most comprehensive open-source image
processing library available. Supports many common formats (png, jpeg,
tiff, pdf, etc) and manipulations (rotate, scale, crop, trim, flip, blur,
etc). All operations are vectorized via the Magick++ STL meaning they
operate either on a single frame or a series of frames for working with
layers, collages, or animation. In RStudio images are automatically
previewed when printed to the console, resulting in an interactive editing
environment. The latest version of the package includes a native graphics
device for creating in-memory graphics or drawing onto images using pixel
coordinates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f magick/tests/spelling.R # dev stuff

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
