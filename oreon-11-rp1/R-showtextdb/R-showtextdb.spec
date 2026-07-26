%global source0_hash 027f5d0ab91eb27c72b6e918a2915b6087f7408b66c1630d69b3e507dd609642

Name:           R-showtextdb
Version:        %R_rpm_version 3.0
Release:        %autorelease
Summary:        Font Files for the 'showtext' Package

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}
Patch:          0001-Load-existing-font-file.patch

BuildArch:      noarch
BuildRequires:  R-devel
BuildRequires:  wqy-microhei-fonts
Requires:       wqy-microhei-fonts

%description
Providing font files that can be used by the 'showtext' package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1
rm showtextdb/inst/{AUTHORS,COPYRIGHTS}

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
pushd %{buildroot}%{_R_libdir}/showtextdb
    rm fonts/*
    ln -s /usr/share/fonts/wqy-microhei-fonts/wqy-microhei.ttc fonts/wqy-microhei.ttc
popd

%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
