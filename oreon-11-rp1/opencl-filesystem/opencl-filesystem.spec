%global source0_hash none
Name:		opencl-filesystem
Version:	1.0
Release:        1%{?dist}
Summary:        OpenCL filesystem layout
License:	LicenseRef-Not-Copyrightable
URL:		http://www.khronos.org/registry/cl/
BuildArch:	noarch
# oreon:deps

# /oreon:deps
%description
This package provides some directories required by packages which use OpenCL.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%install
mkdir -p %{buildroot}/%{_sysconfdir}/OpenCL/vendors/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-24
- Prepare for Oreon 11 (RP1)
