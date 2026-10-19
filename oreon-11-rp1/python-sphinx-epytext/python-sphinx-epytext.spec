%global source0_hash 4cc5ba92693ee8853d841c03db434606275506bb418da5bb7538766c696d5e30
Name:           python-sphinx-epytext
Version:        0.0.4
Release:        1%{?dist}
Summary:        Sphinx epytext extension
License:        MIT
URL:            https://github.com/jayvdb/sphinx-epytext
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx-epytext/sphinx-epytext-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinx-epytext = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinx-epytext
Summary:        Sphinx epytext extension
%description -n python3-sphinx-epytext

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sphinx-epytext-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-epytext usr/lib/python3*/site-packages/sphinx_epytext* usr/lib64/python3*/site-packages/sphinx_epytext* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_epytext* usr/lib64/python3*/site-packages/sphinx_epytext* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-sphinx-epytext -f %{oreon_filedir}/python3-sphinx-epytext.list

%changelog

%autochangelog
