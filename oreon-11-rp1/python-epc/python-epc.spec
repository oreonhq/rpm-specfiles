%global source0_hash e70e619efd25f2cbe44dfad4ac5613475eca0ad374b2a451b12969ffad705eeb

%global srcname epc

%global _description %{expand:EPC is an RPC stack for Emacs Lisp and Python-EPC is its server side and client
side implementation in Python. Using Python-EPC, you can easily call Emacs Lisp
functions from Python and Python functions from Emacs. For example, you can use
Python GUI module to build widgets for Emacs.}

Name:           python-%{srcname}
Version:        0.0.5
Release:        22%{?dist}
Summary:        EPC (RPC stack for Emacs Lisp) for Python

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://python-epc.readthedocs.org/
Source0:        https://github.com/tkf/%{name}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Drop nose dependency
Patch0:         %{name}-0.0.5-nose.patch

BuildRequires:  python3-devel
BuildArch:      noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       %{py3_dist sexpdata}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license COPYING

%changelog
%autochangelog
