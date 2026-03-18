Name:		opencl-filesystem
Version:	1.0
Release:	24%{?dist}
Summary:	OpenCL filesystem layout

License:	LicenseRef-Not-Copyrightable
URL:		http://www.khronos.org/registry/cl/

BuildArch:	noarch


%description
This package provides some directories required by packages which use OpenCL.


%prep


%install
# ICD Loader Vendor Enumeration
# http://www.khronos.org/registry/cl/extensions/khr/cl_khr_icd.txt
mkdir -p %{buildroot}/%{_sysconfdir}/OpenCL/vendors/


%files
%{_sysconfdir}/OpenCL/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-24
- Prepare for Oreon 11 (RP1)
