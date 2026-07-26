%global source0_hash 1a4fe663e11f0751bda47bf39d2d60c069170047cb7e9e54577372846e138b99

Name:           python-logdetective
Version:        3.2.0
Release:        %autorelease
Summary:        Uses LLM AI to search for build/test failure and provide ideas how to fix it

License:        Apache-2.0
URL:            https://pypi.org/project/logdetective/
Source:         %{pypi_source logdetective}

BuildArch:      noarch
BuildRequires:  python3-devel

# this is what llama-cpp is on
ExclusiveArch:  x86_64 aarch64

# for man page
BuildRequires:  asciidoc
BuildRequires:  libxslt

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
A Python tool to analyze logs using a Language Model (LLM) and Drain template
miner.
}

%description %_description

%package -n     python3-logdetective
Summary:        %{summary}
Provides:       logdetective

%description -n python3-logdetective %_description

%pyproject_extras_subpkg -n python3-logdetective server
%pycached %{python3_sitelib}/logdetective/server/*.py

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n logdetective-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
a2x -d manpage -f manpage logdetective.1.asciidoc

%install
%pyproject_install
%pyproject_save_files 'logdetective'
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 logdetective.1 %{buildroot}/%{_mandir}/man1/
rm %{buildroot}/%{python3_sitelib}/logdetective.1.asciidoc || :

%check
#server is broken for now
%pyproject_check_import -e logdetective.server*

%files -n python3-logdetective -f %{pyproject_files}
%{_bindir}/logdetective
%license LICENSE
%doc README.md
%pycached %exclude %{python3_sitelib}/logdetective/server/*.py
%{_mandir}/man1/logdetective.1*

%changelog
%autochangelog
