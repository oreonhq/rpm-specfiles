%global source0_hash e6005a500b75f8a961593fb67d46085107dadb116f59a5c3b524aa0697945b66
Name:           python-bids-validator
Version:        1.14.7.post0
Release:        1%{?dist}
Summary:        Validator for the Brain Imaging Data Structure
License:        MIT AND Unlicense
URL:            https://github.com/bids-standard/bids-validator
Source0:        https://files.pythonhosted.org/packages/source/b/bids_validator/bids_validator-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
A library of helper functions written in Python, for use with BIDS compliant
applications written in this language.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-bids-validator = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-bids-validator
Summary:        Validator for the Brain Imaging Data Structure
# oreon:reqs
Requires:       python3dist(bidsschematools) >= 0.10
# /oreon:reqs
%description -n python3-bids-validator %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bids_validator-%{version}
%oreon_prep
%build

mv -v bids_validator/test_*.py ./
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bids-validator usr/lib/python3*/site-packages/bids_validator* usr/lib64/python3*/site-packages/bids_validator* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bids_validator* usr/lib64/python3*/site-packages/bids_validator* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-bids-validator -f %{oreon_filedir}/python3-bids-validator.list

%changelog

%autochangelog
