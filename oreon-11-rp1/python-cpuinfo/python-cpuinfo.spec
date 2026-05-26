%global srcname cpuinfo
%global sum Getting CPU info

Name:           python-%{srcname}
Version:        9.0.0
Release:        17%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/workhorsy/py-cpuinfo
Source0:        https://files.pythonhosted.org/packages/source/p/py-%{srcname}/py-%{srcname}-%{version}.tar.gz

# s390x support
Patch0:         py-cpuinfo-s390x.patch
# oreon url source checksums begin
%global source0_sha256 3cdbbf3fac90dc6f118bfd64384f309edeadd902d7c8fb17f02ffa1fc3f49690
%global source0_file py-cpuinfo-9.0.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch

# https://github.com/workhorsy/py-cpuinfo/issues/55
# ExclusiveArch:  %%{ix86} x86_64 %%{power64} s390x noarch

BuildRequires:  python3-devel

%description
Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work without
any extra programs or libraries, beyond what your OS provides.

These approaches are used for getting info:
    Windows Registry
    /proc/cpuinfo
    sysctl
    dmesg
    isainfo and psrinfo
    Querying x86 CPUID register


%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work without
any extra programs or libraries, beyond what your OS provides.

These approaches are used for getting info:
    Windows Registry
    /proc/cpuinfo
    sysctl
    dmesg
    isainfo and psrinfo
    Querying x86 CPUID register

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/py-cpuinfo-9.0.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3cdbbf3fac90dc6f118bfd64384f309edeadd902d7c8fb17f02ffa1fc3f49690" || { echo "oreon: Source0 SHA256 mismatch for py-cpuinfo-9.0.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n py-%{srcname}-%{version}
rm -rf *.egg-info

sed -i -e '/^#!\//, 1d' cpuinfo/cpuinfo.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%check
%pyproject_check_import

%{python3} -m unittest test_suite.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst ChangeLog
%{_bindir}/cpuinfo


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.0.0-17
- Prepare for Oreon 11 (RP1)
