%global source0_hash 994d51325d25ad8aa7ce4ebaec003febcce822c3f8c911e3b17c52f7f589f950

%global srcname markdown
%global pkgname markdown

Name:           python-%{pkgname}
Version:        3.10.2
Release:        %autorelease
Summary:        Markdown implementation in Python
License:        BSD-3-Clause
URL:            https://python-markdown.github.io/
Source0:        https://files.pythonhosted.org/packages/source/m/markdown/markdown-3.10.2.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-PyYAML
%if ( 0%{?rhel} && 0%{?rhel} <= 9 )
BuildRequires:  python3-importlib-metadata >= 4.4
Requires:       python3-importlib-metadata >= 4.4
%endif

%global _description %{expand:
This is a Python implementation of John Gruber’s Markdown. It is
almost completely compliant with the reference implementation, though
there are a few very minor differences.}

%description %_description


%package -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname} %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pkgname}

# process license file
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  %{buildroot}%{_bindir}/markdown_py \
  LICENSE.md > LICENSE.html


%check
%python3 -m unittest discover tests


%files -n python3-%{pkgname} -f %{pyproject_files}
# temporarily skip packaging docs - see also
# https://github.com/Python-Markdown/markdown/issues/621
#doc python3/build/docs/*
%license LICENSE.html LICENSE.md
%{_bindir}/markdown_py


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10.2-1
- Prepare for Oreon 11 (RP1)
