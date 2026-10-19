%global source0_hash 7ed2c90486967058a73a547781121983839522d67041ae52c4979616f1b2b746
%bcond tests 1
Name:           python-markdown-callouts
Version:        0.4.0
Release:        1%{?dist}
Summary:        Markdown extension to provide a classier syntax for admonitions
License:        MIT
URL:            https://oprypin.github.io/markdown-callouts
Source0:        https://files.pythonhosted.org/packages/source/m/markdown_callouts/markdown_callouts-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-markdown-callouts = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-markdown-callouts
Summary:        Markdown extension to provide a classier syntax for admonitions
# oreon:reqs
Requires:       python3dist(markdown) >= 3.3.3
# /oreon:reqs
%description -n python3-markdown-callouts

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir markdown_callouts-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-markdown-callouts usr/lib/python3*/site-packages/markdown_callouts* usr/lib64/python3*/site-packages/markdown_callouts* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/markdown_callouts* usr/lib64/python3*/site-packages/markdown_callouts* usr/bin/*

%check

%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif
%files
%files -n python3-markdown-callouts -f %{oreon_filedir}/python3-markdown-callouts.list

%changelog

%autochangelog
