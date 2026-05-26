# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 3a15e97b5e19279978e9aab5567416d76b8101f2cc82f95aca0f6f2dade4fbd7
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
