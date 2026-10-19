%global source0_hash 34093bf6ec82840f6e80ec6dced1d5ead26637fae5abe63562958c7274e1b8fb
Name:           R-textshaping
Version:        %R_rpm_version 1.0.4
Release:        1%{?dist}
Summary:        Bindings to the HarfBuzz and Fribidi Libraries for Text Shaping
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=textshaping&version=%{version}#/textshaping_%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel <= 1.0.4
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(harfbuzz)
# /oreon:deps
%description
Provides access to the text shaping functionality in the HarfBuzz library and
the bidirectional algorithm in the Fribidi library. textshaping is a low-level
utility package mainly for graphic devices that expands upon the font tool-set
provided by the systemfonts package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
