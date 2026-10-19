%global source0_hash b8f21c722a05b622a431c53fce748cc8cad52f4791e843e6340dd198477ddabd
Name:           R-ragg
Version:        %R_rpm_version 1.5.0
Release:        1%{?dist}
Summary:        Graphic Devices Based on AGG
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=ragg&version=%{version}#/ragg_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
# /oreon:deps
%description
Anti-Grain Geometry (AGG) is a high-quality and high-performance 2D drawing
library. The 'ragg' package provides a set of graphic devices based on AGG
to use as alternative to the raster devices provided through the
'grDevices' package.

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
