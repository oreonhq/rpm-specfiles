%global source0_hash 056ce154238c9b5b8d5dcbcb52e1bc51d33870ce08c8a9ca9496478bd59f4653
Name:           R-pillar
Version:        %R_rpm_version 1.11.1
Release:        1%{?dist}
Summary:        Coloured Formatting for Columns
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=pillar&version=%{version}#/pillar_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides 'pillar' and 'colonnade' generics designed for formatting columns
of data using the full range of colours provided by modern terminals.

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
