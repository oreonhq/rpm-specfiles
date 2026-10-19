%global source0_hash 85cf7fcc4753a8c86da9a6f454e46c2a58ffc70c4f47cac4d3e3bcefda2a9e9f
Name:           R-assertthat
Version:        %R_rpm_version 0.2.1
Release:        1%{?dist}
Summary:        Easy Pre and Post Assertions
License:        GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=assertthat&version=%{version}#/assertthat_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
An extension to stopifnot() that makes it easy to declare the pre and post
conditions that you code should satisfy, while also producing friendly
error messages so that your users know what's gone wrong.

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
