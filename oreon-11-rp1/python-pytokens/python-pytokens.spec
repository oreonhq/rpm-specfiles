%global source0_hash 292052fe80923aae2260c073f822ceba21f3872ced9a68bb7953b348e561179a
Name:           python-pytokens
Version:        0.4.1
Release:        1%{?dist}
Summary:        A fast, spec compliant Python 3.14+ tokenizer
License:        MIT
URL:            https://github.com/tusharsadhwani/pytokens
Source0:        https://files.pythonhosted.org/packages/source/p/pytokens/pytokens-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 69
Requires:       python3-pytokens = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytokens+dev
Summary:        Metapackage for python3-pytokens dev extras
Requires:       python3-pytokens = %{version}-%{release}
Provides:       python3dist(pytokens[dev]) = %{version}-%{release}

%description -n python3-pytokens+dev
Metapackage for python3-pytokens dev extras.

%description

%package -n python3-pytokens
Summary:        A fast, spec compliant Python 3.14+ tokenizer
%description -n python3-pytokens

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytokens-%{version}
%oreon_prep
%build

export PYTOKENS_USE_MYPYC=0
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytokens usr/lib/python3*/site-packages/pytokens* usr/lib64/python3*/site-packages/pytokens* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytokens* usr/lib64/python3*/site-packages/pytokens* usr/bin/*

%check

%pytest --override-ini addopts=
%files
%files -n python3-pytokens -f %{oreon_filedir}/python3-pytokens.list

%changelog

%autochangelog
