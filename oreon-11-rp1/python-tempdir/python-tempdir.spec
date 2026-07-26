%global source0_hash 689680ed3ba4cc8347a70e67efc25086ce85b53b9d24a1420899c585bbf7ba8e

%global pname tempdir

%global desc \
Having to manually manage temporary directories is annoying. \
So this class encapsulates temporary directories which just disappear after \
use, including contained directories and files. \
Temporary directories are created with tempfile.mkdtemp and thus safe from \
race conditions. Cleanup might not work on windows if files are still opened. \

Name: python-%{pname}
Version: 0.7.1
Release: 36%{?dist}
Summary: Automatically manage temporary directories, based on tempfile.mkdtemp
License: MIT
URL: https://bitbucket.org/another_thomas/tempdir
Source0: https://pypi.python.org/packages/source/t/%{pname}/%{pname}-%{version}.tar.gz
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-devel

%description -n python3-%{pname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pname}-%{version}
rm -r tempdir.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{pname}

%files -n python3-%{pname} -f %{pyproject_files}
%license docs/license.rst
%doc docs/use.rst

%changelog
%autochangelog
