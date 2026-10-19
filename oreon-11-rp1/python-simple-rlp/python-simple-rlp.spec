%global source0_hash 2df1d2b769f0a0177d26231ab8be16e65e3546b17bb0a9a490efd3517c082876
Name:      python-simple-rlp
Version:   0.1.3
Release:        1%{?dist}
Summary:        Simple RLP (Recursive Length Prefix)
License:   MIT
URL:       https://github.com/SamuelHaidu/simple-rlp
Source0:        https://files.pythonhosted.org/packages/source/s/simple-rlp/simple-rlp-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-simple-rlp = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-simple-rlp
Summary:        Simple RLP (Recursive Length Prefix)
%description -n python3-simple-rlp

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n simple-rlp-%{version}
sed -i 's/\r$//' README.md

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-simple-rlp usr/lib/python3*/site-packages/simple_rlp* usr/lib64/python3*/site-packages/simple_rlp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/simple_rlp* usr/lib64/python3*/site-packages/simple_rlp* usr/bin/*

%check

%files
%files -n python3-simple-rlp -f %{oreon_filedir}/python3-simple-rlp.list

%changelog

%autochangelog
