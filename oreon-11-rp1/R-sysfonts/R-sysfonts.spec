%global source0_hash 52459c34a625a049d22ea6d6ab799428b954783da04a7c4487d47684b8659f88

Name:           R-sysfonts
Version:        %R_rpm_version 0.8.9
Release:        %autorelease
Summary:        Loading Fonts into R

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  liberation-mono-fonts
BuildRequires:  liberation-sans-fonts
BuildRequires:  liberation-serif-fonts
Requires:       liberation-mono-fonts
Requires:       liberation-sans-fonts
Requires:       liberation-serif-fonts

%description
Loading system fonts and Google Fonts <https://fonts.google.com/> into R,
in order to support other packages such as 'R2SWF' and 'showtext'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
pushd %{buildroot}%{_R_libdir}/sysfonts/fonts
rm AUTHORS License.txt
for family in Mono Sans Serif; do
    family_lower="${family,,}"
    for style in Regular Bold Italic BoldItalic; do
        rm Liberation${family}-${style}.ttf
        ln -s /usr/share/fonts/liberation-${family_lower}-fonts/Liberation${family}-${style}.ttf
    done
done
popd

%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
