%global source0_hash 24d49b1f348b6d85ab5ee886b240d38b983574e995bf38c18bbbe4c01865d950
Name:           python-call-graph
Version:        2.1.6
Release:        1%{?dist}
Summary:        Visualises the flow of your Python application
License:        GPL-2.0-only
URL:            https://github.com/lewiscowles1986/py-call-graph/
Source0:        https://files.pythonhosted.org/packages/source/p/python-call-graph/python-call-graph-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-call-graph = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-python-call-graph
Summary:        Visualises the flow of your Python application
%description -n python3-python-call-graph

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir python-call-graph-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1/
cp -pr man/pycallgraph.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles python3-python-call-graph usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%files
%files -n python3-python-call-graph -f %{oreon_filedir}/python3-python-call-graph.list

%changelog

%autochangelog
