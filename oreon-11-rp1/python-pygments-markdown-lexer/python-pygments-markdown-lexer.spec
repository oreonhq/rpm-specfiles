%global source0_hash 4c128c26450b5886521c674d759f95fc3768b8955a7d9c81866ee0213c2febdf
%{!?_licensedir: %global license %%doc}
%global modname pygments-markdown-lexer
%global sum     A Markdown lexer for Pygments to highlight Markdown code snippets
Name:               python-pygments-markdown-lexer
Version:            0.1.0.dev39
Release:        39%{?dist}
Summary:        A Markdown lexer for Pygments to highlight Markdown code snippets
License:            Apache-2.0 AND LicenseRef-Callaway-BSD
URL:                http://pypi.python.org/pypi/pygments-markdown-lexer
Source0:        https://pypi.python.org/packages/source/p/%{modname}/%{modname}-%{version}.zip
BuildArch:          noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pygments
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{sum}

%package -n python3-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python3-%{modname}}
Requires:           python3-pygments
%description -n python3-%{modname}
%{sum}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

%build

%py3_build
%install
%py3_install
rm -rf %{buildroot}/usr/EGG-INFO
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pygments-markdown-lexer -f %{oreon_filedir}/python3-pygments-markdown-lexer.list

%changelog

%autochangelog
