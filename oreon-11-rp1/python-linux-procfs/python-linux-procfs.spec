%if 0%{?fedora}
%else
%global without_python3 1
%endif

Name: python-linux-procfs
Version: 0.7.4
Release: 2%{?dist}
License: GPL-2.0-only
Summary: Linux /proc abstraction classes
Source: https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 3a15e97b5e19279978e9aab5567416d76b8101f2cc82f95aca0f6f2dade4fbd7
%global source0_file python-linux-procfs-0.7.4.tar.xz
# oreon url source checksums end
URL: https://www.kernel.org/pub/software/libs/python/python-linux-procfs
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

# Patches

%global _description\
Abstractions to extract information from the Linux kernel /proc files.

%description %_description

%package -n python3-linux-procfs
Summary: %summary
%{?python_provide:%python_provide python3-linux-procfs}

%description -n python3-linux-procfs %_description

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/python-linux-procfs-0.7.4.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3a15e97b5e19279978e9aab5567416d76b8101f2cc82f95aca0f6f2dade4fbd7" || { echo "oreon: Source0 SHA256 mismatch for python-linux-procfs-0.7.4.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files procfs

%files -n python3-linux-procfs
%defattr(0755,root,root,0755)
%{_bindir}/pflags
%{python3_sitelib}/procfs/
%defattr(0644,root,root,0755)
%{python3_sitelib}/python_linux_procfs*.dist-info
%license COPYING

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.4-2
- Prepare for Oreon 11 (RP1)
