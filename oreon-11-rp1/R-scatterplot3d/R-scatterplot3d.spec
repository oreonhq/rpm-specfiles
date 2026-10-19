%global source0_hash 1c9c08348c3ed925f59df40cb73accc9e1a169ccfb1e8571f105f40fa98e6ec2
Name:           R-scatterplot3d
Version:        %R_rpm_version 0.3-44
Release:        1%{?dist}
Summary:        3D Scatter Plot
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=scatterplot3d&version=0.3-44#/scatterplot3d_0.3-44.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Plots a three dimensional (3D) point cloud.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Fix encoding.
iconv --from=latin1 --to=UTF-8 scatterplot3d/inst/CITATION > CITATION.new && \
touch -r scatterplot3d/inst/CITATION CITATION.new && \
mv CITATION.new scatterplot3d/inst/CITATION
sed -i 's/latin1/UTF-8/g' scatterplot3d/DESCRIPTION

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
