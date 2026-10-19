%global source0_hash 04db2163ca9acb640161fb84dfc492f16abc6f5acc0c64782c197457e15004ac
Name:           R-tikzDevice
Version:        %R_rpm_version 0.12.6
Release:        1%{?dist}
Summary:        R Graphics Output in LaTeX Format
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=tikzDevice&version=%{version}#/tikzDevice_%{version}.tar.gz
ExcludeArch:    %{ix86}
Requires:       texlive-pgf
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  texlive-pgf
# /oreon:deps
%description
Provides a graphics output device for R that records plots in a LaTeX-friendly
format. The device transforms plotting commands issued by R functions into
LaTeX code blocks. When included in a LaTeX document, these blocks are
interpreted with the help of 'TikZ'---a graphics package for TeX and friends
written by Till Tantau. Using the 'tikzDevice', the text of R plots can contain
LaTeX commands such as mathematical formula. The device also allows arbitrary
LaTeX code to be inserted into the output stream.

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
