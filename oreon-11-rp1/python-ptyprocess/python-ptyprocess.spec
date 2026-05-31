%global source0_hash 5c5d0a3b48ceee0b48485e0c26037c0acd7d29765ca3fbb5cb3831d347423220

%global srcname ptyprocess

%bcond_without tests

Name:           python-ptyprocess
Version:        0.7.0
Release:        15%{?dist}
Summary:        Run a subprocess in a pseudo terminal

License:        ISC
URL:            https://github.com/pexpect/ptyprocess
Source:        https://files.pythonhosted.org/packages/source/p/python-ptyprocess/python-ptyprocess-0.7.0.tar.gz
# Remove unittest.makeSuite, gone from Python 3.13
Patch:          https://github.com/pexpect/ptyprocess/pull/75.patch

BuildArch:      noarch

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

%package -n python3-ptyprocess
Summary:        Run a subprocess in a pseudo terminal
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-ptyprocess
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n ptyprocess-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ptyprocess

%if %{with tests}
%check
%{__python3} -m pytest -v
%endif

%files -n python3-ptyprocess -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-15
- Prepare for Oreon 11 (RP1)
