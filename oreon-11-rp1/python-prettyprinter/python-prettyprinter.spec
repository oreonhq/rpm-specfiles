%global source0_hash 9fe5da7ec53510881dd35d7a5c677ba45f34cfe6a8e78d1abd20652cf82139a8
Name:           python-prettyprinter
Version:        0.18.0
Release:        1%{?dist}
Summary:        Syntax-highlighting, declarative and composable pretty printer
License:        MIT
URL:            https://github.com/tommikaikkonen/prettyprinter
BuildArch:      noarch
Source0:        https://files.pythonhosted.org/packages/source/p/prettyprinter/prettyprinter-%{version}.tar.gz
Patch:          0001-Avoid-build-requirement-on-pytest-runner.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-prettyprinter = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-prettyprinter
Summary:        Syntax-highlighting, declarative and composable pretty printer
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-attrs
BuildRequires:  python3-ipython
BuildRequires:  python3-pytz
%description -n python3-prettyprinter

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir prettyprinter-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-prettyprinter usr/lib/python3*/site-packages/prettyprinter* usr/lib64/python3*/site-packages/prettyprinter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/prettyprinter* usr/lib64/python3*/site-packages/prettyprinter* usr/bin/*

%check

%pytest \
    --ignore tests/test_django \
    --ignore tests/test_ast.py \
    --ignore tests/test_numpy.py \
    --ignore tests/test_requests.py \
    --verbose
%files
%files -n python3-prettyprinter -f %{oreon_filedir}/python3-prettyprinter.list

%changelog

%autochangelog
