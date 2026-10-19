%global source0_hash 914c071344fea6890f4e9009d8f82a3c941d982179a446ac349b4d82630a496c
%bcond tests 1
%bcond test_examples 0
%bcond doc_pdf 1
Name:           python-niaaml
Version:        2.2.1
Release:        1%{?dist}
Summary:        Python automated machine learning framework
License:        MIT
URL:            https://github.com/firefly-cpp/NiaAML
Source0:        https://github.com/firefly-cpp/NiaAML/archive/%{version}/NiaAML-%{version}.tar.gz
Source10:       niaaml.1
Source11:       niaaml-infer.1
Source12:       niaaml-optimize.1
BuildArch:      noarch
%if %{with tests}
%endif
%if %{with doc_pdf}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-niaaml = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-niaaml
Summary:        Python automated machine learning framework
%description -n python3-niaaml

%package doc
Summary:        Documentation for NiaAML
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n NiaAML-%{version} -p1

# - Don’t bound the version of Python. We must use the system interpreter.
# - Convert SemVer pins to minimum versions, since we can’t generally respect
#   the upper bounds in Fedora.
sed -r -i -e 's/^python ?=/# &/' -e 's/([^#]+ ?= ?")\^/\1>=/' pyproject.toml

# Ensure the Python interpreter path is correct in the example runner script:
sed -r -i 's|\bpython3\b|%{python3}|' examples/run_all.sh

# Fix CRNL (DOS-style) line endings
dos2unix --keepdate paper/paper.bib

# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/conf.py

%build

%pyproject_wheel
%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif
%install
%pyproject_install
install -d \
    '%{buildroot}%{bash_completions_dir}' \
    '%{buildroot}%{zsh_completions_dir}' \
    '%{buildroot}%{fish_completions_dir}'
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
export _TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION=1
'%{buildroot}%{_bindir}/niaaml' --show-completion bash \
    > '%{buildroot}%{bash_completions_dir}/niaaml'
'%{buildroot}%{_bindir}/niaaml' --show-completion zsh \
    > '%{buildroot}%{zsh_completions_dir}/_niaaml'
'%{buildroot}%{_bindir}/niaaml' --show-completion fish \
    > '%{buildroot}%{fish_completions_dir}/niaaml.fish'
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'
%oreon_autofiles python3-niaaml usr/lib/python3*/site-packages/niaaml* usr/lib64/python3*/site-packages/niaaml* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/niaaml* usr/lib64/python3*/site-packages/niaaml* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%pytest
%endif
%if %{with test_examples}
find examples -type f -name '*.py' |
  env %{py3_test_envvars} xargs -r -n 1 -t -P %{_smp_build_ncpus} -I '{}' \
      '%{python3}' '{}'
%endif
%files
%files -n python3-niaaml -f %{oreon_filedir}/python3-niaaml.list
%files -n python-niaaml-doc -f %{oreon_filedir}/python-niaaml-doc.list

%changelog

%autochangelog
