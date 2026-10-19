%global source0_hash 91c6da10b5bb6f2e9e25345829fb8278c78af019f6fc40887ad49b060483b1d7
Name:           python-docopt-ng
Version:        0.9.0
Release:        1%{?dist}
Summary:        Humane command line arguments parser
License:        MIT
URL:            https://github.com/jazzband/docopt-ng
Source0:        https://files.pythonhosted.org/packages/source/d/docopt_ng/docopt_ng-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-docopt-ng = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-docopt-ng
Summary:        Humane command line arguments parser
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
Conflicts:      python3-docopt
%description -n python3-docopt-ng

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir docopt_ng-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-docopt-ng usr/lib/python3*/site-packages/docopt_ng* usr/lib64/python3*/site-packages/docopt_ng* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/docopt_ng* usr/lib64/python3*/site-packages/docopt_ng* usr/bin/*

%check

%pytest
%files
%files -n python3-docopt-ng -f %{oreon_filedir}/python3-docopt-ng.list

%changelog

%autochangelog
