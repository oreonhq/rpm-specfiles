%global source0_hash 51f370165c124904b907e78f6f0192b88ce2df5a93835cddd11565a328709976
Name:           R-pkgload
Version:        %R_rpm_version 1.4.1
Release:        1%{?dist}
Summary:        Simulate Package Installation and Attach
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=pkgload&version=%{version}#/pkgload_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Simulates the process of installing a package and then attaching it. This
is a key part of the 'devtools' package as it allows you to rapidly iterate
while developing a package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
