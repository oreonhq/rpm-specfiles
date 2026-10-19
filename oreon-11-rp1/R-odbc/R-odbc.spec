%global source0_hash 7135ea9132f02494b8f39701ea2be613556635c3d50ec0e6a9b224e1d47273fe
Name:           R-odbc
Version:        %R_rpm_version 1.6.4.1
Release:        1%{?dist}
Summary:        Connect to ODBC Compatible Databases (using the DBI Interface)
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=odbc&version=%{version}#/odbc_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  cctz-devel
BuildRequires:  pkgconfig(odbc)
# /oreon:deps
%description
A DBI-compatible interface to ODBC databases.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Remove bundled cctz.
rm -r odbc/src/cctz
# Link against system cctz.
sed -i \
    -e '/PKG_CXXFLAGS/s!-Icctz/include!-I/usr/include/cctz!' \
    -e '/PKG_LIBS/s!-Lcctz !!' \
    -e '/$(OBJECTS):/s!cctz/libcctz.a!!' \
    odbc/src/Makevars.in

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
