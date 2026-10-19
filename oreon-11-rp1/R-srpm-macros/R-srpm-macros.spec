%global source0_hash 2a0a297d7295a9eebe2d94c4daa3639328ea51dc984525d35e2404ef98a2e439
Name:           R-srpm-macros
Version:        1.3.7
Release:        1%{?dist}
Summary:        Source-stage rpm automation for R packages
License:        MIT
URL:            https://github.com/rpm-software-management/R-rpm-macros
Source0:        https://github.com/rpm-software-management/R-rpm-macros/archive/refs/tags/v1.3.7.tar.gz#/R-rpm-macros-1.3.7.tar.gz
Patch0:         0001-tests-expect-R-4.6-ABI.patch
BuildArch:      noarch
Requires:       redhat-rpm-config
# oreon:deps
BuildRequires:  R-core
BuildRequires:  make
# /oreon:deps
%description
This package provides SRPM-stage rpm automation to simplify the creation
of R packages.

It limits itself to the automation subset required to create R SRPM packages
and needs to be included in the default build root.

The rest of the automation is provided by the R-rpm-macros package, that
R-srpm-macros will pull in for R packages only.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir R-rpm-macros-%{version}
%oreon_prep
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%check

%make_build test OFFLINE=1
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.7-1
- Import
