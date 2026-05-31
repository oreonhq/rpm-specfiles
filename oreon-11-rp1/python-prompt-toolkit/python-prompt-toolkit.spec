%global source0_hash 28cde192929c8e7321de85de1ddbe736f1375148b02f2e17edd840042b1be855

%global common_description %{expand:
prompt_toolkit is a library for building powerful interactive command line
applications in Python.}

Name:           python-prompt-toolkit
Version:        3.0.52
Release:        %autorelease
Summary:        Library for building powerful interactive command line applications in Python
License:        BSD-3-Clause
URL:            https://github.com/prompt-toolkit/python-prompt-toolkit
Source:        https://files.pythonhosted.org/packages/source/p/prompt-toolkit/prompt-toolkit-3.0.52.tar.gz
BuildArch:      noarch


%description %{common_description}


%package -n python3-prompt-toolkit
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# https://github.com/jonathanslenders/python-prompt-toolkit/issues/94
Recommends:     python3-pygments


%description -n python3-prompt-toolkit %{common_description}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n prompt_toolkit-%{version}
# Workaround for https://github.com/prompt-toolkit/python-prompt-toolkit/issues/1988
sed -i 's/^__version__ = .*/__version__ = "%{version}"/' src/prompt_toolkit/__init__.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files prompt_toolkit


%check
%pytest


%files -n python3-prompt-toolkit -f %{pyproject_files}
%doc README.rst AUTHORS.rst CHANGELOG


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.52-1
- Prepare for Oreon 11 (RP1)
