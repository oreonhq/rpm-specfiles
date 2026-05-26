Name:           pyxattr
Summary:        Extended attributes library wrapper for Python
Version:        0.7.2
Release:        19%{?dist}
License:        LGPL-2.1-or-later
URL:            https://pyxattr.k1024.org/
Source0:        https://pyxattr.k1024.org//downloads/pyxattr-0.7.2.tar.gz
Source1:        https://pyxattr.k1024.org//downloads/pyxattr-0.7.2.tar.gz.asc
Source2:        https://k1024.org/files/key.asc
# oreon url source checksums begin
%global source0_sha256 68477027e6d3310669f98aaef15393bfcd9b2823d7a7f00a6f1d91a3c971ae64
%global source0_file pyxattr-0.7.2.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  libattr-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gnupg2
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Python extension module wrapper for libattr. It allows to query, list,
add and remove extended attributes from files and directories.}

%description %_description

%package -n python3-%{name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name} %_description

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pyxattr-0.7.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "68477027e6d3310669f98aaef15393bfcd9b2823d7a7f00a6f1d91a3c971ae64" || { echo "oreon: Source0 SHA256 mismatch for pyxattr-0.7.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%py3_build

%install
%py3_install

%check
# selinux in koji produces unexpected xattrs for tests
export TEST_IGNORE_XATTRS=security.selinux
# the module is just a C extension => need to add the installed destination to
# PYTHONPATH, otherwise it won't be found
export PYTHONPATH=%{buildroot}%{python3_sitearch}:$PYTHONPATH
# in Copr, skip tests that fail with OSError: [Errno 95] Operation not supported
python3 -m pytest tests %{?copr_projectname:-k 'not (binary_payload or create_on_existing or empty_value or large_value or many_ops or mixed_access or set_get_remove)'}

%files -n python3-%{name}
%{python3_sitearch}/xattr.cpython-%{python3_version_nodots}*
%{python3_sitearch}/*egg-info
%license COPYING
%doc NEWS README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.2-19
- Prepare for Oreon 11 (RP1)
