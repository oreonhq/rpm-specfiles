%global source0_hash 34093bf6ec82840f6e80ec6dced1d5ead26637fae5abe63562958c7274e1b8fb

Name:           R-textshaping
Version:        %R_rpm_version 1.0.4
Release:        %autorelease
Summary:        Bindings to the HarfBuzz and Fribidi Libraries for Text Shaping

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(harfbuzz)
Obsoletes:      %{name}-devel <= 1.0.4

%description
Provides access to the text shaping functionality in the HarfBuzz library and
the bidirectional algorithm in the Fribidi library. textshaping is a low-level
utility package mainly for graphic devices that expands upon the font tool-set
provided by the systemfonts package.

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
%R_check

%files -f %{R_files}

%changelog
%autochangelog
