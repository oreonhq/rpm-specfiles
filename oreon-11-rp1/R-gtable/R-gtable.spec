%global source0_hash d305a5fa11278b649d2d8edc5288bf28009be888a42be58ff8714018e49de0ef
Name:           R-gtable
Version:        %R_rpm_version 0.3.6
Release:        1%{?dist}
Summary:        Arrange 'Grobs' in Tables
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=gtable&version=%{version}#/gtable_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Tools to make it easier to work with "tables" of 'grobs'. The 'gtable'
package defines a 'gtable' grob class that specifies a grid along with a
list of grobs and their placement in the grid. Further the package makes
it easy to manipulate and combine 'gtable' objects so that complex
compositions can be build up sequentially.

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
