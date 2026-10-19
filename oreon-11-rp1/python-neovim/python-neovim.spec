%global source0_hash 6649d630ce4a94007fe69a8debb010c7b185057f36d61576d2542c90f3c8db99
%global desc Implements support for python plugins in Nvim. Also works as a library for\
connecting to and scripting Nvim processes through its msgpack-rpc API.
%bcond check 1
%bcond sphinx 1
Name:           python-neovim
Version:        0.6.0
Release:        1%{?dist}
License:        Apache-2.0
Summary:        Python client to Neovim
URL:            https://github.com/neovim/pynvim
Source0:        https://github.com/neovim/pynvim/archive/%{version}/pynvim-%{version}.tar.gz
BuildArch:      noarch
%if %{with check}
%endif
%if %{with sphinx}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-neovim = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n python%{python3_pkgversion}-neovim
Summary:        Python client to Neovim
%{?python_provide:%python_provide python%{python3_pkgversion}-neovim}
Requires:       neovim
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-greenlet
Requires:       python%{python3_pkgversion}-msgpack
%endif
%description -n python%{python3_pkgversion}-neovim
%{desc}

%if %{with sphinx}
%package doc
Summary:        Documentation for %{name}
%description doc
%{desc}

This package contains documentation in HTML format.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pynvim-%{version}
%oreon_prep
%build

%pyproject_wheel
%if %{with sphinx}
pushd docs
make html
rm -f _build/html/.buildinfo
popd
%endif
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/neovim* usr/lib64/python3*/site-packages/neovim* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%tox run -- -- -k 'not test_broadcast'
%endif
%files
%files -n python3-neovim -f %{oreon_filedir}/python3-neovim.list
%files -n python-neovim-doc -f %{oreon_filedir}/python-neovim-doc.list

%changelog

%autochangelog
