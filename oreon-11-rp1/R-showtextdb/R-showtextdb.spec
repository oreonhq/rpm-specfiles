%global source0_hash 027f5d0ab91eb27c72b6e918a2915b6087f7408b66c1630d69b3e507dd609642
Name:           R-showtextdb
Version:        %R_rpm_version 3.0
Release:        1%{?dist}
Summary:        Font Files for the 'showtext' Package
License:        Apache-2.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=showtextdb&version=%{version}#/showtextdb_%{version}.tar.gz
Patch:          0001-Load-existing-font-file.patch
BuildArch:      noarch
Requires:       wqy-microhei-fonts
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  wqy-microhei-fonts
# /oreon:deps
%description
Providing font files that can be used by the 'showtext' package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1
rm showtextdb/inst/{AUTHORS,COPYRIGHTS}

%build

%install
%R_install
pushd %{buildroot}%{_R_libdir}/showtextdb
    rm fonts/*
    ln -s /usr/share/fonts/wqy-microhei-fonts/wqy-microhei.ttc fonts/wqy-microhei.ttc
popd
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
