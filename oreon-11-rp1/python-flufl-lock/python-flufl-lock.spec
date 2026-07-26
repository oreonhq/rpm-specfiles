%global source0_hash 61c7246b34d6e5544c8a1fa4dae396d10e16ceb23371a31db22e0a2993d01432

%global pkgname flufl-lock

Name:           python-%{pkgname}
Version:        8.0.2
Release:        9%{?dist}
Summary:        NFS-safe file locking with timeouts for POSIX systems

License:        Apache-2.0
URL:            https://gitlab.com/warsaw/flufl.lock
Source0:        https://files.pythonhosted.org/packages/source/f/flufl.lock/flufl_lock-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# for tests
# we don't actually test code cov.
# upstream default pytest flags have --cov
# so this is easier than a patch.  we add
# the --no-cov flag below to avoid running coverage
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-sybil

%global _description %{expand:
The flufl.lock library provides an NFS-safe file-based locking algorithm
influenced by the GNU/Linux "open(2)" man page, under the description of
the "O_EXCL" option.}

%description %{_description}

%package -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n flufl_lock-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flufl

%check
# this file causes pytest to do weird things
# so let's get it out of the way
rm -f conftest.py
%pytest --no-cov

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.rst docs/

%changelog
%autochangelog
