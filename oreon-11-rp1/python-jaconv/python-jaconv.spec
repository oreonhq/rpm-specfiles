%global source0_hash 53f6f968276846716f0f37100a6d5c7308cfa1e0c714eb41287d5bb09345c40f
Name:           python-jaconv
Version:        0.5.0
Release:        1%{?dist}
Summary:        Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, Zenkaku and more
License:        ...
URL:            https://github.com/ikegami-yukino/jaconv
Source0:        https://files.pythonhosted.org/packages/source/j/jaconv/jaconv-%{version}.tar.gz
BuildArch:      noarch
Patch0:         https://patch-diff.githubusercontent.com/raw/ikegami-yukino/jaconv/pull/36.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jaconv = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jaconv
Summary:        Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, Zenkaku and more
%description -n python3-jaconv

%prep
%global oreon_srcdir jaconv-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jaconv usr/lib/python3*/site-packages/jaconv* usr/lib64/python3*/site-packages/jaconv* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jaconv* usr/lib64/python3*/site-packages/jaconv* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jaconv -f %{oreon_filedir}/python3-jaconv.list

%changelog

%autochangelog
