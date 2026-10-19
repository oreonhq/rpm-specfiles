%global source0_hash 783692117346074cc8860cc16f7e8b328b05fd040e5c206a869ee351e704e917
Name:           R-docopt
Version:        %R_rpm_version 0.7.2
Release:        1%{?dist}
Summary:        Command-Line Interface Specification Language
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=docopt&version=%{version}#/docopt_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Define a command-line interface by just giving it a description in the specific
format.

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
